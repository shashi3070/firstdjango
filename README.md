Edit following file

1.	C:\Users\A1507\AppData\Local\Continuum\anaconda3\Lib\site-packages\django\contrib\admin\options.py

	def _response_post_save(self, request, obj):
	        opts = self.model._meta
	        if self.has_view_or_change_permission(request):
	            post_url = reverse('admin:%s_%s_changelist' %
	                               (opts.app_label, opts.model_name),
	                               current_app=self.admin_site.name)
	            preserved_filters = self.get_preserved_filters(request)
	            post_url = add_preserved_filters({'preserved_filters': preserved_filters, 'opts': opts}, post_url)
	        else:
	            post_url = reverse('admin:index',
	                               current_app=self.admin_site.name)
	        #return HttpResponseRedirect(post_url)
	        
	        if 'pythonjobinformations' in str(request):
	            return HttpResponseRedirect('/pythonjob/')
	        elif 'talendjobinformations' in str(request):
	            return HttpResponseRedirect('/Talendjob/')
	        elif 'matillionjobinformation' in str(request):
	            return HttpResponseRedirect('/matillionjobs/')
	        elif 'customjobinformations' in str(request):
	            return HttpResponseRedirect('/CustomJobSee/')
	        else:
	            print(str(request))
	            return HttpResponseRedirect('/')


2. 	


