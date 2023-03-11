import pytest
from scrapy.http import HtmlResponse


def test_html_selector():
    html_body = u'''
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml" id="html">
<head><meta http-equiv="Cache-Control" content="no-siteapp" /><meta http-equiv="Cache-Control" content="no-transform " /><meta http-equiv="Content-Type" content="text/html; charset=UTF-8" /><title>
	古诗三百首_古诗文网
</title>
<script type="text/javascript">
    if ((navigator.userAgent.match(/(phone|pad|pod|iPhone|iPod|ios|iPad|Android|Mobile|BlackBerry|IEMobile|MQQBrowser|JUC|Fennec|wOSBrowser|BrowserNG|WebOS|Symbian|Windows Phone)/i))) {
        window.location.href = "https://m.gushiwen.cn/gushi/sanbai.aspx";
    } else {

    }
</script>
<link href="/css/skinSo220601.css" rel="stylesheet" type="text/css" />
    <script src="/js/jquery-3.2.1.min.js" type="text/javascript"></script>
<script type="text/javascript">
    //取得cookie值
    function getCookie(name) {
        var arr, reg = new RegExp("(^| )" + name + "=([^;]*)(;|$)");

        if (arr = document.cookie.match(reg))

            return unescape(arr[2]);
        else
            return null;
    }

    //判断收藏
    function selectLike(id) {
        document.getElementById('likeImg' + id).name = parseInt(document.getElementById('likeImg' + id).name) + 1;
        if (document.getElementById('likeImg' + id).name == '1') {
            var idsShigeLaiyo = getCookie('idsShiwen2017');
            if (idsShigeLaiyo != null && idsShigeLaiyo != '') {
                var ids = idsShigeLaiyo.split(',');
                for (var i = 0; i < ids.length; i++) {
                    if (ids[i] == id) {
                        document.getElementById('likeImg' + id).src = 'https://song.gushiwen.cn/siteimg/shou-cangok.png';
                        document.getElementById('likeImg' + id).alt = '已收藏';
                        break;
                    }
                }
            }
        }
    }

    //判断收藏名句
    function selectLikeMingju(id) {
        document.getElementById('likeImg' + id).name = parseInt(document.getElementById('likeImg' + id).name) + 1;
        if (document.getElementById('likeImg' + id).name == '1') {
            var idsShigeLaiyo = getCookie('idsMingju2017');
            if (idsShigeLaiyo != null && idsShigeLaiyo != '') {
                var ids = idsShigeLaiyo.split(',');
                for (var i = 0; i < ids.length; i++) {
                    if (ids[i] == id) {
                        document.getElementById('likeImg' + id).src = 'https://song.gushiwen.cn/siteimg/shou-cangok.png';
                        document.getElementById('likeImg' + id).alt = '已收藏';
                        break;
                    }
                }
            }
        }
    }

    //判断收藏作者
    function selectLikeAuthor(id) {
        document.getElementById('likeImg' + id).name = parseInt(document.getElementById('likeImg' + id).name) + 1;
        if (document.getElementById('likeImg' + id).name == '1') {
            var idsShigeLaiyo = getCookie('idsAuthor2017');
            if (idsShigeLaiyo != null && idsShigeLaiyo != '') {
                var ids = idsShigeLaiyo.split(',');
                for (var i = 0; i < ids.length; i++) {
                    if (ids[i] == id) {
                        document.getElementById('likeImg' + id).src = 'https://song.gushiwen.cn/siteimg/shou-cangok.png';
                        document.getElementById('likeImg' + id).alt = '已收藏';
                        break;
                    }
                }
            }
        }
    }

    //判断收藏古籍
    function selectLikeGuwen(id) {
        document.getElementById('likeImg' + id).name = parseInt(document.getElementById('likeImg' + id).name) + 1;
        if (document.getElementById('likeImg' + id).name == '1') {
            var idsShigeLaiyo = getCookie('idsGuji2017');
            if (idsShigeLaiyo != null && idsShigeLaiyo != '') {
                var ids = idsShigeLaiyo.split(',');
                for (var i = 0; i < ids.length; i++) {
                    if (ids[i] == id) {
                        document.getElementById('likeImg' + id).src = 'https://song.gushiwen.cn/siteimg/shou-cangok.png';
                        document.getElementById('likeImg' + id).alt = '已收藏';
                        break;
                    }
                }
            }
        }
    }
    </script>

    <script>
        var _hmt = _hmt || [];
        (function () {
            var hm = document.createElement("script");
            hm.src = "//hm.baidu.com/hm.js?9007fab6814e892d3020a64454da5a55";
            var s = document.getElementsByTagName("script")[0];
            s.parentNode.insertBefore(hm, s);
        })();
</script>

</head>
<body onclick="closeshowBos()">
<div class="main1">
    <div class="cont">
        <div class="left">
            <a href="https://www.gushiwen.cn/">古诗文网</a>
        </div>
        <div class="right">
            <div class="son1">
                <a style="margin-left:1px;" href="https://www.gushiwen.cn/">推荐</a>
                  
                  <a href="/shiwens/" style="background-color:#757863;border-bottom:3px solid #F0EFE2;line-height:43px; height:43px;">诗文</a>
                   
                  <a href="/mingjus/">名句</a>
                   
                  <a href="/authors/">作者</a>
                   
                  <a href="/guwen/">古籍</a>
                  
                  <a href="/user/collect.aspx" rel="nofollow">我的</a>
                  
                <a style="width:65px;" href="/app/" target="_blank">手机版</a>
            </div>
            <div class="son2">
                <div class="search">
                <form action="/search.aspx" onsubmit="return selectSearch()" contentType="text/html; charset=utf-8">
                    <input onkeydown="noajaxkeyUp()" oninput ="goshowBos()" id="txtKey" name="value" type="text" value="" maxlength="40" autocomplete="off" style="height:25px; line-height:25px; float:left; padding-left:5px; width:260px; font-size:14px; clear:left; border:0px;" />
                    <input style=" display:none;" id='valuej' name="valuej" value="" />
                    <input type="submit" style="float:right; width:24px; height:24px; clear:right; margin-top:2px; margin-right:3px; background-image:url(https://song.gushiwen.cn/siteimg/docSearch.png); background-repeat:no-repeat; background-size:24px 24px; border:0px;cursor:pointer;" value="" />
                    <input id="b" style="display:none;" type="text" />
                </form>
                </div>
                <div id="box"></div>
            </div>
        </div>
    </div>
</div>
        
<div class="main3">
    <div class="left">
        <div class="title">
        <div class="titleleft"></div>
        <h1>古诗三百首</h1>
        </div>
        <div class="sons">
        <div class="typecont">
            <div class="bookMl"><strong>先秦两汉诗</strong></div>
                <span><a href="/shiwenv_21c484c79935.aspx" target="_blank">击壤歌</a>(夏商民歌)</span>
                <span><a href="/shiwenv_4c5705b99143.aspx" target="_blank">关雎</a>《诗经》</span>
                <span><a href="/shiwenv_478043ea449a.aspx" target="_blank">木瓜</a>《诗经》</span>
                <span><a href="/shiwenv_6ba04da3fdc1.aspx" target="_blank">桃夭</a>《诗经》</span>
                <span><a href="/shiwenv_15cd220102d6.aspx" target="_blank">蒹葭</a>《诗经》</span>
                <span><a href="/shiwenv_ab10f29a0d36.aspx" target="_blank">无衣</a>《诗经》</span>
                <span><a href="/shiwenv_8dd719a833f0.aspx" target="_blank">河广</a>《诗经》</span>
                <span><a href="/shiwenv_1fecfb7d6ac8.aspx" target="_blank">采薇</a>《诗经》</span>
                <span><a href="/shiwenv_1cc4f4d60a66.aspx" target="_blank">硕鼠</a>《诗经》</span>
                <span><a href="/shiwenv_ac847f034730.aspx" target="_blank">伐檀</a>《诗经》</span>
                <span><a href="/shiwenv_52ddfd4a0f5c.aspx" target="_blank">相鼠</a>《诗经》</span>
                <span><a href="/shiwenv_60ff036cbc0e.aspx" target="_blank">易水歌</a>(荆轲)</span>
                <span><a href="/shiwenv_7b0679dcf4a4.aspx" target="_blank">垓下歌</a>(项羽)</span>
                <span><a href="/shiwenv_1d9d6294438d.aspx" target="_blank">大风歌</a>(刘邦)</span>
                <span><a href="/shiwenv_515f5c1f245b.aspx" target="_blank">秋风辞</a>(刘彻)</span>
                <span><a href="/shiwenv_8ac2a2fae9c7.aspx" target="_blank">李延年歌</a>(李延年)</span>
                <span><a href="/shiwenv_4ef2774ed20a.aspx" target="_blank">上邪</a>(汉乐府民歌)</span>
                <span><a href="/shiwenv_ef9cd9ba44bb.aspx" target="_blank">江南</a>(汉乐府民歌)</span>
                <span><a href="/shiwenv_183d69f50755.aspx" target="_blank">长歌行</a>(汉乐府民歌)</span>
                <span><a href="/shiwenv_db1436a0175e.aspx" target="_blank">古歌</a>(汉乐府民歌)</span>
                <span><a href="/shiwenv_5f6efd08156d.aspx" target="_blank">十五从军征</a>(汉乐府民歌)</span>
                <span><a href="/shiwenv_a7e1ebce8d01.aspx" target="_blank">明月何皎皎</a>(古诗十九首)</span>
                <span><a href="/shiwenv_0046a6e4e3e8.aspx" target="_blank">东城高且长</a>(古诗十九首)</span>
                <span><a href="/shiwenv_cfa983aabd96.aspx" target="_blank">行行重行行</a>(古诗十九首)</span>
                <span><a href="/shiwenv_c72d94b49cc6.aspx" target="_blank">涉江采芙蓉</a>(古诗十九首)</span>
                <span><a href="/shiwenv_7f09a756c9c0.aspx" target="_blank">迢迢牵牛星</a>(古诗十九首)</span>
                <span><a href="/shiwenv_7969b037360b.aspx" target="_blank">回车驾言迈</a>(古诗十九首)</span>
                <span><a href="/shiwenv_6105b29267b5.aspx" target="_blank">客从远方来</a>(古诗十九首)</span>
                <span><a href="/shiwenv_74f93a1d0f88.aspx" target="_blank">凛凛岁云暮</a>(古诗十九首)</span>
                <span><a href="/shiwenv_b9a75d49f3c5.aspx" target="_blank">桓灵时童谣</a>(佚名)</span>
</div>
<div class="typecont">
<div class="bookMl"><strong>魏晋南北朝诗</strong></div>
            <span><a href="/shiwenv_d78b6331098e.aspx" target="_blank">龟虽寿</a>(曹操)</span>
            <span><a href="/shiwenv_0c29e174924a.aspx" target="_blank">蒿里行</a>(曹操)</span>
            <span><a href="/shiwenv_630c04c81858.aspx" target="_blank">观沧海</a>(曹操)</span>
            <span><a href="/shiwenv_35000de73cdb.aspx" target="_blank">短歌行</a>(曹操)</span>
            <span><a href="/shiwenv_2d0c9ade951e.aspx" target="_blank">赠从弟</a>(刘桢)</span>
            <span><a href="/shiwenv_88ccf5cf1d59.aspx" target="_blank">室思</a>(徐干)</span>
            <span><a href="/shiwenv_dc47feaddcd7.aspx" target="_blank">燕歌行</a>(曹丕)</span>
            <span><a href="/shiwenv_11d3cbf86d9d.aspx" target="_blank">白马篇</a>(曹植)</span>
            <span><a href="/shiwenv_305d29fb64aa.aspx" target="_blank">七步诗</a>(曹植)</span>
            <span><a href="/shiwenv_2b832f229933.aspx" target="_blank">杂诗·南国有佳人</a>(曹植)</span>
            <span><a href="/shiwenv_cf61fbd62088.aspx" target="_blank">七哀诗·西京乱无象</a>(王粲)</span>
            <span><a href="/shiwenv_3dfd964acf90.aspx" target="_blank">赠秀才入军·其十四</a>(嵇康)</span>
            <span><a href="/shiwenv_7b8b53c74b60.aspx" target="_blank">咏怀八十二首·其一</a>(阮籍)</span>
            <span><a href="/shiwenv_d8de659f4173.aspx" target="_blank">吴孙皓初童谣</a>(无名氏)</span>
            <span><a href="/shiwenv_5f6cff2b82eb.aspx" target="_blank">咏史·郁郁涧底松</a>(左思)</span>
            <span><a href="/shiwenv_cf73601829ff.aspx" target="_blank">思吴江歌</a>(张翰)</span>
            <span><a href="/shiwenv_a537ff195683.aspx" target="_blank">归园田居·其一</a>(陶渊明)</span>
            <span><a href="/shiwenv_a9c118750a79.aspx" target="_blank">归园田居·其三</a>(陶渊明)</span>
            <span><a href="/shiwenv_5b90a9bb5230.aspx" target="_blank">饮酒·其五</a>(陶渊明)</span>
            <span><a href="/shiwenv_cb6db9f85f94.aspx" target="_blank">咏荆轲</a>(陶渊明)</span>
            <span><a href="/shiwenv_e80463a9d45e.aspx" target="_blank">读山海经·其一</a>(陶渊明)</span>
            <span><a href="/shiwenv_8e0c3f897ea9.aspx" target="_blank">读山海经·其十</a>(陶渊明)</span>
            <span><a href="/shiwenv_404930bd804c.aspx" target="_blank">杂诗</a>(陶渊明)</span>
            <span><a href="/shiwenv_9481782facfb.aspx" target="_blank">酌贪泉</a>(吴隐之)</span>
            <span><a href="/shiwenv_fb47fbe5b9c7.aspx" target="_blank">登江中孤屿</a>(谢灵运)</span>
            <span><a href="/shiwenv_5261df279f62.aspx" target="_blank">拟行路难·其四</a>(鲍照)</span>
            <span><a href="/shiwenv_62aea44ba9a1.aspx" target="_blank">拟行路难·其六</a>(鲍照)</span>
            <span><a href="/shiwenv_18d68bd0d5a9.aspx" target="_blank">梅花落</a>(鲍照)</span>
            <span><a href="/shiwenv_cf482f8bf41e.aspx" target="_blank">赠范晔诗</a>(陆凯)</span>
            <span><a href="/shiwenv_ccb4d7a7d147.aspx" target="_blank">晚登三山还望京邑</a>(谢朓)</span>
            <span><a href="/shiwenv_4dd00caa9977.aspx" target="_blank">王孙游</a>(谢朓)</span>
            <span><a href="/shiwenv_ab33e7a49bd7.aspx" target="_blank">之零陵郡次新亭</a>(范云)</span>
            <span><a href="/shiwenv_6d23122c5741.aspx" target="_blank">估客乐</a>(释宝月)</span>
            <span><a href="/shiwenv_526fd025200d.aspx" target="_blank">夜夜曲</a>(沈约)</span>
            <span><a href="/shiwenv_e59a5b3e2028.aspx" target="_blank">咏早梅</a>(何逊)</span>
            <span><a href="/shiwenv_5e086e54af88.aspx" target="_blank">边城思</a>(何逊)</span>
            <span><a href="/shiwenv_89748a423718.aspx" target="_blank">山中杂诗</a>(吴均)</span>
            <span><a href="/shiwenv_e1b856d94566.aspx" target="_blank">诏问山中何所有赋诗</a>(陶宏景)</span>
            <span><a href="/shiwenv_3f7503246290.aspx" target="_blank">入若耶溪</a>(王籍)</span>
            <span><a href="/shiwenv_ddc36841d123.aspx" target="_blank">蜀道难·其一</a>(萧纲)</span>
            <span><a href="/shiwenv_934f1575c41f.aspx" target="_blank">蜀道难·其二</a>(萧纲)</span>
            <span><a href="/shiwenv_d221931bbef8.aspx" target="_blank">晚出新亭</a>(阴铿)</span>
            <span><a href="/shiwenv_00040aa34a6b.aspx" target="_blank">关山月</a>(徐陵)</span>
            <span><a href="/shiwenv_68051ed348e5.aspx" target="_blank">断句</a>(刘昶)</span>
            <span><a href="/shiwenv_5304d5173010.aspx" target="_blank">寄王琳</a>(庾信)</span>
            <span><a href="/shiwenv_c8b882d0cead.aspx" target="_blank">作蚕丝</a>(南朝民歌)</span>
            <span><a href="/shiwenv_863659d1c3b7.aspx" target="_blank">陇头歌辞</a>(北朝民歌)</span>
            <span><a href="/shiwenv_42ab3a41f32c.aspx" target="_blank">折杨柳歌辞</a>(北朝民歌)</span>
            <span><a href="/shiwenv_f996111bff75.aspx" target="_blank">敕勒歌</a>(北朝民歌)</span>
            <span><a href="/shiwenv_d7d3315f74d4.aspx" target="_blank">长安九日诗</a>(江总)</span>
            <span><a href="/shiwenv_29252ac44d0f.aspx" target="_blank">人日思归</a>(薛道衡)</span>
            <span><a href="/shiwenv_515c8ac22eae.aspx" target="_blank">侍宴咏石榴</a>(孔绍安)</span>
</div>
<div class="typecont">
<div class="bookMl"><strong>宋诗</strong></div>
            <span><a href="/shiwenv_2bba1443c73f.aspx" target="_blank">塞上</a>(柳开)</span>
            <span><a href="/shiwenv_62b40696d6c7.aspx" target="_blank">柳枝词</a>(郑文宝)</span>
            <span><a href="/shiwenv_0119bf86bce5.aspx" target="_blank">村行</a>(王禹偁)</span>
            <span><a href="/shiwenv_ef86254f695c.aspx" target="_blank">春居杂兴</a>(王禹偁)</span>
            <span><a href="/shiwenv_9488a9c708f6.aspx" target="_blank">柳</a>(寇准)</span>
            <span><a href="/shiwenv_10086b1c2cc6.aspx" target="_blank">书河上亭壁</a>(寇准)</span>
            <span><a href="/shiwenv_009089d2ab35.aspx" target="_blank">咏傀儡</a>(杨亿)</span>
            <span><a href="/shiwenv_e1339dc3ff03.aspx" target="_blank">山园小梅</a>(林逋)</span>
            <span><a href="/shiwenv_f98499b15326.aspx" target="_blank">落花</a>(宋祁)</span>
            <span><a href="/shiwenv_d4b985ecee90.aspx" target="_blank">宿甘露寺僧舍</a>(曾公亮)</span>
            <span><a href="/shiwenv_a9ba69db102b.aspx" target="_blank">东溪</a>(梅尧臣)</span>
            <span><a href="/shiwenv_660c5685f2ca.aspx" target="_blank">鲁山山行</a>(梅尧臣)</span>
            <span><a href="/shiwenv_4b580390b62b.aspx" target="_blank">陶者</a>(梅尧臣)</span>
            <span><a href="/shiwenv_862f48392426.aspx" target="_blank">考试毕登铨楼</a>(梅尧臣)</span>
            <span><a href="/shiwenv_c55b372b8545.aspx" target="_blank">初晴游沧浪亭</a>(苏舜钦)</span>
            <span><a href="/shiwenv_5c37302541f1.aspx" target="_blank">夏意</a>(苏舜钦)</span>
            <span><a href="/shiwenv_73df2273247f.aspx" target="_blank">蚕妇</a>(张俞)</span>
            <span><a href="/shiwenv_affc7e5b993a.aspx" target="_blank">晚泊岳阳</a>(欧阳修)</span>
            <span><a href="/shiwenv_b5a499a58256.aspx" target="_blank">画眉鸟</a>(欧阳修)</span>
            <span><a href="/shiwenv_9fc50f382e93.aspx" target="_blank">戏答元珍</a>(欧阳修)</span>
            <span><a href="/shiwenv_a929ae77e836.aspx" target="_blank">丰乐亭游春</a>(欧阳修)</span>
            <span><a href="/shiwenv_c5c55e166d05.aspx" target="_blank">别滁</a>(欧阳修)</span>
            <span><a href="/shiwenv_69c7960d910a.aspx" target="_blank">乡思</a>(李觏)</span>
            <span><a href="/shiwenv_846e626d74d3.aspx" target="_blank">梅花</a>(王安石)</span>
            <span><a href="/shiwenv_f5b1b53b6e7e.aspx" target="_blank">叠题乌江亭</a>(王安石)</span>
            <span><a href="/shiwenv_a167901c9c90.aspx" target="_blank">元日</a>(王安石)</span>
            <span><a href="/shiwenv_df14e6fd217b.aspx" target="_blank">泊船瓜洲</a>(王安石)</span>
            <span><a href="/shiwenv_4a272f472fee.aspx" target="_blank">登飞来峰</a>(王安石)</span>
            <span><a href="/shiwenv_a233cb62c4be.aspx" target="_blank">春夜</a>(王安石)</span>
            <span><a href="/shiwenv_b40eef10e038.aspx" target="_blank">春日偶成</a>(程颢)</span>
            <span><a href="/shiwenv_b67f9200fc5e.aspx" target="_blank">新晴</a>(刘攽)</span>
            <span><a href="/shiwenv_4ee438cabb4a.aspx" target="_blank">雨后池上</a>(刘攽)</span>
            <span><a href="/shiwenv_d886bb39429c.aspx" target="_blank">暑旱苦热</a>(王令)</span>
            <span><a href="/shiwenv_0d1727cef77a.aspx" target="_blank">送春</a>(王令)</span>
            <span><a href="/shiwenv_3979911579cf.aspx" target="_blank">村居</a>(张舜民)</span>
            <span><a href="/shiwenv_a0290f719b42.aspx" target="_blank">咏柳</a>(曾巩)</span>
            <span><a href="/shiwenv_29b4e8c9ded3.aspx" target="_blank">城南</a>(曾巩)</span>
            <span><a href="/shiwenv_f2f5469a6044.aspx" target="_blank">题西林壁</a>(苏轼)</span>
            <span><a href="/shiwenv_84b5b3488790.aspx" target="_blank">惠崇春江晚景</a>(苏轼)</span>
            <span><a href="/shiwenv_31bc973d596d.aspx" target="_blank">和子由渑池怀旧</a>(苏轼)</span>
            <span><a href="/shiwenv_eafb4ea8a749.aspx" target="_blank">春宵</a>(苏轼)</span>
            <span><a href="/shiwenv_8949464433f0.aspx" target="_blank">饮湖上初晴后雨</a>(苏轼)</span>
            <span><a href="/shiwenv_c987db20a4d7.aspx" target="_blank">赠刘景文</a>(苏轼)</span>
            <span><a href="/shiwenv_df5646346cac.aspx" target="_blank">海棠</a>(苏轼)</span>
            <span><a href="/shiwenv_88a266b84b06.aspx" target="_blank">禾熟</a>(孔平仲)</span>
            <span><a href="/shiwenv_2ed4ff6cd2d0.aspx" target="_blank">寄内</a>(孔平仲)</span>
            <span><a href="/shiwenv_705ee4ad5c5f.aspx" target="_blank">牧童诗</a>(黄庭坚)</span>
            <span><a href="/shiwenv_8545428012cd.aspx" target="_blank">登快阁</a>(黄庭坚)</span>
            <span><a href="/shiwenv_fcaff9381740.aspx" target="_blank">鄂州南楼书事</a>(黄庭坚)</span>
            <span><a href="/shiwenv_6980f0bf99ae.aspx" target="_blank">雨中登岳阳楼望君山</a>(黄庭坚)</span>
            <span><a href="/shiwenv_4ab1896158c4.aspx" target="_blank">临平道中</a>(道潜)</span>
            <span><a href="/shiwenv_50b475cde3ac.aspx" target="_blank">春日</a>(晁冲之)</span>
            <span><a href="/shiwenv_48fd52d666eb.aspx" target="_blank">春日</a>(张耒)</span>
            <span><a href="/shiwenv_5f1aa916c2fb.aspx" target="_blank">夜坐</a>(张耒)</span>
            <span><a href="/shiwenv_cb5d821bdf54.aspx" target="_blank">纳凉</a>(秦观)</span>
            <span><a href="/shiwenv_1e0dccec086a.aspx" target="_blank">春日</a>(秦观)</span>
            <span><a href="/shiwenv_3145692e79f5.aspx" target="_blank">还自广陵</a>(秦观)</span>
            <span><a href="/shiwenv_5b1bdce24256.aspx" target="_blank">春怀示邻里</a>(陈师道)</span>
            <span><a href="/shiwenv_4e502c3f481a.aspx" target="_blank">示三子</a>(陈师道)</span>
            <span><a href="/shiwenv_f36fc0991d66.aspx" target="_blank">春游湖</a>(徐俯)</span>
            <span><a href="/shiwenv_75f517e12a1d.aspx" target="_blank">绝句</a>(吴涛)</span>
            <span><a href="/shiwenv_a0c7065be42d.aspx" target="_blank">连州阳山归路</a>(吕本中)</span>
            <span><a href="/shiwenv_ea1d6f4a3fde.aspx" target="_blank">自责</a>(朱淑真)</span>
            <span><a href="/shiwenv_e5325dec4270.aspx" target="_blank">落花</a>(朱淑真)</span>
            <span><a href="/shiwenv_94e232608ac8.aspx" target="_blank">春日</a>(汪藻)</span>
            <span><a href="/shiwenv_c689eae0951f.aspx" target="_blank">汴京纪事</a>(刘子翚)</span>
            <span><a href="/shiwenv_e4cd80aceb52.aspx" target="_blank">夏日绝句</a>(李清照)</span>
            <span><a href="/shiwenv_e51d28d4cdd5.aspx" target="_blank">苏秀道中</a>(曾几)</span>
            <span><a href="/shiwenv_fbbd80710c5e.aspx" target="_blank">三衢道中</a>(曾几)</span>
            <span><a href="/shiwenv_9b3d3cb65c13.aspx" target="_blank">病牛</a>(李纲)</span>
            <span><a href="/shiwenv_9a36e882c21f.aspx" target="_blank">襄邑道中</a>(陈与义)</span>
            <span><a href="/shiwenv_af50523b010a.aspx" target="_blank">雨晴</a>(陈与义)</span>
            <span><a href="/shiwenv_d73b1592e415.aspx" target="_blank">牡丹</a>(陈与义)</span>
            <span><a href="/shiwenv_b14d6469f3fa.aspx" target="_blank">池州翠微亭</a>(岳飞)</span>
            <span><a href="/shiwenv_178402e62453.aspx" target="_blank">樵夫</a>(萧德藻)</span>
            <span><a href="/shiwenv_0ccd54b5b58a.aspx" target="_blank">临安春雨初霁</a>(陆游)</span>
            <span><a href="/shiwenv_e86ad372580b.aspx" target="_blank">金错刀行</a>(陆游)</span>
            <span><a href="/shiwenv_bf183dbd63bc.aspx" target="_blank">剑门道中遇微雨</a>(陆游)</span>
            <span><a href="/shiwenv_53b46be5f768.aspx" target="_blank">梅花绝句</a>(陆游)</span>
            <span><a href="/shiwenv_966c8a76211f.aspx" target="_blank">示儿</a>(陆游)</span>
            <span><a href="/shiwenv_38c4a0c84fe9.aspx" target="_blank">十一月四日风雨大作</a>(陆游)</span>
            <span><a href="/shiwenv_7c14409ca751.aspx" target="_blank">书愤</a>(陆游)</span>
            <span><a href="/shiwenv_d02a847e3a85.aspx" target="_blank">病起书怀</a>(陆游)</span>
            <span><a href="/shiwenv_dab95da71436.aspx" target="_blank">秋夜将晓出篱门迎凉有感</a>(陆游)</span>
            <span><a href="/shiwenv_6e4b9596b2f3.aspx" target="_blank">四时田园杂兴</a>(范成大)</span>
            <span><a href="/shiwenv_1ddfa97c32c3.aspx" target="_blank">横塘</a>(范成大)</span>
            <span><a href="/shiwenv_0795b7d63e8d.aspx" target="_blank">州桥</a>(范成大)</span>
            <span><a href="/shiwenv_fd8967ffeeab.aspx" target="_blank">三江小渡</a>(杨万里)</span>
            <span><a href="/shiwenv_975bf39b1456.aspx" target="_blank">舟过安仁</a>(杨万里)</span>
            <span><a href="/shiwenv_e8965f3cb528.aspx" target="_blank">初入淮河四绝句</a>(杨万里)</span>
            <span><a href="/shiwenv_31dd7d07323c.aspx" target="_blank">小池</a>(杨万里)</span>
            <span><a href="/shiwenv_3ab4125fd0f1.aspx" target="_blank">晓出净慈寺送林子方</a>(杨万里)</span>
            <span><a href="/shiwenv_f92fb36ff846.aspx" target="_blank">宿新市徐公店</a>(杨万里)</span>
            <span><a href="/shiwenv_63f2cb1073ff.aspx" target="_blank">题临安邸</a>(林升)</span>
            <span><a href="/shiwenv_dd1c97accf6e.aspx" target="_blank">活水亭观书有感</a>(朱熹)</span>
            <span><a href="/shiwenv_ba4626c44270.aspx" target="_blank">春日</a>(朱熹)</span>
            <span><a href="/shiwenv_882d0d07d13e.aspx" target="_blank">立春偶成</a>(张栻)</span>
            <span><a href="/shiwenv_16b8ddde2dd8.aspx" target="_blank">除放自石湖归苕溪</a>(姜夔)</span>
            <span><a href="/shiwenv_1bba73cc8c98.aspx" target="_blank">过垂虹</a>(姜夔)</span>
            <span><a href="/shiwenv_bb59b6f85212.aspx" target="_blank">新凉</a>(徐玑)</span>
            <span><a href="/shiwenv_c1537124e930.aspx" target="_blank">约客</a>(赵师秀)</span>
            <span><a href="/shiwenv_07f5e3403665.aspx" target="_blank">乡村四月</a>(翁卷)</span>
            <span><a href="/shiwenv_99343af61310.aspx" target="_blank">江村晚眺</a>(戴复古)</span>
            <span><a href="/shiwenv_d0517d3dd0a0.aspx" target="_blank">淮村兵后</a>(戴复古)</span>
            <span><a href="/shiwenv_a31b957aba53.aspx" target="_blank">游园不值</a>(叶绍翁)</span>
            <span><a href="/shiwenv_e4df1367a39a.aspx" target="_blank">落梅</a>(刘克庄)</span>
            <span><a href="/shiwenv_92b73651b92d.aspx" target="_blank">莺梭</a>(刘克庄)</span>
            <span><a href="/shiwenv_e7dc6304c1d3.aspx" target="_blank">初夏游张园</a>(戴敏)</span>
            <span><a href="/shiwenv_745de66f357c.aspx" target="_blank">春暮</a>(曹豳)</span>
            <span><a href="/shiwenv_f20c6e290a03.aspx" target="_blank">绝句</a>(志南)</span>
            <span><a href="/shiwenv_5796865dca4a.aspx" target="_blank">过零丁洋</a>(文天祥)</span>
            <span><a href="/shiwenv_e0c2469a2834.aspx" target="_blank">二砺</a>(郑思肖)</span>
            <span><a href="/shiwenv_0a65b1091d79.aspx" target="_blank">画菊</a>(郑思肖)</span>
            <span><a href="/shiwenv_f89e91962a3d.aspx" target="_blank">寒夜</a>(杜耒)</span>
            <span><a href="/shiwenv_8f1be8b774c2.aspx" target="_blank">雪梅</a>((卢钺)</span>
            <span><a href="/shiwenv_cf40b2692a2f.aspx" target="_blank">武夷山中</a>(谢枋得)</span>
            <span><a href="/shiwenv_e814b38c37b1.aspx" target="_blank">月儿弯弯照九州</a>(南宋民歌)</span>
</div>
<div class="typecont">
            <div class="bookMl"><strong>五言绝句</strong></div>
            <span><a href="/shiwenv_ffc3de59f87e.aspx" target="_blank">绝句</a>(王庭筠)</span>
            <span><a href="/shiwenv_d2dc2bca986a.aspx" target="_blank">台山杂咏</a>(元好问)</span>
            <span><a href="/shiwenv_d4251de1d5c0.aspx" target="_blank">壬辰十二月车驾东狩后</a>(元好问)</span>
            <span><a href="/shiwenv_531487dfc924.aspx" target="_blank">同儿辈赋未开海棠</a>(元好问)</span>
            <span><a href="/shiwenv_3f9a52155e2c.aspx" target="_blank">博浪沙</a>(陈孚)</span>
            <span><a href="/shiwenv_5f1eaf0ead05.aspx" target="_blank">山家</a>(刘因)</span>
            <span><a href="/shiwenv_b985fd4c15a0.aspx" target="_blank">东城</a>(赵孟頫)</span>
            <span><a href="/shiwenv_625122d98389.aspx" target="_blank">临平泊舟</a>(黄庚)</span>
            <span><a href="/shiwenv_ba5e30db470e.aspx" target="_blank">到京师</a>(杨载)</span>
            <span><a href="/shiwenv_99593a1af00d.aspx" target="_blank">院中独坐</a>(虞集)</span>
            <span><a href="/shiwenv_cb181f3fe002.aspx" target="_blank">画鸭</a>(揭侯斯)</span>
            <span><a href="/shiwenv_82fd6027caf3.aspx" target="_blank">墨梅</a>(王冕)</span>
            <span><a href="/shiwenv_260765c38b55.aspx" target="_blank">湖上</a>(徐元杰)</span>
            <span><a href="/shiwenv_203cdd10d0ca.aspx" target="_blank">上京即事</a>(萨都刺)</span>
</div>
<div class="typecont">
<div class="bookMl"><strong>五言绝句</strong></div>
            <span><a href="/shiwenv_fb4403a7a32d.aspx" target="_blank">京师得家书</a>(袁凯)</span>
            <span><a href="/shiwenv_7424dbea4855.aspx" target="_blank">天平山中</a>(杨基)</span>
            <span><a href="/shiwenv_314cc9e53848.aspx" target="_blank">春暮西园</a>(高启)</span>
            <span><a href="/shiwenv_fd1900eea689.aspx" target="_blank">寻胡隐君</a>(高启)</span>
            <span><a href="/shiwenv_a9d80ed06ffb.aspx" target="_blank">春雁</a>(王恭)</span>
            <span><a href="/shiwenv_aacda5e3e84e.aspx" target="_blank">发淮安</a>(杨士奇)</span>
            <span><a href="/shiwenv_229a5d381d6b.aspx" target="_blank">幼女词</a>(毛铉)</span>
            <span><a href="/shiwenv_63077cbb00fd.aspx" target="_blank">乡人至夜话</a>(李昌祺)</span>
            <span><a href="/shiwenv_c6c93895df0a.aspx" target="_blank">石灰吟</a>(于谦)</span>
            <span><a href="/shiwenv_14df22a8fd7f.aspx" target="_blank">题画</a>(沈周)</span>
            <span><a href="/shiwenv_f55907b251d1.aspx" target="_blank">柯敬仲墨竹</a>(李东阳)</span>
            <span><a href="/shiwenv_49e33b2a997d.aspx" target="_blank">言志</a>(唐寅)</span>
            <span><a href="/shiwenv_ea6243da5680.aspx" target="_blank">船板床</a>(李梦阳)</span>
            <span><a href="/shiwenv_e0022a7b82a0.aspx" target="_blank">在武昌作</a>(徐祯卿)</span>
            <span><a href="/shiwenv_c2e9940be46c.aspx" target="_blank">重赠吴国宾</a>(边贡)</span>
            <span><a href="/shiwenv_fafdab6ae79c.aspx" target="_blank">竹枝词</a>(何景明)</span>
            <span><a href="/shiwenv_0f55933bda98.aspx" target="_blank">出郊</a>(杨慎)</span>
            <span><a href="/shiwenv_1407f7e38e46.aspx" target="_blank">塞下曲</a>(谢榛)</span>
            <span><a href="/shiwenv_2e3054d7d3e5.aspx" target="_blank">塞上曲送元美</a>(李攀龙)</span>
            <span><a href="/shiwenv_914f49b8c9c7.aspx" target="_blank">就义诗</a>(杨继盛)</span>
            <span><a href="/shiwenv_0b5697fbae9c.aspx" target="_blank">题《墨葡萄图》</a>(徐渭)</span>
            <span><a href="/shiwenv_b801aa227372.aspx" target="_blank">马上作</a>(戚继光)</span>
            <span><a href="/shiwenv_35fa981f06c2.aspx" target="_blank">今日诗</a>(文嘉)</span>
            <span><a href="/shiwenv_6676ea7453b1.aspx" target="_blank">枕石</a>(高攀龙)</span>
            <span><a href="/shiwenv_d913aa8c4790.aspx" target="_blank">感事</a>(袁宏道)</span>
            <span><a href="/shiwenv_c14f7d0c37b5.aspx" target="_blank">江宿</a>(汤显祖)</span>
            <span><a href="/shiwenv_72f7e33ff468.aspx" target="_blank">渡易水</a>(陈子龙)</span>
            <span><a href="/shiwenv_b30859eabc54.aspx" target="_blank">即事</a>(夏完淳)</span>
            <span><a href="/shiwenv_d01bc3fbb10b.aspx" target="_blank">别云间</a>(夏完淳)</span>
            <span><a href="/shiwenv_5ce52b5282ab.aspx" target="_blank">闯王</a>(明朝民歌)</span>
</div>
<div class="typecont" style="border:0px;">
<div class="bookMl"><strong>五言绝句</strong></div>
            <span><a href="/shiwenv_a1e9bca90dfa.aspx" target="_blank">阻雪</a>(吴伟业)</span>
            <span><a href="/shiwenv_a1dc95d15aa4.aspx" target="_blank">闻鹧鸪</a>(尤侗)</span>
            <span><a href="/shiwenv_de509b34e342.aspx" target="_blank">出居庸关</a>(朱彝尊)</span>
            <span><a href="/shiwenv_1eaa0ce953db.aspx" target="_blank">真州绝句</a>(王士祯)</span>
            <span><a href="/shiwenv_27f3f8b08e3b.aspx" target="_blank">过湖北山家</a>(施闰章)</span>
            <span><a href="/shiwenv_b227e24b2d70.aspx" target="_blank">自湘东驿遵陆至芦溪</a>(查慎行)</span>
            <span><a href="/shiwenv_d88e3533fc4a.aspx" target="_blank">舟夜书所见</a>(查慎行)</span>
            <span><a href="/shiwenv_5816326dac9a.aspx" target="_blank">过许州</a>(沈德潜)</span>
            <span><a href="/shiwenv_ef1ba2570ce3.aspx" target="_blank">秣陵怀古</a>(纳兰性德)</span>
            <span><a href="/shiwenv_b19f64f4a291.aspx" target="_blank">萤火</a>(赵执信)</span>
            <span><a href="/shiwenv_5a22c2d89bf3.aspx" target="_blank">灵隐寺月夜</a>(厉鹗)</span>
            <span><a href="/shiwenv_e5c9337524b7.aspx" target="_blank">竹石</a>(郑燮)</span>
            <span><a href="/shiwenv_ecc9acd2b27a.aspx" target="_blank">山中雪后</a>(郑燮)</span>
            <span><a href="/shiwenv_59e2882fc46b.aspx" target="_blank">渔家</a>(郑燮)</span>
            <span><a href="/shiwenv_93c121e175f6.aspx" target="_blank">偶然作</a>(屈复)</span>
            <span><a href="/shiwenv_9211704923ca.aspx" target="_blank">岁暮到家</a>(蒋士铨)</span>
            <span><a href="/shiwenv_bc1e52481a58.aspx" target="_blank">马嵬</a>(袁枚)</span>
            <span><a href="/shiwenv_4aa6ea82a0bf.aspx" target="_blank">夜过借园见主人坐月下吹笛</a>(袁枚)</span>
            <span><a href="/shiwenv_a1b1e11bc897.aspx" target="_blank">山行杂咏</a>(袁枚)</span>
            <span><a href="/shiwenv_58699ebb5e93.aspx" target="_blank">所见</a>(袁枚)</span>
            <span><a href="/shiwenv_81e6db75a7af.aspx" target="_blank">遣兴</a>(袁枚)</span>
            <span><a href="/shiwenv_632e1799e76c.aspx" target="_blank">富春至严陵山水甚佳</a>(纪昀)</span>
            <span><a href="/shiwenv_c1e5416e8000.aspx" target="_blank">论诗</a>(赵翼)</span>
            <span><a href="/shiwenv_781eea742277.aspx" target="_blank">山行</a>(姚鼐)</span>
            <span><a href="/shiwenv_01b3f00494ec.aspx" target="_blank">感旧</a>(黄景仁)</span>
            <span><a href="/shiwenv_5cc9bc00cc98.aspx" target="_blank">别老母</a>(黄景仁)</span>
            <span><a href="/shiwenv_75957e2a4d1e.aspx" target="_blank">咏史</a>(龚自珍)</span>
            <span><a href="/shiwenv_d78d2dc95f06.aspx" target="_blank">己亥杂诗·其五</a>(龚自珍)</span>
            <span><a href="/shiwenv_838d9b401572.aspx" target="_blank">己亥杂诗</a>(龚自珍)</span>
            <span><a href="/shiwenv_425fb837c387.aspx" target="_blank">村居</a>(高鼎)</span>
            <span><a href="/shiwenv_b6bd9a33dfd7.aspx" target="_blank">画</a>(王维)</span>
            <span><a href="/shiwenv_1aaed47f2347.aspx" target="_blank">春愁</a>(丘逢甲)</span>
            <span><a href="/shiwenv_5dd34a4d891c.aspx" target="_blank">狱中题壁</a>(谭嗣同)</span>
            <span><a href="/shiwenv_ebb65733f23d.aspx" target="_blank">读《陆放翁集》</a>(梁启超)</span>
            <span><a href="/shiwenv_685696a135e0.aspx" target="_blank">对酒</a>(秋瑾)</span>
            <span><a href="/shiwenv_ee377ff2e0cc.aspx" target="_blank">狱中赠邹容</a>(章炳麟)</span>
</div>
</div>


<div id="btmwx" style="clear:both; margin-top:20px; float:left; width:670px; background-color:#F0EFE2; height:auto;">
<script type="text/javascript" src="//enennsa.gushiwen.cn/site/n/production/ihk_kof/static/ee.js"></script>
</div>

<div id="threeWeixin" style="display:none;height: 100%;width: 100%;left: 0;top: 0;bottom: 0;position: fixed;background: rgba(0, 0, 0, 0.5);filter: alpha(opacity = 50);">
    <div class="hide-center" id="hide-center">
        <div id="formhead">
            <div id="formhead-title">
                <span style=" float:left; font-size:18px; margin-left:46px; margin-top:5px;">关注微信公众号</span>
                <span style=" float:left; clear:both; color:#999999; font-weight:normal; font-size:12px;margin-left:61px; margin-top:10px;">精选内容每周推送</span>
            </div>
            <button type="button" id="close">X</button>
        </div>
        <div id="formbody">
            <img id="erweimaCanshu" width="200" height="200" src="" alt="" />
        </div>
    </div>

</div>


<div id="threeWeixin2" style="display:none; height: 100%;width: 100%;left: 0;top: 0;bottom: 0;position: fixed;background: rgba(0, 0, 0, 0.5);filter: alpha(opacity = 50);">
    <div class="hide-center" id="hide-center2">
        <div id="formhead2">
            <div id="formhead-title2">
                <span style=" float:left; font-size:18px; margin-left:55px; margin-top:5px;">微信扫码登录</span>
                <span style=" float:left; clear:both; color:#999999; font-weight:normal; font-size:12px;margin-left:32px; margin-top:10px;">首次需关注公众号 |</span><a style="color:#999999; float:left; margin-left:5px; font-size:12px; font-weight:normal; margin-top:10px;" href="/user/login.aspx?from=http://so.gushiwen.cn/gushi/sanbai.aspx">账号登录</a>
            </div>
            <button type="button" id="close2">X</button>
        </div>
        <div id="formbody2">
            <img id="erweimaCanshu2" width="200" height="200" src="" alt="" />
        </div>
    </div>
</div>


<script type="text/javascript">
    //取得cookie值
    function getCookie(name) {
        var arr, reg = new RegExp("(^| )" + name + "=([^;]*)(;|$)");

        if (arr = document.cookie.match(reg))

            return unescape(arr[2]);
        else
            return null;
    }

    if (getCookie('gsw2017user') != null && getCookie('gsw2017user').split('|').length >= 3) {
        var userDate = getCookie('gsw2017user').split('|')[2];
        var myDate = new Date(userDate);
        var now = new Date();
        if (myDate >= now) {
            document.getElementById('btmwx').style.display = 'none';
        }
    }

    $("#close").click(function () {
        $("#threeWeixin").fadeOut("slow");
        clearInterval(intervalErweima);
        intervalErweima2 = null;
    })

    $("#close2").click(function () {
        $("#threeWeixin2").fadeOut("slow");
        clearInterval(intervalErweima2);
        intervalErweima2 = null;
    })
    var timesRun = 0;
    var scene_id = Math.floor((Math.random() * 9999999) + 200000000);

    //判断是否为登录用户但未关注公众号
    var wxopenid = getCookie('wxopenid');
    var gsw2017user = getCookie('gsw2017user');
    var threeWeixinID = document.getElementById('threeWeixin');
    var threeWeixin2ID = document.getElementById('threeWeixin2');
    var erweimaShow = 0;
    var intervalErweima = null;
    var intervalErweima2 = null;
    //wxopenid为空必然未提醒，提醒后1周内不再提醒。如果账号能保存，那么wxopenid必然能保存


    $("#html").click(function () {
        //仅改变定位
        if (threeWeixinID.style.display != 'none') {
            return;
        }
        else if (threeWeixin2ID.style.display != 'none') {
            return;
        }
        setTimeout(showErweima, 1000);
    })

    function showErweima() {
        if (document.hidden) {
            return;
        }

        if (gsw2017user != null && getCookie('login') != null && wxopenid == null && erweimaShow == 0) {

            //获取二维码
            var xmlhttp;
            if (window.XMLHttpRequest) {// code for IE7+, Firefox, Chrome, Opera, Safari
                xmlhttp = new XMLHttpRequest();
            }
            else {// code for IE6, IE5
                xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
            }
            xmlhttp.onreadystatechange = function () {
                if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
                    if (xmlhttp.responseText.length > 5) {
                        document.getElementById('erweimaCanshu').src = "https://mp.weixin.qq.com/cgi-bin/showqrcode?ticket=" + xmlhttp.responseText;


                        $("#threeWeixin").fadeIn("slow");
                        timesRun = 0;

                        //判断码是否被扫
                        intervalErweima = setInterval("selectErweima()", "3000");
                    }
                }
            }
            xmlhttp.open("GET", "/getTicket.aspx?scene_id=" + scene_id, false);
            xmlhttp.send();

        }
        else if (gsw2017user == null && getCookie('login') != null && erweimaShow == 0) {

            //获取二维码
            if (getCookie('ticketStr') != null && getCookie('ticketStr').indexOf("|") > 0) {
                var ticketStr = getCookie('ticketStr').split('|');
                scene_id = ticketStr[0];
                if (ticketStr[1].length > 5) {
                    document.getElementById('erweimaCanshu2').src = "https://mp.weixin.qq.com/cgi-bin/showqrcode?ticket=" + ticketStr[1];

                    $("#threeWeixin2").fadeIn("slow");
                    timesRun = 0;

                    //判断码是否被扫
                    intervalErweima2 = setInterval("selectErweima2()", "3000");
                }
            }
            else {
                var xmlhttp;
                if (window.XMLHttpRequest) {// code for IE7+, Firefox, Chrome, Opera, Safari
                    xmlhttp = new XMLHttpRequest();
                }
                else {// code for IE6, IE5
                    xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
                }
                xmlhttp.onreadystatechange = function () {
                    if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
                        if (xmlhttp.responseText.length > 5) {
                            document.getElementById('erweimaCanshu2').src = "https://mp.weixin.qq.com/cgi-bin/showqrcode?ticket=" + xmlhttp.responseText;

                            $("#threeWeixin2").fadeIn("slow");
                            timesRun = 0;

                            //判断码是否被扫
                            intervalErweima2 = setInterval("selectErweima2()", "3000");
                        }
                    }
                }
                xmlhttp.open("GET", "/getTicket.aspx?scene_id=" + scene_id, false);
                xmlhttp.send();
            }

        }
    }



    //判断码是否被扫
    function selectErweima2() {
        //60秒后停止
        timesRun = timesRun + 1;
        if (timesRun > 10) {
            $("#threeWeixin2").fadeOut("slow");

            clearInterval(intervalErweima2);
            intervalErweima2 = null;
        }

        //有二维码才查询自己数据库
        if (getCookie('ticketStr') != null && getCookie('ticketStr').indexOf("|") > 0) {
            var xmlhttp;
            if (window.XMLHttpRequest) {// code for IE7+, Firefox, Chrome, Opera, Safari
                xmlhttp = new XMLHttpRequest();
            }
            else {// code for IE6, IE5
                xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
            }
            xmlhttp.onreadystatechange = function () {
                if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
                    if (xmlhttp.responseText == "1") {
                        $("#threeWeixin2").fadeOut("slow");
                        erweimaShow = 1;
                        clearInterval(intervalErweima2);
                        intervalErweima2 = null;
                    }
                }
            }
            xmlhttp.open("POST", "/user/getEventLogin.aspx?&scene_id=" + scene_id, false);
            xmlhttp.send();
        }
    }

    function selectErweima() {
        //60秒后停止
        timesRun = timesRun + 1;
        if (timesRun > 10) {
            $("#threeWeixin").fadeOut("slow");
            clearInterval(intervalErweima);
            intervalErweima = null;
        }

        //有二维码才查询自己数据库
        if (getCookie('ticketStr') != null && getCookie('ticketStr').indexOf("|") > 0) {
            var xmlhttp;
            if (window.XMLHttpRequest) {// code for IE7+, Firefox, Chrome, Opera, Safari
                xmlhttp = new XMLHttpRequest();
            }
            else {// code for IE6, IE5
                xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
            }
            xmlhttp.onreadystatechange = function () {
                if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
                    if (xmlhttp.responseText != "未扫码") {

                        $("#threeWeixin").fadeOut("slow");
                        erweimaShow = 1;
                        clearInterval(intervalErweima);
                        intervalErweima = null;
                    }
                }
            }
            xmlhttp.open("POST", "/getEventKey.aspx?&scene_id=" + scene_id, false);
            xmlhttp.send();
        }
    }

</script>
    </div>
    <div class="right">
        <div class="sons">
        <div class="title">
        <div class="titleleft"></div>
            诗文
        </div>
<div class="cont">
    <a href="https://so.gushiwen.cn/gushi/tangshi.aspx">唐诗三百</a>
    <a href="https://so.gushiwen.cn/gushi/sanbai.aspx">古诗三百</a>
    <a href="https://so.gushiwen.cn/gushi/songsan.aspx">宋词三百</a>
    <a href="https://so.gushiwen.cn/gushi/xiaoxue.aspx">小学古诗</a>
    <a href="https://so.gushiwen.cn/gushi/chuzhong.aspx">初中古诗</a>
    <a href="https://so.gushiwen.cn/gushi/gaozhong.aspx">高中古诗</a>
    <a href="https://so.gushiwen.cn/wenyan/xiaowen.aspx">小学文言</a>
    <a href="https://so.gushiwen.cn/wenyan/chuwen.aspx">初中文言</a>
    <a href="https://so.gushiwen.cn/wenyan/gaowen.aspx">高中文言</a>
    <a href="https://so.gushiwen.cn/gushi/songci.aspx">宋词精选</a>
    <a href="https://so.gushiwen.cn/gushi/shijiu.aspx">古诗十九</a>
    <a href="https://so.gushiwen.cn/gushi/shijing.aspx">诗经</a>
    <a href="https://so.gushiwen.cn/gushi/chuci.aspx">楚辞</a>
    <a href="https://so.gushiwen.cn/gushi/yuefu.aspx">乐府</a>
    <a href="https://so.gushiwen.cn/gushi/xiejing.aspx">写景</a>
    <a href="/gushi/yongwu.aspx">咏物</a>
    <a href="/gushi/chuntian.aspx">春天</a>
    <a href="/gushi/xiatian.aspx">夏天</a>
    <a href="/gushi/qiutian.aspx">秋天</a>
    <a href="/gushi/dongtian.aspx">冬天</a>
    <a href="/gushi/yu.aspx">写雨</a>
    <a href="/gushi/xue.aspx">写雪</a>
    <a href="/gushi/feng.aspx">写风</a>
    <a href="/gushi/hua.aspx">写花</a>
    <a href="/gushi/meihua.aspx">梅花</a>
    <a href="/gushi/hehua.aspx">荷花</a>
    <a href="/gushi/juhua.aspx">菊花</a>
    <a href="/gushi/liushu.aspx">柳树</a>
    <a href="/gushi/yueliang.aspx">月亮</a>
    <a href="/gushi/shanshui.aspx">山水</a>
    <a href="/gushi/shan.aspx">写山</a>
    <a href="/gushi/shui.aspx">写水</a>
    <a href="/gushi/changjiang.aspx">长江</a>
    <a href="/gushi/huanghe.aspx">黄河</a>
    <a href="/gushi/ertong.aspx">儿童</a>
    <a href="/gushi/niao.aspx">写鸟</a>
    <a href="/gushi/ma.aspx">写马</a>
    <a href="/gushi/tianyuan.aspx">田园</a>
    <a href="/gushi/biansai.aspx">边塞</a>
    <a href="/gushi/diming.aspx">地名</a>
    <a href="/gushi/jieri.aspx">节日</a>
    <a href="/gushi/chunjie.aspx">春节</a>
    <a href="/gushi/yuanxiao.aspx">元宵</a>
    <a href="/gushi/hanshi.aspx">寒食</a>
    <a href="/gushi/qingming.aspx">清明</a>
    <a href="/gushi/duanwu.aspx">端午</a>
    <a href="/gushi/qixi.aspx">七夕</a>
    <a href="/gushi/zhongqiu.aspx">中秋</a>
    <a href="/gushi/chongyang.aspx">重阳</a>
    <a href="/gushi/huaigu.aspx">怀古</a>
    <a href="/gushi/shuqing.aspx">抒情</a>
    <a href="/gushi/aiguo.aspx">爱国</a>
    <a href="/gushi/libie.aspx">离别</a>
    <a href="/gushi/songbie.aspx">送别</a>
    <a href="/gushi/sixiang.aspx">思乡</a>
    <a href="/gushi/sinian.aspx">思念</a>
    <a href="/gushi/aiqing.aspx">爱情</a>
    <a href="/gushi/lizhi.aspx">励志</a>
    <a href="/gushi/zheli.aspx">哲理</a>
    <a href="/gushi/guiyuan.aspx">闺怨</a>
    <a href="/gushi/daowang.aspx">悼亡</a>
    <a href="/gushi/xieren.aspx">写人</a>
    <a href="/gushi/laoshi.aspx">老师</a>
    <a href="/gushi/muqin.aspx">母亲</a>
    <a href="/gushi/youqing.aspx">友情</a>
    <a href="/gushi/zhanzheng.aspx">战争</a>
    <a href="/gushi/dushu.aspx">读书</a>
    <a href="/gushi/xishi.aspx">惜时</a>
    <a href="/gushi/youguo.aspx">忧民</a>
    <a href="/gushi/wanyue.aspx">婉约</a>
    <a href="/gushi/haofang.aspx">豪放</a>
    <a href="/gushi/minyao.aspx">民谣</a>
    
    
    
    <a href="/wenyan/guanzhi.aspx">古文观止</a>
    <a href="https://so.gushiwen.cn/shiwens/">更多>></a>
</div>
</div>
                <div class="abcd">
            
<script type="text/javascript" src="//enennsa.gushiwen.cn/common/r/openjs/m_lj/source/o/static/seou.js"></script>
        </div>
        <div class="juzioncont">
          <img style=" float:left; margin:10px; margin-right:0px;" src="https://song.gushiwen.cn/siteimg/app/appdown.png" width="80" height="80" /><p><center style="font-size:18px; margin-top:14px;">扫码下载</center></p><p><center style="font-size:18px; margin-top:5px;">古诗文网客户端</center></p>
        </div>
        <div class="abcd">
            
<script type="text/javascript" src="//enennsa.gushiwen.cn/common/ql_kinrd_n/n.js"></script>
        </div>
        <div class="juzioncont">
          <img style=" float:left; margin:10px; margin-right:0px;" src="https://song.gushiwen.cn/siteimg/app/erma_guwendao.png" width="80" height="80" /><p><center style="font-size:18px; margin-top:14px;">扫码关注</center></p><p><center style="font-size:18px;margin-top:5px;">古文岛主公众号</center></p>
        </div>
        <div class="abcd">
            
<script type="text/javascript" src="//enennsa.gushiwen.cn/source/jed/static/b_gkw_m_k.js"></script>
        </div>
    </div>
</div>




<div class="main4">
    © 2023 <a href="https://www.gushiwen.cn/">古诗文网</a> | <a href="https://so.gushiwen.cn/shiwens/">诗文</a> | <a href="https://so.gushiwen.cn/mingjus/">名句</a> | <a href="https://so.gushiwen.cn/authors/">作者</a> | <a href="https://so.gushiwen.cn/guwen/">古籍</a> | <a href="/jiucuo.aspx?u=" target="_blank" rel="nofollow">纠错</a>
</div>


<script type="text/javascript">
    window.onload = function () {
        setIframeHeight(document.getElementById('external-frame'));
    };
    if (getCookie('gsw2017user') != null && getCookie('gsw2017user').split('|').length >= 3) {
        var userDate = getCookie('gsw2017user').split('|')[2];
        var myDate = new Date(userDate);
        var now = new Date();
        if (myDate >= now) {
            for (var i = 0; i < document.getElementsByClassName("abcd").length; i++) {
                document.getElementsByClassName("abcd")[i].style.display = 'none';
            }
        }
    }
</script>

<script defer="defer" src="/js/skinso20220717.js" type="text/javascript"></script>
</body>
</html>

    '''
    resp = HtmlResponse(
        url='https://so.gushiwen.cn/gushi/sanbai.aspx', body=html_body, encoding='utf8')

    sel = resp.selector.css(".left .typecont a")
    assert len(sel.xpath("@href").getall()) > 0
    assert len(sel.xpath("@href").getall()
               ) == len(sel.xpath("text()").getall())
    assert sel.xpath("text()").getall()[:3] == ['击壤歌', '关雎', '木瓜']

    sel = resp.selector.css(".right .cont a")
    assert len(sel.xpath("@href").getall()) > 0
    assert len(sel.xpath("@href").getall()
               ) == len(sel.xpath("text()").getall())
    assert sel.xpath("text()").getall()[:3] == ['唐诗三百', '古诗三百', '宋词三百']
