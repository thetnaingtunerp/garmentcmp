import datetime

from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.db.models import Sum,Count,F,Avg
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic import TemplateView, View, CreateView, DetailView,FormView,ListView,UpdateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.core.paginator import Paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import *
from .models import *

class Test(View):
    def get(self,request):
        message_data='TheNaings'
        context = {'message_data':message_data}
        return render(request, 'home.html', context)

    def post(self,request):
        t=request.POST.get('test')
        return HttpResponse(t)

#Buyer Section
class BuyerView(View):
    def get(self,request):
        buyer = Buyer.objects.all()
        context ={
            'buyer':buyer
        }
        return render(request, 'buyer_list.html', context)
    def post(self,request):
        buyer_name = request.POST.get('buyer_name')
        vendor_name = request.POST.get('vendor_name')
        address = request.POST.get('address')
        message = None
        if not buyer_name:
            message = 'please enter buyer name'
        elif not address:
            message = 'Please Fill Address'
        if not message:
            b = Buyer(BuyerName=buyer_name,Address=address, Vendor=vendor_name)
            b.save()
            success = 'Buyer Name Created'
            buyer = Buyer.objects.all()
            context = {
                'success':success,
                'message':message,
                'buyer':buyer,
            }
            return render(request, 'buyer_list.html', context)
        else:
            buyer = Buyer.objects.all()
            context = {
                # 'success': success,
                'message': message,
                'buyer': buyer,
            }
            return render(request, 'buyer_list.html', context)

#Style Section
class StyleView(View):
    def get(self,request):
        buyer = Buyer.objects.all()
        style = Style.objects.all()
        context = {
            'style': style,
            'buyer':buyer,
        }
        return render(request, 'style_list.html', context)
    def post(self,request):
        buyer_name = request.POST.get('buyer_name')
        style_code = request.POST.get('style_code')
        item = request.POST.get('item')
        message = None
        if not buyer_name:
            message = 'please enter buyer name'
        elif not style_code:
            message = 'please enter style code'
        elif not item:
            message = 'please fill item'
        if not message:
            v=Buyer.objects.filter(BuyerName=buyer_name)
            vender = v[0].Vendor
            s = Style(Vendor=vender,BuyerName=buyer_name,StyleCode=style_code,ItemName=item)
            s.save()
            success = 'Style Created Successful'
            buyer = Buyer.objects.all()
            style = Style.objects.all()
            context = {
                'message': message,
                'success': success,
                'style': style,
                'buyer': buyer,

            }
            return render(request, 'style_list.html', context)
        else:
            buyer = Buyer.objects.all()
            style = Style.objects.all()
            context = {
                'style': style,
                'buyer': buyer,
                'message':message
            }
            return render(request, 'style_list.html', context)

class ProductionLineView(View):
    def get(self,request):
        line = ProductionLine.objects.all()
        context={'line':line}
        return render(request, 'ProductionLineView.html', context)
    def post(self,request):
        line = request.POST.get('line')
        message = None
        if not line:
            message = 'please enter line name'
        if not message:
            l = ProductionLine(ProductionLine=line)
            l.save()
            success = 'Production Line Created'
            line = ProductionLine.objects.all()
            context = {'success':success,'line':line}
            return render(request, 'ProductionLineView.html', context)
        else:
            line = ProductionLine.objects.all()
            context = {'line': line, 'message':message}
            return render(request, 'ProductionLineView.html', context)

class OrderQtyView(TemplateView):
    template_name = 'orderqty_create.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #     # supplier id get from request url
        style_id = self.kwargs['id']
        # get style info
        style_data = Style.objects.get(id=style_id)
        context['style_data']=style_data

        return context


class SaveOrderQty(View):
    def get(self,request):
        pass
    def post(self,request):
        buyer = request.POST.get('buyer')
        style_code = request.POST.get('style_code')
        item = request.POST.get('item')
        order_date = request.POST.get('order_date')
        order_qty = request.POST.get('order_qty')
        cmp = request.POST.get('cmp_amount')
        making_charge = request.POST.get('making_charge')
        import_export_charge = request.POST.get('import_export_charge')
        box_charge = request.POST.get('box_charge')
        poly_bag = request.POST.get('poly_bag')
        sewing_thread = request.POST.get('sewing_thread')
        delivery = request.POST.get('deli_date')
        fabricETA = request.POST.get('fabric_eta')
        accETA = request.POST.get('acc_eta')
        vendor = request.POST.get('vendor')
        message = None
        print(box_charge)

        if not order_date:
            message = 'select date'
        elif not order_qty:
            message = 'enter order qty'
        elif not cmp:
            message = 'set cmp'
        # elif not making_charge:
        #     making_charge = 0
        # elif not import_export_charge:
        #     import_export_charge = 0
        # elif not box_charge:
        #     box_charge = 0
        # elif not poly_bag:
        #     poly_bag=0
        # elif not sewing_thread:
        #     sewing_thread=0

        if not message:

            cmp_amount = float(cmp)*float(order_qty)
            cmp_condition = int(making_charge) + int(import_export_charge) + int(poly_bag) + int(sewing_thread)+int(box_charge)
            serial_number = buyer + style_code + order_date


            saorder = OrderQty(
                buyer=buyer,
                vendor=vendor,
                style=style_code,
                item=item,
                order_qty=order_qty,
                cmp=cmp,
                cmp_amount=cmp_amount,
                making_charge=making_charge,
                import_export_charge=import_export_charge,
                box_charge=box_charge,
                poly_bag=poly_bag,
                sewing_thread=sewing_thread,
                cmp_condition=cmp_condition,
                delivery =delivery,
                fabricETA = fabricETA,
                accETA=accETA,
                date = order_date,
                serial_number=serial_number
            )
            saorder.save()
            orderqty = OrderQty.objects.all()
            success ='Order Qty Save Successfully'
            context = {
                'success':success,
                'orderqty':orderqty,
            }
            return render(request, 'OrederCMPreportView.html', context)
        else:
            message = 'Please Enter Correct Data'
            context = {'message':message}
            return render(request, 'style_list.html',context)

class OrederCMPreportView(View):
    def get(self,request):
        orderqty = OrderQty.objects.all()
        form = OrderDeliveryForm()
        context={
            'orderqty':orderqty,
            'form':form
        }
        return render(request, 'OrederCMPreportView.html', context)

class ETAView(View):
    def get(self,request):
        orderqty = OrderQty.objects.all()
        # form = OrderETAForm()
        context = {
            'orderqty': orderqty,
            # 'form': form
        }
        return render(request, 'ETAView.html', context)

class OrderQtyDetailView(TemplateView):
    template_name = 'OrderQtyDetailView.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #     # supplier id get from request url
        order_id = self.kwargs['id']
        # get style info
        order_data = OrderQty.objects.get(id=order_id)
        context['order_data']=order_data

        return context

class EditOrderQtyView(View):
    def get(self, request, pk):
        pi = OrderQty.objects.get(id=pk)
        fm = EditOrderQtyForm(instance=pi)
        return render(request, 'EditOrderQtyView.html', {'form': fm})

    def post(self, request, pk):
        pi = OrderQty.objects.get(id=pk)
        fm = EditOrderQtyForm(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            making_charge = request.POST.get('making_charge')
            import_export_charge = request.POST.get('import_export_charge')
            box_charge = request.POST.get('box_charge')
            poly_bag = request.POST.get('poly_bag')
            sewing_thread = request.POST.get('sewing_thread')
            cmp_condition = int(making_charge)+int(import_export_charge)+int(box_charge)+int(poly_bag)+int(sewing_thread)
            c = OrderQty.objects.filter(id=pi.id).update(cmp_condition=cmp_condition)

        return redirect('myapp:OrederCMPreportView')


class ProductionInputView(View):
    def get(self,request):
        line = ProductionLine.objects.all()
        style = Style.objects.all()
        context={'line':line,'style':style}
        return render(request, 'ProductionInput.html', context)

    def post(self,request):
        line = request.POST.get('pline')
        style = request.POST.get('style_code')
        input_qty = request.POST.get('qty')
        message = None
        if not line:
            message = 'line error'
        elif not style:
            message = 'style error'
        elif not input_qty:
            message = 'please enter input qty'
        if not message:
            target = ProductionLine.objects.get(ProductionLine=line)
            dtarget = target.daily_target
            # print(dtarget)
            inputqty = ProductionInput(line=line,style=style,input_qty=input_qty,daily_target=dtarget)
            inputqty.save()
            line = ProductionLine.objects.all()
            style = Style.objects.all()
            pi = ProductionInput.objects.all()
            context = {'line': line, 'style': style,'success':'Success','pi':pi}
            return render(request, 'ProductionInput.html', context)
        else:
            line = ProductionLine.objects.all()
            style = Style.objects.all()
            context = {'line': line, 'style': style,'message':message}
            return render(request, 'ProductionInput.html', context)


class DailyProductionView(View):
    def get(self,request):
        line = ProductionLine.objects.all()
        style = Style.objects.all()
        daily_target_view = DailyProductionOuput.objects.values('line','daily_target').annotate(sum=Sum('daily_target'),stock=Sum('input_qty'), t_total_output_qty=Sum('total_output_qty')).filter(date=datetime.datetime.now())
        context={'line':line,'style':style, 'daily_target_view':daily_target_view}
        return render(request, 'DailyProductionView.html', context)

    def post(self,request):
        pass

class DailyTargetView(View):
    def get(self,request):
        line = ProductionLine.objects.all()
        style = Style.objects.all()
        pro_input = ProductionInput.objects.filter(status=False)
        daily_target_view = DailyProductionOuput.objects.filter(date=datetime.datetime.now())
        context={'line':line,'style':style, 'pro_input':pro_input, 'daily_target_view':daily_target_view}
        return render(request, 'DailyTargetView.html', context)

    def post(self,request):
        line = request.POST.get('line')
        style = request.POST.get('style')
        input_qty = request.POST.get('input_qty')
        target_qty = request.POST.get('target_qty')
        st = OrderQty.objects.filter(style=style)
        a=st[0].cmp

        # target = ProductionLine.objects.get(ProductionLine=line)
        # dtarget = target.daily_target

        tar = DailyProductionOuput(line=line,style=style,input_qty=input_qty,daily_target=target_qty, cmp_amount=a)
        tar.save()
        pro_input = ProductionInput.objects.filter(status=False,line=line).update(daily_target=target_qty)
        return redirect('myapp:DailyTargetView')


def DailyTargetFilterView(request):
    pro_input = ProductionInput.objects.all()
    line = ProductionLine.objects.all()
    li = request.GET.get('pline')
    if li == None:
        line = ProductionLine.objects.all()
        style = Style.objects.all()
        pro_input = ProductionInput.objects.filter(status=False)
        context={'line':line,'style':style, 'pro_input':pro_input}
        return render(request, 'DailyTargetView.html', context)
    else:
        line = ProductionLine.objects.all()
        style = Style.objects.all()
        pro_input = ProductionInput.objects.filter(line=li,status=False)
        context={'line':line,'style':style, 'pro_input':pro_input}
        return render(request, 'DailyTargetView.html', context)


def LineDataEntryView(request):
    pline = request.GET.get('pline')
    po = DailyProductionOuput.objects.filter(line=pline,date=datetime.datetime.now())
    context={'po':po}
    return render(request, 'LineDataEntryView.html', context)

class LineDataEntrySave(View):
    def post(self,request):
        shift_1 = request.POST.get('shift_1')
        shift_2 = request.POST.get('shift_2')
        shift_3 = request.POST.get('shift_3')
        shift_4 = request.POST.get('shift_4')
        shift_5 = request.POST.get('shift_5')
        shift_6 = request.POST.get('shift_6')
        shift_7 = request.POST.get('shift_7')
        shift_8 = request.POST.get('shift_8')
        shift_9 = request.POST.get('shift_9')
        shift_10 = request.POST.get('shift_10')
        shift_11 = request.POST.get('shift_11')
        shift_12 = request.POST.get('shift_12')
        data_id = request.POST.get('id')
        style = request.POST.get('style')
        cmp_amount = request.POST.get('cmp_amount')



        total_shift_data = int(shift_1) + int(shift_2) + int(shift_3) + int(shift_4) + int(shift_5) + int(shift_6) + int(shift_7) + int(shift_8) + int(shift_9) + int(shift_10) + int(shift_11) + int(shift_12)

        acc_total_cmp = int(total_shift_data) * float(cmp_amount)
        # acc_men_cmp = float(acc_total_cmp)/
        # to get menpower
        line_name = DailyProductionOuput.objects.filter(id=data_id)
        l = line_name[0].line
        mp = DailyProductionLineMenPower.objects.filter(line=l,date=datetime.datetime.now())
        op_qty = mp[0].num_operator
        hp_qty = mp[0].num_helper
        total_menpower = int(op_qty)+int(hp_qty)
        acc_men_cmp = float(acc_total_cmp)/int(total_menpower)

        #get production percentage
        # per = total_shift_data

        
        po = DailyProductionOuput.objects.filter(id=data_id).update(
            shift_1=shift_1,
            shift_2=shift_2,
            shift_3=shift_3,
            shift_4=shift_4,
            shift_5=shift_5,
            shift_6=shift_6,
            shift_7=shift_7,
            shift_8=shift_8,
            shift_9=shift_9,
            shift_10=shift_10,
            shift_11=shift_11,
            shift_12=shift_12,
            total_output_qty=total_shift_data,
            acc_total_cmp=acc_total_cmp,
            menpower=total_menpower,
            cmp_pr_menpower = acc_men_cmp
            )

        return redirect(request.META.get('HTTP_REFERER'))

class DashboardView(View):
    def get(self,request):
        daily_target_view = DailyProductionOuput.objects.values('line','daily_target','wok_hr').annotate(sum=Sum('daily_target'),stock=Sum('input_qty'), t_total_output_qty=Sum('total_output_qty'),t_s1=Sum('shift_1'), t_s2=Sum('shift_2'), t_s3=Sum('shift_3'), t_s4=Sum('shift_4'), t_s5=Sum('shift_5'), t_s6=Sum('shift_6'), t_s7=Sum('shift_7'), t_s8=Sum('shift_8'), t_s9=Sum('shift_9'), t_s10=Sum('shift_10'), t_s11=Sum('shift_11'), t_s12=Sum('shift_12')).filter(date=datetime.datetime.now())
        
        context = {'daily_target_view':daily_target_view}
        return render(request, 'DashboardView.html', context)


class DashboardColorView(TemplateView):
    def get(self,request):
        li = ProductionLine.objects.all()
        # print(li[1].ProductionLine)
        line1 = DailyProductionOuput.objects.values('line','daily_target','wok_hr').annotate(sum=Sum('daily_target'),stock=Sum('input_qty'), t_total_output_qty=Sum('total_output_qty'),t_s1=Sum('shift_1'), t_s2=Sum('shift_2'), t_s3=Sum('shift_3'), t_s4=Sum('shift_4'), t_s5=Sum('shift_5'), t_s6=Sum('shift_6'), t_s7=Sum('shift_7'), t_s8=Sum('shift_8'), t_s9=Sum('shift_9'), t_s10=Sum('shift_10'), t_s11=Sum('shift_11'), t_s12=Sum('shift_12')).filter(date=datetime.datetime.now(),line=li[0].ProductionLine)
        line2 = DailyProductionOuput.objects.values('line','daily_target','wok_hr').annotate(sum=Sum('daily_target'),stock=Sum('input_qty'), t_total_output_qty=Sum('total_output_qty'),t_s1=Sum('shift_1'), t_s2=Sum('shift_2'), t_s3=Sum('shift_3'), t_s4=Sum('shift_4'), t_s5=Sum('shift_5'), t_s6=Sum('shift_6'), t_s7=Sum('shift_7'), t_s8=Sum('shift_8'), t_s9=Sum('shift_9'), t_s10=Sum('shift_10'), t_s11=Sum('shift_11'), t_s12=Sum('shift_12')).filter(date=datetime.datetime.now(),line=li[1].ProductionLine)
        line3 = DailyProductionOuput.objects.values('line','daily_target','wok_hr').annotate(sum=Sum('daily_target'),stock=Sum('input_qty'), t_total_output_qty=Sum('total_output_qty'),t_s1=Sum('shift_1'), t_s2=Sum('shift_2'), t_s3=Sum('shift_3'), t_s4=Sum('shift_4'), t_s5=Sum('shift_5'), t_s6=Sum('shift_6'), t_s7=Sum('shift_7'), t_s8=Sum('shift_8'), t_s9=Sum('shift_9'), t_s10=Sum('shift_10'), t_s11=Sum('shift_11'), t_s12=Sum('shift_12')).filter(date=datetime.datetime.now(),line=li[2].ProductionLine)
        line4 = DailyProductionOuput.objects.values('line','daily_target','wok_hr').annotate(sum=Sum('daily_target'),stock=Sum('input_qty'), t_total_output_qty=Sum('total_output_qty'),t_s1=Sum('shift_1'), t_s2=Sum('shift_2'), t_s3=Sum('shift_3'), t_s4=Sum('shift_4'), t_s5=Sum('shift_5'), t_s6=Sum('shift_6'), t_s7=Sum('shift_7'), t_s8=Sum('shift_8'), t_s9=Sum('shift_9'), t_s10=Sum('shift_10'), t_s11=Sum('shift_11'), t_s12=Sum('shift_12')).filter(date=datetime.datetime.now(),line=li[3].ProductionLine)
        line5 = DailyProductionOuput.objects.values('line','daily_target','wok_hr').annotate(sum=Sum('daily_target'),stock=Sum('input_qty'), t_total_output_qty=Sum('total_output_qty'),t_s1=Sum('shift_1'), t_s2=Sum('shift_2'), t_s3=Sum('shift_3'), t_s4=Sum('shift_4'), t_s5=Sum('shift_5'), t_s6=Sum('shift_6'), t_s7=Sum('shift_7'), t_s8=Sum('shift_8'), t_s9=Sum('shift_9'), t_s10=Sum('shift_10'), t_s11=Sum('shift_11'), t_s12=Sum('shift_12')).filter(date=datetime.datetime.now(),line=li[4].ProductionLine)
        line6 = DailyProductionOuput.objects.values('line','daily_target','wok_hr').annotate(sum=Sum('daily_target'),stock=Sum('input_qty'), t_total_output_qty=Sum('total_output_qty'),t_s1=Sum('shift_1'), t_s2=Sum('shift_2'), t_s3=Sum('shift_3'), t_s4=Sum('shift_4'), t_s5=Sum('shift_5'), t_s6=Sum('shift_6'), t_s7=Sum('shift_7'), t_s8=Sum('shift_8'), t_s9=Sum('shift_9'), t_s10=Sum('shift_10'), t_s11=Sum('shift_11'), t_s12=Sum('shift_12')).filter(date=datetime.datetime.now(),line=li[5].ProductionLine)
        

        context = {'line1':line1,'line2':line2,'line3':line3,'line4':line4,'line5':line5,'line6':line6}
        return render(request, 'DashboardColorView.html', context)
    # template_name = 'DashboardColorView.html'



class ProductionLineOutputDetail(View):
    def get(self,request):
        pline = request.GET.get('pline')
        daily_rank = DailyProductionOuput.objects.values('line').annotate(sum=Sum('daily_target'),t_total_output_qty=Sum('total_output_qty')).filter(date=datetime.datetime.now())
        daily_style = DailyProductionOuput.objects.values('style').filter(date=datetime.datetime.now(), line=pline)
        work_hr = DailyProductionOuput.objects.filter(date=datetime.datetime.now(), line=pline)
        wh = work_hr[0].wok_hr
        dt = work_hr[0].daily_target
        a = int(dt)/int(wh)
        shift = int(a)

        li = ProductionLine.objects.all()

        daily_target_view = DailyProductionOuput.objects.values('line').annotate(sum=Sum('daily_target'),stock=Sum('input_qty'),t_s1=Sum('shift_1'), t_s2=Sum('shift_2'), t_s3=Sum('shift_3'), t_s4=Sum('shift_4'), t_s5=Sum('shift_5'), t_s6=Sum('shift_6'), t_s7=Sum('shift_7'), t_s8=Sum('shift_8'), t_s9=Sum('shift_9'), t_s10=Sum('shift_10'), t_s11=Sum('shift_11'), t_s12=Sum('shift_12'),t_total_output_qty=Sum('total_output_qty')).filter(date=datetime.datetime.now(), line=pline)
        line1 = DailyProductionOuput.objects.values('line', 'daily_target').annotate(sum=Sum('daily_target'), t_total_output_qty=Sum('total_output_qty')).filter(date=datetime.datetime.now(),line=li[0].ProductionLine)
        line2 = DailyProductionOuput.objects.values('line', 'daily_target').annotate(sum=Sum('daily_target'),
                                                                                     t_total_output_qty=Sum(
                                                                                         'total_output_qty')).filter(
            date=datetime.datetime.now(), line=li[1].ProductionLine)
        line3 = DailyProductionOuput.objects.values('line', 'daily_target').annotate(sum=Sum('daily_target'),
                                                                                     t_total_output_qty=Sum(
                                                                                         'total_output_qty')).filter(
            date=datetime.datetime.now(), line=li[2].ProductionLine)
        line4 = DailyProductionOuput.objects.values('line', 'daily_target').annotate(sum=Sum('daily_target'),
                                                                                     t_total_output_qty=Sum(
                                                                                         'total_output_qty')).filter(
            date=datetime.datetime.now(), line=li[3].ProductionLine)
        line5 = DailyProductionOuput.objects.values('line', 'daily_target').annotate(sum=Sum('daily_target'),
                                                                                     t_total_output_qty=Sum(
                                                                                         'total_output_qty')).filter(
            date=datetime.datetime.now(), line=li[4].ProductionLine)
        line6 = DailyProductionOuput.objects.values('line', 'daily_target').annotate(sum=Sum('daily_target'),
                                                                                     t_total_output_qty=Sum(
                                                                                         'total_output_qty')).filter(
            date=datetime.datetime.now(), line=li[5].ProductionLine)


        context = {'daily_target_view':daily_target_view, 'daily_style':daily_style, 'shift':shift, 'pline':pline, 'dt':dt, 'daily_rank':daily_rank,'line1':line1,'line2':line2,'line3':line3,'line4':line4,'line5':line5,'line6':line6}
        return render(request, 'ProductionLineOutputDetail.html', context)
    # template_name = 'ProductionLineOutputDetail.html'
    
class DailyAttendanceView(View):
    def get(self,request):
        data = DailyProductionLineMenPower.objects.filter(date=datetime.datetime.now())
        line = ProductionLine.objects.all()
        context = {'data':data,'line':line}
        return render(request, 'DailyAttendanceView.html', context)

    def post(self,request):
        pline = request.POST.get('pline')
        op = request.POST.get('op')
        hp = request.POST.get('hp')
        mp = DailyProductionLineMenPower(line=pline,num_operator=op,num_helper=hp)
        mp.save()
        return redirect('myapp:DailyAttendanceView')


# ======== AccInventoyForm ============
class AccInventoyList(View):
    def get(self,request):
        acc = AccInventoy.objects.all()
        context = {'acc': acc,}
        return render(request, 'AccInventoyList.html', context)

class ProductInline():
    form_class = AccInventoyForm
    model = AccInventoy
    template_name = "acc_create_or_update.html"

    def form_valid(self, form):
        named_formsets = self.get_named_formsets()
        if not all((x.is_valid() for x in named_formsets.values())):
            return self.render_to_response(self.get_context_data(form=form))

        self.object = form.save()

        # for every formset, attempt to find a specific formset save function
        # otherwise, just save.
        for name, formset in named_formsets.items():
            formset_save_func = getattr(self, 'formset_{0}_valid'.format(name), None)
            if formset_save_func is not None:
                formset_save_func(formset)
            else:
                formset.save()
        return redirect('myapp:AccInventoyList')

    def formset_variants_valid(self, formset):
        """
        Hook for custom formset saving.. useful if you have multiple formsets
        """
        variants = formset.save(commit=False)  # self.save_formset(formset, contact)
        # add this, if you have can_delete=True parameter set in inlineformset_factory func
        for obj in formset.deleted_objects:
            obj.delete()
        for variant in variants:
            variant.accinv = self.object
            variant.save()

    def formset_images_valid(self, formset):
        """
        Hook for custom formset saving.. useful if you have multiple formsets
        """
        images = formset.save(commit=False)  # self.save_formset(formset, contact)
        # add this, if you have can_delete=True parameter set in inlineformset_factory func
        for obj in formset.deleted_objects:
            obj.delete()
        for image in images:
            image.accinv = self.object
            image.save()


class ProductCreate(ProductInline, CreateView):

    def get_context_data(self, **kwargs):
        ctx = super(ProductCreate, self).get_context_data(**kwargs)
        ctx['named_formsets'] = self.get_named_formsets()
        return ctx

    def get_named_formsets(self):
        if self.request.method == "GET":
            return {
                'variants': VariantFormSet(prefix='variants'),
                'images': ImageFormSet(prefix='images'),
            }
        else:
            return {
                'variants': VariantFormSet(self.request.POST or None, self.request.FILES or None, prefix='variants'),
                'images': ImageFormSet(self.request.POST or None, self.request.FILES or None, prefix='images'),
            }

class ProductUpdate(ProductInline, UpdateView):

    def get_context_data(self, **kwargs):
        ctx = super(ProductUpdate, self).get_context_data(**kwargs)
        ctx['named_formsets'] = self.get_named_formsets()
        return ctx

    def get_named_formsets(self):
        return {
            'variants': VariantFormSet(self.request.POST or None, self.request.FILES or None, instance=self.object, prefix='variants'),
            'images': ImageFormSet(self.request.POST or None, self.request.FILES or None, instance=self.object, prefix='images'),
        }



def delete_image(request, pk):
    try:
        image = AccImage.objects.get(id=pk)
    except AccImage.DoesNotExist:
        messages.success(
            request, 'Object Does not exit'
            )
        return redirect('myapp:update_product', pk=image.accinv.id)

    image.delete()
    messages.success(
            request, 'Image deleted successfully'
            )
    return redirect('myapp:update_product', pk=image.accinv.id)


def delete_variant(request, pk):
    try:
        variant = AccVariant.objects.get(id=pk)
    except AccVariant.DoesNotExist:
        messages.success(
            request, 'Object Does not exit'
            )
        return redirect('myapp:update_product', pk=variant.accinv.id)

    variant.delete()
    messages.success(
            request, 'Variant deleted successfully'
            )
    return redirect('myapp:update_product', pk=variant.accinv.id)


class AccVarientList(View):
    def get(self,request):
        acc = AccVariant.objects.all()
        accreq = AccessoriesRequestToWh.objects.filter(request_by=request.user)
        context = {'acc': acc,'accreq':accreq}
        return render(request, 'acc_varient_list.html', context)

    def post(self,request):
        style_po_id = request.POST.get('style_po_id')
        style_po = request.POST.get('style_po')
        size = request.POST.get('size')
        request_qty = request.POST.get('request_qty')
        status='requested'
        accreq = AccessoriesRequestToWh(
            style_po_id=style_po_id,
            style_po=style_po,
            size=size,
            request_status=status,
            request_qty=request_qty,
            status=status,
            request_date=datetime.datetime.now(),
            request_by=request.user,
        )
        accreq.save()
        return redirect('myapp:AccVarientList')


class WarehouseMgrView(View):
    def get(self,request):
        acc = AccVariant.objects.all()
        accreq = AccessoriesRequestToWh.objects.filter(request_status='requested')
        approved_req = AccessoriesRequestToWh.objects.filter(request_status='approved')

        context = {'acc': acc, 'accreq': accreq, 'approved_req':approved_req}
        return render(request, 'WarehouseMgrView.html', context)


class AccRequestStatusChange(View):
    def get(self,request,pk):
        status = AccessoriesRequestToWh.objects.get(id=pk)
        status.request_status='approved'

        status.save()
        return redirect('myapp:WarehouseMgrView')


class WH_to_Production_Acc(View):
    def get(self,request):
        AccV = AccVariant.objects.all()
        approved_req = AccessoriesRequestToWh.objects.filter(request_status='approved')
        wh_to_pro = WarehouseToProductionHistory.objects.all()
        context={'AccV':AccV,'approved_req':approved_req,'wh_to_pro':wh_to_pro}
        return render(request, 'WH_to_Production_Acc.html',context)

    def post(self,request):
        style_po_id = request.POST.get('style_po_id')
        style_po = request.POST.get('style_po')
        size = request.POST.get('size')
        request_qty = request.POST.get('request_qty')
        request_by= request.POST.get('request_by')
        request_line= request.POST.get('request_line')
        handover_quantity = request.POST.get('handover_quantity')
        operator = request.POST.get('operator')
        remark = request.POST.get('remark')
        r_id = request.POST.get('r_id')

        get_id = AccVariant.objects.get(id=style_po_id)
        get_acc_qty = get_id.quantity
        balance = int(get_acc_qty)-int(handover_quantity)
        acc_update = AccVariant.objects.filter(id=style_po_id).update(quantity=balance)
        rid = AccessoriesRequestToWh.objects.filter(id = r_id).update(request_status='completed')
        his = WarehouseToProductionHistory(
            style_po_id=style_po_id,
            style_po=style_po,
            size=size,
            request_qty=request_qty,
            request_by=request_by,
            request_line=request_line,
            handover_quantity=handover_quantity,
            operator=operator,
            handover_by=request.user,
            remark = remark,

        )
        his.save()
        return redirect('myapp:WH_to_Production_Acc')



#Fabric Inventory start
class FabricInvoiceList(View):
    def get(self,request):
        fab_inv = FabricInventoy.objects.all()
        fab_compo = FabricComposition.objects.all()
        context = {'fab_inv':fab_inv, 'fab_compo':fab_compo}
        return render(request,'FabricInvoiceList.html', context)

class FabricRequesttoWH(View):
    def get(self, request):
        fab_compo = FabricComposition.objects.all()
        context = {'fab_compo':fab_compo}
        return render(request,'FabricRequesttoWH.html', context)


class FabricProductInline():
    form_class = FabricInventoyForm
    model = FabricInventoy
    template_name = "fabric_create_or_update.html"

    def form_valid(self, form):
        named_formsets = self.get_named_formsets()
        if not all((x.is_valid() for x in named_formsets.values())):
            return self.render_to_response(self.get_context_data(form=form))

        self.object = form.save()

        # for every formset, attempt to find a specific formset save function
        # otherwise, just save.
        for name, formset in named_formsets.items():
            formset_save_func = getattr(self, 'formset_{0}_valid'.format(name), None)
            if formset_save_func is not None:
                formset_save_func(formset)
            else:
                formset.save()
        return redirect('myapp:FabricInvoiceList')

    def formset_variants_valid(self, formset):
        """
        Hook for custom formset saving.. useful if you have multiple formsets
        """
        variants = formset.save(commit=False)  # self.save_formset(formset, contact)
        # add this, if you have can_delete=True parameter set in inlineformset_factory func
        for obj in formset.deleted_objects:
            obj.delete()
        for variant in variants:
            variant.accinv = self.object
            variant.save()

    def formset_images_valid(self, formset):
        """
        Hook for custom formset saving.. useful if you have multiple formsets
        """
        images = formset.save(commit=False)  # self.save_formset(formset, contact)
        # add this, if you have can_delete=True parameter set in inlineformset_factory func
        for obj in formset.deleted_objects:
            obj.delete()
        for image in images:
            image.accinv = self.object
            image.save()


class FabricProductCreate(FabricProductInline, CreateView):

    def get_context_data(self, **kwargs):
        ctx = super(FabricProductCreate, self).get_context_data(**kwargs)
        ctx['named_formsets'] = self.get_named_formsets()
        return ctx

    def get_named_formsets(self):
        if self.request.method == "GET":
            return {
                'variants': FabricCompositionFormSet(prefix='variants'),
                'images': FabricImageFormSet(prefix='images'),
            }
        else:
            return {
                'variants': FabricCompositionFormSet(self.request.POST or None, self.request.FILES or None, prefix='variants'),
                'images': FabricImageFormSet(self.request.POST or None, self.request.FILES or None, prefix='images'),
            }

class FabricProductUpdate(FabricProductInline, UpdateView):

    def get_context_data(self, **kwargs):
        ctx = super(FabricProductUpdate, self).get_context_data(**kwargs)
        ctx['named_formsets'] = self.get_named_formsets()
        return ctx

    def get_named_formsets(self):
        return {
            'variants': FabricCompositionFormSet(self.request.POST or None, self.request.FILES or None, instance=self.object, prefix='variants'),
            'images': FabricImageFormSet(self.request.POST or None, self.request.FILES or None, instance=self.object, prefix='images'),
        }



def delete_fabric_image(request, pk):
    try:
        image = FabricImage.objects.get(id=pk)
    except FabricImage.DoesNotExist:
        messages.success(
            request, 'Object Does not exit'
            )
        return redirect('myapp:update_fabric', pk=image.accinv.id)

    image.delete()
    messages.success(
            request, 'Image deleted successfully'
            )
    return redirect('myapp:update_fabric', pk=image.accinv.id)


def delete_fabric(request, pk):
    try:
        variant = FabricComposition.objects.get(id=pk)
    except FabricComposition.DoesNotExist:
        messages.success(
            request, 'Object Does not exit'
            )
        return redirect('myapp:update_fabric', pk=variant.accinv.id)

    variant.delete()
    messages.success(
            request, 'Variant deleted successfully'
            )
    return redirect('myapp:update_fabric', pk=variant.accinv.id)
