$(document).ready(function() {
	$(".Line").click(function() {
		$(".bottom-nav").toggle();
		$(".tan1").toggle();
	});
	$(".tiaozhuan1,.tiaozhuan2,.tiaozhuan3").click(function() {
		$(".bottom-nav").hide();
		$(".tan1").hide();
	});
	// $(".bottom-nav").stop().fadeIn();

	// $(".bottom-nav").stop().fadeOut(); 

	$(".bottom-nav").hover(function() {
		// $(".bottom-nav").stop().fadeIn();
		$(".bottom-nav").show();
		$(".tan1").show();
	}, function() {
		// $(".bottom-nav").stop().fadeOut(); 
		$(".bottom-nav").hide();
		$(".tan1").hide();
	});
	$(".tiaozhuanpc").click(function() {
		$(this).find("a").addClass("moren");
		$(this).siblings("li").find("a").removeClass("moren")
	});
	$(".tiaozhuanpc1").click(function() {
		$("#tiaozhuan1").addClass("tiaozhuan");
		$("#tiaozhuan2").removeClass("tiaozhuan");
		$("#tiaozhuan3").removeClass("tiaozhuan");
		$(this).find("a").addClass("moren");
		$(this).siblings("li").find("a").removeClass("moren");

	});
	$(".tiaozhuanpc2").click(function() {
		$("#tiaozhuan2").addClass("tiaozhuan");
		$("#tiaozhuan1").removeClass("tiaozhuan");
		$("#tiaozhuan3").removeClass("tiaozhuan");
		$(this).find("a").addClass("moren");
		$(this).siblings("li").find("a").removeClass("moren");
	});
	$(".tiaozhuanpc3").click(function() {
		$("#tiaozhuan3").addClass("tiaozhuan");
		$("#tiaozhuan2").removeClass("tiaozhuan");
		$("#tiaozhuan1").removeClass("tiaozhuan");
		$(this).find("a").addClass("moren");
		$(this).siblings("li").find("a").removeClass("moren");
	});

	$(".tiaozhuan1").click(function() {
		$("#tiaozhuan1").addClass("tiaozhuan");
		$("#tiaozhuan2").removeClass("tiaozhuan");
		$("#tiaozhuan3").removeClass("tiaozhuan");

	});
	$(".tiaozhuan2").click(function() {
		$("#tiaozhuan2").addClass("tiaozhuan");
		$("#tiaozhuan1").removeClass("tiaozhuan");
		$("#tiaozhuan3").removeClass("tiaozhuan");

	});
	$(".tiaozhuan3").click(function() {
		$("#tiaozhuan3").addClass("tiaozhuan");
		$("#tiaozhuan2").removeClass("tiaozhuan");
		$("#tiaozhuan1").removeClass("tiaozhuan");

	});
})