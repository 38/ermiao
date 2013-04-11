function checkarg(field, value,e){
	e.ret.html("checking...");
	request = $.ajax({
		url: "/checkarg",
		type: "post",
		data: "field=" + field + "&" + "value=" + value,
		success: function(data){
			e.ret.html(e.info[data]);
		}
	});
}
$(document).ready(function(){
	fields = [
				{
					name:'nickname', 
			    	info: ["ok","用户已被注册"],
					handler: function(e){
						checkarg("nickname",$("#nickname").val(),e);
					}
				} , 
				{
					name:'email',
					info: ["ok", "Email已被注册","<a href='http://www.gravatar.com'>去Gravatar设置头像</a>"],
					handler: function(e){
						checkarg("email",$("#email").val(),e);
					}
				} ,
				{
					name: 'password',
					info: ["ok", "密码长度小于6"],
					handler: function(e){
						if($("#password").val().length < 6) e.ret.html(e.info[1]);
						else e.ret.html(e.info[0]);
					}
				} ,
				{
					name: 'confirmpwd',
					info: ["ok", "两次输入的密码不相符"],
					handler: function(e){
						if($("#confirmpwd").val() != $("#password").val()) e.ret.html(e.info[1]);
						else e.ret.html(e.info[0]);
					}
				}
	];
	eventfunction = function(i){
		return (function(){
				obj = fields[i];
				e = { 
					ret : $("#" + obj.name + "_info"),
			   		info : obj.info
				};
				obj.handler(e);
		});
	}
	for(var i in fields){
		$("#" + fields[i].name).change(eventfunction(i));
	}
	$("#reg").bind('submit', function(e){
		if($("#nickname_info").html() != 'ok') return false;
		if($("#email_info").html() != 'ok') return false;
		if($("#password_info").html() != 'ok') return false;
		if($("#confirmpwd_info").html() != 'ok') return false;
		pwd = $("#password");
		confirmpwd = $("#confirmpwd");
		confirmpwd.val("");
		pwd.val(MD5(pwd.val()));
		$(this).submit();
		return 0;
	});
});
