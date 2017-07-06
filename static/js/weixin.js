$(function(){
var sharedata = {};
sharedata.title = window.wxshare_title;
sharedata.desc = window.wxshare_desc;
sharedata.link =window.wxshare_link;
sharedata.imgUrl =window.wxshare_imgUrl;
sharedata.hideOptionMenu = window.wxshare_hideOptionMenu;
sharedata.debug = window.wxshare_debug;
wx.config({
                debug: sharedata.debug, // 开启调试模式,调用的所有api的返回值会在客户端alert出来，若要查看传入的参数，可以在pc端打开，参数信息会通过log打出，仅在pc端时才会打印。
                appId: "wx6924e47808faa535", // 必填，公众号的唯一标识
                timestamp: "1495425353", // 必填，生成签名的时间戳
                nonceStr: "18915459", // 必填，生成签名的随机串
                signature: "699d47f811677e05fc0900d65f5cef41e6866c5e",// 必填，签名，见附录1
                jsApiList: ["onMenuShareTimeline", "onMenuShareAppMessage", "onMenuShareQQ", "onMenuShareWeibo", "hideOptionMenu","scanQRCode"] // 必填，需要使用的JS接口列表，所有JS接口列表见附录2
            });    
     wx.ready(function () {
        //分享到朋友圈
        wx.onMenuShareTimeline({
            title: sharedata.title, // 分享标题
            link: sharedata.link, // 分享链接
            imgUrl: sharedata.imgUrl//, // 分享图标
           // success: successcall
        });
        //分享给朋友
        wx.onMenuShareAppMessage({
            title: sharedata.title, // 分享标题
            desc: sharedata.desc, // 分享描述
            link: sharedata.link, // 分享链接
            imgUrl: sharedata.imgUrl, // 分享图标
            type: sharedata.type, // 分享类型,music、video或link，不填默认为link
            dataUrl: sharedata.dataUrl//, // 如果type是music或video，则要提供数据链接，默认为空
          //  success: successcall
        });
        wx.onMenuShareQQ({
            title: sharedata.title, // 分享标题
            desc: sharedata.desc, // 分享描述
            link: sharedata.link, // 分享链接
            imgUrl: sharedata.imgUrl//, // 分享图标
          //  success: successcall
        });
        wx.onMenuShareWeibo({
            title: sharedata.title, // 分享标题
            desc: sharedata.desc, // 分享描述
            link: sharedata.link, // 分享链接
            imgUrl: sharedata.imgUrl//, // 分享图标
          //  success: successcall
        });
        if (sharedata.hideOptionMenu) {
            wx.hideOptionMenu();
        }else {
            wx.showOptionMenu();
        }

    });
});