		
function GetData(){
			$.ajax(
				    {
				        type:"GET",
				        url: "/GetHistoryLogs/",
				        

				        dataType: 'json',

				        success: function( data ) 
					        {
					            
					            
					            var trHTML=''
					           	console.log(data['history_data'])
					            li=data['history_data']
					           	for(i=0;i<li.length;i++){
					           		//console.log(li[i].JobID)
					           		trHTML += '<tr><td>' + li[i].JobType + '</td><td>' + li[i].JobName + '</td><td>' + li[i].StartTime + '</td><td>' + li[i].EndTime + '</td><td>' + li[i].Sche_or_Manu + '</td><td>'+li[i].Status+'</td><td>'+li[i].description+'</td></tr>'
					           	}
					            $(".MainContent").empty();
					            $('.MainContent').append(trHTML);
					            
					             $('#table_id').DataTable({
					             	
										columnDefs: [
										{targets: 5,render: $.fn.dataTable.render.ellipsis(20) },
										{targets: 6,render: $.fn.dataTable.render.ellipsis(50) },
										{targets: 1,render: $.fn.dataTable.render.ellipsis(25) },										
				                    ],
				                    "rowCallback": function( row, data,index ) {
					                    	console.log('in rowCallback')
					                    	console.log(data[0])
										    if ( data[0] == "CustomJobs" ) {
										      $('td', row).css('background-color', '#A9A9A9');
										    }
										    else if ( data[0] == "TalendJobs" ) {
										      $('td', row).css('background-color', '#C0C0C0');
										    }
										    else if ( data[0] == "PythonJobs" ) {
										      $('td', row).css('background-color', '#D8D8D8');
										    }
										     else{

										    	 $('td', row).css('background-color', '#F5F5F5');
										    }
									  },

									  "order": [[ 2, 'desc' ]],

					             });

					             $('#table_id').css({"visibility":"visible"})
					             $('#loadingiconid').css({"display":"none"})


								

					        }
		    	 });
}



