function on_image_file_selected() {
	  if(this.files[0].size > 1024*1024){
		alert("不支持大于1M的图片");
		return true;
	  }
	  var id_container = $('#id_img_id');
	  var prev_container = $('#preview');
	  upload_preview_image($('#image_form'), id_container);
	  $("#image_form input[type=file]").change(on_image_file_selected); // rebind the event
	  id_container.val('uploading');
	  prev_container.html("正在加载图片...");
	  setTimeout(function prev_poll(){
		  if(id_container.val() != 'uploading'){
			show_preview_image(prev_container,id_container.val());
		  }
		  else setTimeout(prev_poll,500);
		  },0);
	  return true;
}
function upload_preview_image(form, ret){
	request = $.ajaxFileUpload({
		url: '/upload_preview',
		secureuri: false,
		fileElementId: 'image_filename',
		dataType: 'json',
		success: function(data, status){
			if(0 == data.return){
				ret.val(data.id);
			} else{
				ret.val('failed');
			}
		}
	});
}
_date = new Date();
function rotate_image(dir,id){

	$.ajax({
		url:  "/rotate",
		type: "post",
		data: "id=" + id + "&dir=" + dir,
		success: function(){
			$(".img_previewer").attr('src', '/showimg?id=' + id + '&t=' + _date.getTime());
		}
	});
}
function show_preview_image(container, id){
	if(id == 'failed')
		container.html("图片加载失败");
	else
	{
		var html = "<div>";
		html += "<img class=\"img_previewer\" src=/showimg?id=" + id + "></img><br/>";
		html += "<a href=\"javascript:void(0);\" onclick=\"rotate_image(1,\'"+id+"\');\">左转90度</a>";
		html += "<a href=\"javascript:void(0);\" onclick=\"rotate_image(-1,\'"+id+"\');\" style='verticle-'>右转90度</a>";
		html += "</div>";

		container.html(html);
	}
}
