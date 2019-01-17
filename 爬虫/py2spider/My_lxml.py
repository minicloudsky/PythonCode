#coding: utf-8
# 获取所有 <li>
from lxml import etree
html = """
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="zh" lang="zh">
<head>
<title>中国大学MOOC(慕课)_最好的在线课程学习平台</title>
<meta http-equiv="content-type" content="text/html;charset=utf-8"/>
<link rel="shortcut icon" href="//nos.netease.com/edu-image/32a8dd2a-b9aa-4ec9-abd5-66cd8751befb.png?imageView&quality=100" />
<meta http-equiv="x-dns-prefetch-control" content="on"/>
<link rel="dns-prefetch" href="//s.stu.126.net"/>
<link rel="dns-prefetch" href="//icourse163.org/"/>
<link rel="dns-prefetch" href="//mc.stu.126.net"/>
<link rel="dns-prefetch" href="//mooc.study.163.com"/>
<link rel="dns-prefetch" href="//ursdoccdn.nosdn.127.net/"/>
<link rel="dns-prefetch" href="//nos.netease.com"/>
<link rel="dns-prefetch" href="//imgsize.ph.126.net"/>
<link rel="dns-prefetch" href="//img0.ph.126.net"/>
<link rel="dns-prefetch" href="//img1.ph.126.net"/>
<link rel="dns-prefetch" href="//img2.ph.126.net"/>
<link rel="dns-prefetch" href="//push.zhanzhang.baidu.com"/>
<link rel="dns-prefetch" href="//api.share.baidu.com"/>
<link rel="dns-prefetch" href="//js.passport.qihucdn.com"/>
<link rel="dns-prefetch" href="//s2.qhimg.com"/>
<meta http-equiv="Pragma" content="no-cache"/>
<meta http-equiv="Cache-Control" content="no-cache" max-age="0"/>
<meta http-equiv="X-UA-Compatible" content="IE=edge" />
<meta http-equiv="Expires" content="0"/>
<meta name="author" content="Netease"/>
<meta name="version" content="1.0"/>
<meta name="keywords" content="中国大学MOOC,MOOC,慕课,在线学习,在线教育,大规模开放式在线课程,网络公开课,视频公开课,大学公开课,大学mooc, icourse163,慕课网, MOOC学院"/>
<meta name="description" content="中国大学MOOC(慕课) 是爱课程网携手云课堂打造的在线学习平台，每一个有提升愿望的人，都可以在这里学习中国最好的大学课程，学完还能获得认证证书。中国大学MOOC是国内最好的中文MOOC学习平台，拥有来自于众多985高校的顶级课程，最好最全的大学课程，与名师零距离。"/>
<meta property="wb:webmaster" content="981d7778ffe598a6" />
<meta name="360-site-verification" content="92d0cfcc97ca254f26fcc0586fa319b6" />
<meta name="sogou_site_verification" content="kFeGWcT6tD"/>
<meta property="qc:admins" content="2206160020613752351636727736372561577477166045" />
<meta name="shenma-site-verification" content="8ef752d11066ef909303c078d32230d6_1456214698">
<script>location.config = {root:'/pub/h/web/',ver:{"about/contactus.html":"1d98e1ed4a41caf8791907a98dbcb005","center/accountSetting.html":"ec7b7c427dff12f27984df7950f391f5","center/mailSetting.html":"1bc29b6f43d979e430f62f8b7194372a","center/personInfoSetting.html":"d758a11c5b7a516bd8c9c9edc3ed4914","center/teacherCenter.html":"ecb0c756fc13432b89de054c17283a04","center/teacherCenterEdit.html":"c91f7e7ed6cf8a7644c3589373c830ca","center/teacherInfoEdit.html":"68d680fba71ad4ce20ce4a272d6dce22","center/universityCenter.html":"a29f471b212d0d728907d166f325eaac","cert/apply.html":"da287e6476933e56f2f23331c071a83b","cert/certDesign.html":"b76a7b43c025460449c5c7886b6b7d93","cert/verify.html":"c7b702f8fb653f69832438dc05562c0b","common/commonutil.html":"ac20166566f5204608422782b0627716","course/courseList.html":"f70ea351ba4cef4788762f2c0b973523","course/info.html":"ebe87d7beb70c0ce481e92143cfc4a60","error/error.html":"c6f254b39b7d0995984f29b51c9b00aa","help/helpBack.html":"2aa4f74c722ecffc74c17150d100e2bc","help/helpFront.html":"b53e33413f642855db3fe0436e68de1d","home/course.html":"c4659957c75551e98f1847f12c9005ed","home/discuss.html":"3dd62173064eca830af47c5a3917b699","home/index.html":"9e10d4b4010004a92d6b6148a8d0ed8c","home/mycert.html":"afda1fd483f4b9a4b96f662d15cf4880","home/selfIntro.html":"02de98e1f1157de702697e2bf3d8aa21","index.html":"3568143da61f69033810f1752df1d345","live/index.html":"3fef1b8b6d1400c6ea53d5f06bc3c061","member/addMember.html":"ffb5584c5a23725d7bb24e17783bad03","member/icourseLogin.html":"b858e087ce8e8c68ce127c3ca4c20c78","member/login.html":"e94c8e329ffa11d80b2065ef36545a9f","member/ursLogin.html":"2cbe80197a602e5ee23139c6870eb6ed","module-live/src/component/live-manage-balance/component.html":"25a61449b1adc8b0e5e39696716e1eaf","module-live/src/component/live-manage-config/component.html":"34115e39a2bb96a711a1255f0dc501a9","module-live/src/component/live-manage-list/component.html":"ef322e91c61a0236990a2245c981c0d2","module-live/src/component/live-manage-list/obsStartDialogTpl.html":"fbede6a4db8ad8af2db37878f1137da5","module-live/src/component/live-mobile-chat/component.html":"3b65499c43e72f29c42e732db11cfc01","module-live/src/component/live-mobile-player/component.html":"37ceef60535336bec734a936dd34f3f4","module-live/src/component/live-pc-chat/component.html":"14fc99ba5984f5c6be85787d4b54cefb","module-live/src/component/live-pc-player/component.html":"b681fb26a64b2d9f1d69810213e41491","module-live/src/live-manage/index.html":"a503f6871a07aa5f305adb11a25adfc4","module-live/src/live-mobile/index.html":"f7843e27e662394e7d7edd392ec4c94f","module-live/src/live-pc/index.html":"ea7406dae3a2233530e4fb3d1178b0da","module-live-room/src/component/room-list-view/component.html":"d4f2bdc58c7f462a85c15f2631cfa9aa","module-live-room/src/live-room/index.html":"48b9b8861926c651516a175e4cf4a2d1","order/payOrder.html":"d8a0d39b855328ef3c11efdd98236a16","pay/donateCourse.html":"ba1119589c9d10b58c69501f3d384a3d","pay/order.html":"28d370f01514656e15b6da1e95718481","spoc/center/teacherCenter.html":"2ec7d2e185d7ed01b90a3523ae647d4c","spoc/center/universityCenter.html":"c431714fb4d59dc59cb28b82fcf8897d","spoc/cloud/caseIntro.html":"1b11dc7f63770dfabd2799973dc3ed3e","spoc/cloud/courseResource.html":"28f7edb6b39cdb3599f005d2495e0723","spoc/cloud/help.html":"42d81bd7708f33bb3128674d1d51a0a4","spoc/cloud/index.html":"001543e4c69b9b0b489813b1cdb56ce2","spoc/spoc.html":"49fd3bcc418771ffa5480af5d3e93a60","teacherPage/course.html":"87168ff34623467fd0f8a31a639219bc","teacherPage/discuss.html":"34ec0d0ca0f3638f7ab1ea04342d2256","teacherPage/index.html":"6c7b1fb1d1445bd8ff77156005cd6a16","vocation/vocation.html":"3265db08b7b4e9e15edf1aacb048a3e7"}};</script>
<script src="http://mc.stu.126.net/pub/s/web/libEs5Shim_756305f19411676ebd3089401c210201.js"></script>
<script>
window.gaProduct = "mooc";
window.urlPrefix = {
indexPrefix             : "/",
homePrefix              : "/home.htm",
loginPrefix             : "/member/login.htm",
logoutPrefix            : "/passport/member/logout.htm",
searchPrefix            : "/search.htm",
courseListPrefix        : "/category/all",
universityListPrefix    : "/university/view/all.htm",
universityPrefix        : "/university/",
universityPreviewPrefix : "/university/preview/",
vocationIndexPrefix     : "/vemooc",
courseInfoPrefix        : "/course/",
courseInfoPreviewPrefix : "/course/preview/",
courseLearnPrefix       : "/learn/",
courseLearnPreviewPrefix: "/learn/preview/",
courseLearnReviewPrefix : "/learn/review/",
learnForTeacherPrefix   : "/learn/enroll/",
spocMainPrefix          : "/spoc/schoolcloud/index.htm",
spocCourseInfoPrefix    : "/spoc/course/",
spocCourseLearnPrefix   : "/spoc/learn/",
spocUsityIdPrefix       : "/spoc/university.htm?schoolId=",
spocUniversityListPrefix      : "/university/view/all.htm",
spocUniversityPrefix       	  : "/spoc/university/",
spocUniversityPreviewPrefix   : "/spoc/university/preview/",
spocMemberPrefix       		  : "/spoc/u/",
spocMemberPreviewPrefix       : "/spoc/u/preview/",
memberPrefix            : "/u/",
memberPreviewPrefix     : "/u/preview/",
addMemberInfoPrefix     : "http://www.icourse163.org/member/addMemberInfo.htm",
partnerSuperAdminPrefix : "/partnerAdmin/superAdmin.htm",
partnerEditorAdminPrefix: "/partnerAdmin/editorAdmin.htm",
adminManagerPrefix      : "/collegeAdmin/schoolPanel.htm",
adminTeacherPrefix      : "/collegeAdmin/teacherPanel.htm",
coursecreatePrefix      : "/collegeAdmin/courseCreate.htm",
adminSetMessagePrefix   : "/collegeAdmin/setMessage.htm",
adminSettingPrefix      : "/collegeAdmin/setting.htm",
adminToolsPrefix        : "/collegeAdmin/tools.htm",
termManagePrefix        : "/collegeAdmin/termManage/",
reviewQuizPrefix        : "/review/quiz/{id}.htm",
reviewHwPrefix          : "/review/hw/",
reviewTrainPrefix       : "/review/train/",
teacherMainEditPrefix   : "/user/teacherMainEdit.htm",
personInfoSettingPrefix : "/user/setting/personInfoEdit.htm",
accountSettingPrefix    : "/user/setting/accountSetting.htm",
attachmentPrefix        : "/homework/attachment.htm",
titleAttachmentPrefix   : "/question/title/attachment.htm",
notSupportedPrefix      : "/common/errors/notSupported.htm",
helpFrontPrefix         : "/help/help.htm",
helpBackIndexPrefix     : "/help/helpIndex.htm",
helpBackPrefix          : "/help/manageHelp.htm",
aboutUsPrefix           : "/about/aboutus.htm",
contactUsPrefix         : "/about/contactus.htm",
certApplyPrefix         : "/cert/apply.htm",
certDesignPrefix        : "/cert/certDesign/{id}.htm",
chargeCertDesignPrefix  : "/cert/chargeCertDesign/{id}.htm",
payOrderPrefix          : "/pay/order.htm",
donateCoursePrefix      : "/donate/course.htm",
getTextPrefix           : "/resource/getText.htm",
cdnReportPrefix			: 'http://study.163.com/about/cdnReport.htm',
snsOAuthPrefix          : "/passport/sns/doOAuth.htm",
ursAuthorPrefix         : "http://www.icourse163.org/member/ursLogin.htm",
thirdBindCallbackHref   : "http://www.icourse163.org/logingate/urs/bindCallback.htm",
icourseAuthorPrefix     : "http://www.icourse163.org/member/icourseLogin.htm"
};
window.moocHost             = "icourse163.org";
window.moocHref             = "http://www.icourse163.org";
window.moocStaticHost       = "mc.stu.126.net";
window.callAppDownloadHref  = "http://www.icourse163.org/client/callAppDownload.htm";
window.NEJ_CONF = {
clipboard: 'http://mc.stu.126.net/res/swf/nej_clipboard.swf?0eba83544b107d7207d8936baab41283'
};

window.serverTimeDiff = new Date().getTime() - 1508246505807;
window.webUser = {
id:"1024008068",
nickName:"wuplus",
roles:[
],
passport:"68589219D8D13DF9741B8380DAB5BBAF",
personalUrlPrefix:"http://www.icourse163.org/u/",
personalUrlSuffix:"mooc1486474581274",
smallFaceUrl:"http://edu-image.nosdn.127.net/2C152CF7D122FEEADD3D82DCF1814F01.jpg?imageView&amp;thumbnail=28y28&amp;quality=100",
largeFaceUrl:"http://edu-image.nosdn.127.net/2C152CF7D122FEEADD3D82DCF1814F01.jpg?imageView&amp;thumbnail=120y120&amp;quality=100",
loginId:"68589219D8D13DF9741B8380DAB5BBAF",
loginType:"4",

email:"3013568147@qq.com",

end_key:"end_value"
};
window.cert_owner = false;
window.currentPageName = "home";
window.imageUrlMap = {
loading_circle_gif:"http://mc.stu.126.net/res/images/ui/loading_circle.gif?00ef871b291bc03a497d608a5bd8ec99",
share_sprite:"http://mc.stu.126.net/res/images/ui/shareUI.png?e2653a364a790663aed6c6ece19fd83a",
ui_sprite:"http://mc.stu.126.net/res/images/ui/ui_sprite.png?5f7eedcf69b8a05d3ed53b4c1918de1c",
forum_icon_sprite:"http://mc.stu.126.net/res/images/ui/forum_icon.png?b12539c2400cc76ad30262bdf7e12cbd",
image_upload_swf:"http://mc.stu.126.net/res/swf/imageUpload.swf?884965992b66cee07fb945929ac4b00f",
image_pdf_swf:"http://mc.stu.126.net/res/swf/pdfReader.swf?74ddf86a5d97e5af891638154a0989d1",
image_video_swf:"http://mc.stu.126.net/res/swf/moocPlayer.swf",
img_upd_select_swf:"http://mc.stu.126.net/res/swf/DragCutUpload_mooc.swf?ac94fb92d65cb0f12a93a8ca00fa3df9",
img_default_big_head:"http://edu-image.nosdn.127.net/457BE69DFFF1A6157EAF6D44EA2D8662.png?imageView&thumbnail=180y180&quality=100",
img_default_small_head:"http://mc.stu.126.net/res/images/common/headImg/small.jpg?06517f5e438da035a4016abd8e661d2f",
img_default_unviersity_1:"http://mc.stu.126.net/res/images/common/default/university1.png?55bbec907070a55ee4d333bc645445d1",
img_default_unviersity_2:"http://mc.stu.126.net/res/images/common/default/university2.png?a00032f80fa68a6ea6135ee8df9ed7a4",
img_default_unviersity_3:"http://mc.stu.126.net/res/images/common/default/university3.png?63f350451049f7803b014abab9408a4d",
img_default_unviersity_cert:"http://mc.stu.126.net/res/images/common/default/universityCert.png?4c209d5c5ebddc91e80fcf34795ddae1",
img_default_course:"http://mc.stu.126.net/res/images/common/default/course.jpg?2bc75b250fac482eabbcbc071b94abd4",
img_default_signature:"http://mc.stu.126.net/res/images/common/signature_example.png?a15f9c690bfd58771de32d5c483dea59",
img_step_score_mail:"http://mc.stu.126.net/res/images/common/step_score_mail.jpg?201e015a404c3c7aef85de694a4b6622"
};
window.swfUrlMap = {
CloudPlayer:"http://mc.stu.126.net/res/swf/eduPlayer.swf?44b31cc78f39b70739b248ddfc803915",
cloudPlayerUI:"http://mc.stu.126.net/res/swf/cloudPlayerUI.swf?83eaf96a4fa93df776e734c42d59ecc6"
}
window.URSLoginConfig = {
product : 'imooc',
promark : 'cjJVGQM',
host : 'www.icourse163.org',
cookieDomain : 'icourse163.org',
skin : 3,
page : 'login',
needUnLogin : 1 ,
defaultUnLogin:1,
placeholder : {account:'常用邮箱或网易邮箱',pwd:'密码'},
needPrepare: 1,
regUrl : 'http://zc.reg.163.com/regInitialized?pd=imooc&pkid=YeaYYzQ&pkht=www.icourse163.org',
coverBackground : "background:-webkit-radial-gradient(center,rgba(0,0,0,0.3),#000 75%);",
single : 1,
cssDomain : 'http://cmc.stu.126.net/u/css/cms/',
cssFiles : 'urs4moocweb.css',
frameSize : {'width':380,'height':282},
logincb : function(cb){}
};
</script>
<script type="text/javascript" src="http://ursdoccdn.nosdn.127.net/webzj_cdn101/pathb_message_17011101.js"></script>
<script src="http://mc.stu.126.net/pub/s/web/libRegular_e3fc7f63ef5a597f84cc352c95c59683.js"></script><script type="text/javascript">
window.isMobilePhone = "false";
window.gaTrackPageview = '_trackPageview';
window.gaTrackEvent = '_trackEvent';
window.gaqStr = '_gaq';
window._gaq = [];
window._gaq.push(['_setAccount', 'UA-35176345-3'],['_setLocalGifPath', '/UA-35176345-3/__utm.gif'],['_setLocalRemoteServerMode']);
window._gaq.push(['_addOrganic', 'm.baidu.com', 'word']);
window._gaq.push(['_addOrganic', 'soso', 'search']);
window._gaq.push(['_addOrganic', 'sogou', 'query']);
window._gaq.push(['_addOrganic', 'haosou', 'q']);
window._gaq.push(['_addOrganic', 'youdao', 'q']);
window._gaq.push(['_addOrganic', 'chinaso', 'q']);
window._gaq.push(['_addOrganic', 'zhongsou', 'w']);
window._gaq.push(['_addOrganic', 'm.sp.sm.cn', 'w']);
(function() {
var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
ga.src = 'http://wr.da.netease.com/ga.js';
var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
})();
</script>
<!--[if lt IE 9]>
<script src="http://mc.stu.126.net/pub/s/web/libH5Shiv_f4d9dea8e0ae8455500862bbb874d63c.js"></script>
<![endif]-->
</head>
<link rel="stylesheet" href="http://mc.stu.126.net/pub/s/web/pt_home_16e6e3fc07c8ec874178a9562aca6ce3.css"/>
<body>
<div id="j-activityBanner" class="f-dn ga-click" data-cate="小黄条" data-action="点击" style="position:relative;z-index:300;"></div>
<div id="j-activityRightBanner" class="ga-click" style="position:fixed;z-index:300;text-align:right;right: 16px;bottom:143px;"></div>
<div id="j-appbanner" style="position:relative;z-index:300;"></div>
<div id="g-container">
<div class="web-nav-container">
<div class="m-navTop-func">
<div class="m-navTop-func-i">
<div class="u-navLogin-container">
<div class="u-navLogin-logo"><a href="http://www.icourse163.org" target="_top"><img width="190" height="28" src="http://edu-image.nosdn.127.net/C0124E0336721FF65563B76A16A8143F.png?imageView&thumbnail=190y28&quality=100"></a></div>
<div class="e-hover-source u-navLogin-course"><a href="http://www.icourse163.org/category/all" target="_top"><span class="nav">课程</span></a>
<div class="e-hover-target">
<div class="e-hover-arrow"></div>
<div class="e-hover-arrow-border"></div>
<div class="e-hover-content">
<div class="j-nav-CateBox u-cateBox-container"></div>
</div>
</div>
</div>
<div class="u-navLogin-school"><a href="http://www.icourse163.org/university/view/all.htm" target="_top"><span class="nav">名校</span></a></div>
<div class="u-navLogin-loginBox">
<div class="u-navLogin-loginBox-i">
<div class="m-navlinks" id='j-topnav'>
<div class="login f-cb">
<div class="info f-pr j-nav-info-box">
<div class="face f-fl f-thide">
<a class="" href="/home.htm?userId=1024008068" target="_self">
<img class="" id="my-img"
src="http://imgsize.ph.126.net/?enlarge=true&imgurl=http://edu-image.nosdn.127.net/2C152CF7D122FEEADD3D82DCF1814F01.jpg?imageView&amp;amp;thumbnail=120y120&amp;amp;quality=100_30x30x1x95.png"
width="30" height="30" alt="wuplus">
</a>
</div>
<div class="j-nav-set sets" style="display:none">
<div class="e-hover-arrow"></div>
<div class="e-hover-arrow-border"></div>
<ul class="set">
<li class="text"><span class="f-fc9">正使用“腾讯QQ”帐号登录</span></li>
<li class="f-dn j-my-live"><a class="f-fc6 ga-click" data-cate="导航栏" href="/live/liveRoom.htm" data-action="头像下点击" target="_blank">我的直播</a></li>
<li class="j-cert-card" style="display:none;"><a class="f-fc6" href="/home.htm?userId=1024008068#/home/mycert" target="_blank">我的认证证书</a></li>
<li class="j-partner-man" style="display:none;"><a class="f-fc6" href="/partnerAdmin/superAdmin.htm" target="_blank">高教社管理员</a></li>
<li class="j-editor-man" style="display:none;"><a class="f-fc6 j-editor-txt" href="/partnerAdmin/editorAdmin.htm" target="_blank"></a></li>
<li class="j-school-man" style="display:none;"><a class="f-fc6" href="/collegeAdmin/schoolPanel.htm" target="_blank">高校管理后台</a></li>
<li class="j-postgrade-man" style="display:none;"><a class="f-fc6" href="/collegeAdmin/postgradExamSchoolPanel.htm" target="_blank">考研高校管理后台</a></li>
<li class="j-teacher-man" style="display:none;"><a class="f-fc6" href="/collegeAdmin/teacherPanel.htm" target="_blank">课程管理后台</a></li>
<li class="j-teacher-main" style="display:none;"><a class="f-fc6" href="/u/mooc1486474581274" target="_blank">老师主页</a></li>
<li><a class="f-fc6" href="/user/setting/personInfoEdit.htm" target="_blank">设置</a></li>
<li class="exit"><a class="f-fc6" href="/member/logout.htm" >退出</a></li>
</ul>
</div>
</div>
<div class="j-passportforplug" style="display:none;">68589219D8D13DF9741B8380DAB5BBAF</div>
<div class="arrow"></div>
</div>
</div></div>
</div>
<div class="ga-click u-navLogin-myCourse" data-cate="首页_头部导航" data-action="个人中心">
<div class="u-navLogin-myCourse-t">
<div class="ga-click u-navLogin-myCourse u-navLogin-center-container" data-cate="首页_头部导航" data-action="个人中心"><a href="http://www.icourse163.org/home.htm?userId=1024008068" target="_top"><span class="nav">个人中心</span></a></div>
</div>
</div>
<div class="u-navLogin-searchFunc">
<div class="u-navLogin-searchFunc-i">
<div class="j-search-box u-search-container">
<div class="j-input u-search-input"></div>
<div class="u-search-icon"><span class="u-icon-search2 j-searchBtn"></span></div>
</div>
</div>
</div>
<div class="e-hover-source u-navLogin-appText"><a href="http://www.icourse163.org/mobile.htm?from=navibar&mobiletopbar=hidden" target="_top"><span class="nav">客户端</span></a>
<div class="e-hover-target">
<div class="e-hover-arrow"></div>
<div class="e-hover-arrow-border"></div>
<div class="e-hover-content">
<div class="u-app-download-container">
<div class="u-app-tip"><span>扫码下载官方APP</span></div>
<div class="u-app-qrcode"><img width="140" height="140" src="http://img1.ph.126.net/Rg6muO26iMOFWx9vwEHC-g==/6630234335885341999.png"></div>
<div class="u-app-iphone-link"><a href="https://itunes.apple.com/cn/app/id977883304" target="_blank"></a></div>
<div class="u-app-android-link"><a href="http://study.163.com/pub/ucmooc/ucmooc-android-official.apk" target="_blank"></a></div>
</div>
</div>
</div>
</div>
<div class="u-navLogin-app"><img width="13" height="21" src="http://edu-image.nosdn.127.net/03CC83FA97B35119DFB8C772754765CC.png?imageView&thumbnail=13y22&quality=100"></div>
<div class="u-navLogin-discuss"><a href="http://www.icourse163.org/forum/1001974001.htm" target="_top"><span class="nav">学 · 问</span></a></div>
<div class=" u-navLogin-cloud">
<a href="http://www.icourse163.org/spoc/schoolcloud/index.htm" target="_blank"><span class="nav">学校云</span></a>
</div>
<div class="j-kaoyan-link u-navLogin-kaoyan">
<a href="//kaoyan.icourse163.org" target="_blank"><span class="nav">考研</span></a></div>
<div class="j-latest-mark u-navLogin-mark f-f0 f-dn"><span>新</span></div>
</div>
</div>
</div>
</div><div id="g-body"><div id="j-self-content" class=" top-box f-f0">
<img class="top-bac f-dn" id="j-top-back" width="100%" height="220" src="http://edu-image.nosdn.127.net/BCA790F6E742B8CBF078CA413D2ED7AD.png?imageView&thumbnail=1920y220&quality=100">
</div>
<div id="j-mailNotice" class="p-tp-email">
</div>
<div id="j-home-content" class="home-content"></div>
</div>
<div class="g-wrap m-foot f-pr" id="j-footer">
<div class="g-flow f-cb">
<div class="f1 f-fl">
<div class="logo"></div>
<p class="f-fc14 f-fc9">由高教社联手网易推出，让每一个有提升愿望的用户能够学到中国知名高校的课程，并获得认证。</p>
</div>
<div class="f4 f-fr f-pr">
<h4 class="f-fcc">友情链接</h4>
<div class="f-cb">
<a href="http://kada.study.163.com/?inref=index_bottomlink" target="_blank" class="f-fc9 f4a">网易卡搭</a>
<a href="http://study.163.com/" target="_blank" class="f-fc9 f4a">网易云课堂</a>
<a href="http://100.163.com/" target="_blank" class="f-fc9 f4a">网易100分</a>
</div>
</div>
<div class="f3 f-fr f-pr">
<h4 class="f-fcc">关注我们</h4>
<div class="f-cb">
<a class="f-icon f-fc9 u-icon-weixin weixin gzIc f-pr f-fl">
<div class="tipQrcode f-pa">
<div class="qrImag">
<img src="http://img1.ph.126.net/B2oJVwACEBhteg--bddGYw==/978969969017630218.png" width="120px" height="120px" alt="加中M微信好友">
</div>
<div class="tip f-pa"></div>
</div>
</a>
<a href="http://weibo.com/icourse163" target="_blank" class="f-icon f-fc9 gzIc f-fs1 f-fl u-icon-weibo weibo"></a>
</div>
</div>
<div class="f2 f-fr f-pr">
<h4 class="f-fcc">关于我们</h4>
<div class="f-cb">
<a href="/about/aboutus.htm" target="_blank" class="f-fc9 f2a">关于我们</a>
<a href="/spoc/schoolcloud/index.htm" target="_blank" class="f-fc9 f2a">学校云</a>
<a href="/about/contactus.htm#/contactus?type=2" target="_blank" class="f-fc9 f2a">联系我们</a>
<a href="/help/help.htm" target="_blank" class="f-fc9 f2a">常见问题</a>
<a href="/about/contactus.htm#/contactus?type=4" target="_blank" class="f-fc9 f2a">意见反馈</a>
<a href="/about/contactus.htm#/contactus?type=5" target="_blank" class="f-fc9 f2a">法律条款</a>
</div>
</div>
</div>
<div class="beian"><p class="f-fc12 f-fc6"> <a class="f-fc6" target="_blank" href="http://www.miitbeian.gov.cn/state/outPortal/loginPortal.action">粤B2-20090191-26</a> | 京ICP备12020869号-2 | <a class="f-fc6" target="_blank" href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=44010602000207">京公网安备44010602000207</a> <br>©2014-2017 icourse163.org </p></div>
</div>
</div>
<script>
window.isNeedFillMemberInfo = false;
if(!location.search && window.webUser){
location.search = "?userId="+ window.webUser.id;
}
</script>
<script src="http://mc.stu.126.net/pub/s/web/core_2f054fcdf80a72e7d461972c02893d55.js"></script>
<script src="http://mc.stu.126.net/pub/s/web/pt_home_3161ef34b4f2a345ce26d45bffdd1fb8.js"></script>
</body>
</html>"""
select = etree.HTML(html)
result = select.xpath('//li')
for i in result:
    print(result)

print type(result[0])

