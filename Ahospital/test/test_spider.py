from ..Ahospital.spiders.spider import HospitalSpider
from ..Ahospital.pipelines import AhospitalPipeline
from ..Ahospital.items import AhospitalItem

import scrapy
from scrapy.http import HtmlResponse
from scrapy import Request
# test the director page
def test_spider1():
    body = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html lang="zh-hans" dir="ltr">
<head>
<title>常见化验指标及意义 - A+医学百科</title>
<meta name="viewport" content="width=device-width, initial-scale=1" />
<meta name="applicable-device" content="pc,mobile" />
<meta http-equiv="Cache-Control" content="no-transform" />
<meta http-equiv="Cache-Control" content="no-siteapp" />
<meta name="generator" content="MediaWiki 1.16.0" />
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<link rel="apple-touch-icon" href="http://s.ayxbk.com/common/images/apple-touch-icon.png" />
<link rel="shortcut icon" href="http://s.ayxbk.com/favicon.ico" />
<link rel="search" type="application/opensearchdescription+xml" href="/opensearch_desc.php" title="A+医学百科 (zh-hans)" />
<link rel="copyright" href="/w/A%2B%E5%8C%BB%E5%AD%A6%E7%99%BE%E7%A7%91:%E7%89%88%E6%9D%83" />
<link rel="stylesheet" href="http://s.ayxbk.com/vector/main-mini.css?278" media="screen" />

</head>
<body class="mediawiki ltr ns-0 ns-subject page-常见化验指标及意义 skin-vector">
		<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
		<script>
		     (adsbygoogle = window.adsbygoogle || []).push({
		          google_ad_client: "ca-pub-4174070858627065",
		          enable_page_level_ads: true
		     });
		</script>
		<div id="mw-page-base" class="noprint"></div>
		<div id="mw-head-base" class="noprint"></div>
		<!-- content -->
		<div id="content" >
			<a id="top"></a>
			<div id="mw-js-message" style="display:none;"></div>
						<!-- firstHeading -->
			<h1 id="firstHeading" class="firstHeading">常见化验指标及意义</h1>
			<!-- /firstHeading -->
			<!-- bodyContent -->
			<div id="bodyContent">
				<!-- subtitle -->
				<div id="contentSub"></div>
				<!-- /subtitle -->
																<!-- jumpto -->
				<div id="jump-to-nav">
					跳转到： <a href="#mw-head">导航</a>,
					<a href="#p-search">搜索</a>
				</div>
				<!-- /jumpto -->
								<!-- bodytext -->
				<table class="nav">

<tr>
<td><a href="/w/%E9%A6%96%E9%A1%B5" title="首页">A+医学百科</a> &gt;&gt; 常见化验指标及意义
</td></tr></table>
<p><a href="/w/%E8%A1%80%E6%B6%B2%E4%B8%80%E8%88%AC%E6%A3%80%E6%9F%A5" title="血液一般检查">血液一般检查</a></p>
<ul>
<li><a href="/w/%E7%99%BD%E7%BB%86%E8%83%9E%E5%88%86%E7%B1%BB%E8%AE%A1%E6%95%B0" title="白细胞分类计数">白细胞分类计数</a>（<a href="/w/DC" title="DC" class="mw-redirect">DC</a>)</li>
<li><a href="/w/%E5%97%9C%E9%85%B8%E6%80%A7%E7%B2%92%E7%BB%86%E8%83%9E%E7%9B%B4%E6%8E%A5%E8%AE%A1%E6%95%B0" title="嗜酸性粒细胞直接计数">嗜酸性粒细胞直接计数</a>（<a href="/w/EOS" title="EOS" class="mw-redirect">EOS</a>)</li>
<li><a href="/w/%E8%A1%80%E5%B8%B8%E8%A7%84" title="血常规" class="mw-redirect">血常规</a>
<ul>
<li><a href="/w/%E7%BA%A2%E7%BB%86%E8%83%9E" title="红细胞">红细胞</a>（<a href="/w/RBC" title="RBC" class="mw-redirect">RBC</a>)</li>
<li><a href="/w/%E8%A1%80%E7%BA%A2%E8%9B%8B%E7%99%BD" title="血红蛋白">血红蛋白</a>（<a href="/w/Hb" title="Hb" class="mw-redirect">Hb</a>)</li>
<li><a href="/w/%E7%99%BD%E7%BB%86%E8%83%9E" title="白细胞">白细胞</a>（<a href="/w/WBC" title="WBC" class="mw-redirect">WBC</a>)</li>
</ul>
</li>
<li><a href="/w/%E8%A1%80%E6%B2%89" title="血沉">血沉</a>（<a href="/w/ESR" title="ESR" class="mw-redirect">ESR</a>)</li>
</ul>
<table id="toc" class="toc">
<tr>
<td>
<div id="toctitle">
<h2>目录</h2>
</div>
<ul>
<li class="toclevel-1 tocsection-1"><a href="#.E5.B0.BF.E6.B6.B2.E6.A3.80.E6.9F.A5"><span class="tocnumber">1</span> <span class="toctext">尿液检查</span></a></li>
<li class="toclevel-1 tocsection-2"><a href="#.E7.B2.AA.E4.BE.BF.E6.A3.80.E6.9F.A5"><span class="tocnumber">2</span> <span class="toctext">粪便检查</span></a></li>
<li class="toclevel-1 tocsection-3"><a href="#.E8.82.9D.E7.82.8E.E7.97.85.E6.AF.92.E8.A1.80.E6.B8.85.E5.AD.A6.E6.A0.87.E8.AE.B0"><span class="tocnumber">3</span> <span class="toctext">肝炎病毒血清学标记</span></a></li>
<li class="toclevel-1 tocsection-4"><a href="#.E6.B0.A8.E5.9F.BA.E9.85.B8.E5.8F.8A.E5.85.B6.E4.BB.A3.E8.B0.A2.E4.BA.A7.E7.89.A9"><span class="tocnumber">4</span> <span class="toctext">氨基酸及其代谢产物</span></a></li>
<li class="toclevel-1 tocsection-5"><a href="#.E5.9E.82.E4.BD.93.E6.BF.80.E7.B4.A0.E6.A3.80.E6.B5.8B"><span class="tocnumber">5</span> <span class="toctext">垂体激素检测</span></a></li>
<li class="toclevel-1 tocsection-6"><a href="#.E8.83.86.E8.89.B2.E7.B4.A0.E6.A3.80.E6.9F.A5"><span class="tocnumber">6</span> <span class="toctext">胆色素检查</span></a></li>
<li class="toclevel-1 tocsection-7"><a href="#.E8.9B.8B.E7.99.BD.E8.B4.A8.E6.B5.8B.E5.AE.9A"><span class="tocnumber">7</span> <span class="toctext">蛋白质测定</span></a></li>
<li class="toclevel-1 tocsection-8"><a href="#.E8.9B.8B.E7.99.BD.E8.B4.A8.E5.8F.8A.E6.B0.A8.E7.9A.84.E6.B5.8B.E5.AE.9A"><span class="tocnumber">8</span> <span class="toctext">蛋白质及氨的测定</span></a></li>
<li class="toclevel-1 tocsection-9"><a href="#.E9.AA.A8.E9.AB.93.E7.BB.86.E8.83.9E.E5.AD.A6.E6.A3.80.E6.9F.A5"><span class="tocnumber">9</span> <span class="toctext">骨髓细胞学检查</span></a></li>
<li class="toclevel-1 tocsection-10"><a href="#.E7.94.B2.E7.8A.B6.E6.97.81.E8.85.BA.E5.8A.9F.E8.83.BD.E6.A3.80.E6.B5.8B"><span class="tocnumber">10</span> <span class="toctext">甲状旁腺功能检测</span></a></li>
<li class="toclevel-1 tocsection-11"><a href="#.E7.94.B2.E7.8A.B6.E8.85.BA.E5.8A.9F.E8.83.BD.E6.A3.80.E6.B5.8B"><span class="tocnumber">11</span> <span class="toctext">甲状腺功能检测</span></a></li>
<li class="toclevel-1 tocsection-12"><a href="#.E6.B5.86.E8.86.9C.E8.85.94.E7.A9.BF.E5.88.BA.E6.B6.B2.E6.A3.80.E6.9F.A5"><span class="tocnumber">12</span> <span class="toctext">浆膜腔穿刺液检查</span></a></li>
<li class="toclevel-1 tocsection-13"><a href="#.E7.B2.BE.E6.B6.B2.E6.A3.80.E6.9F.A5"><span class="tocnumber">13</span> <span class="toctext">精液检查</span></a></li>
<li class="toclevel-1 tocsection-14"><a href="#.E9.85.B6.E7.B1.BB.E6.B5.8B.E5.AE.9A"><span class="tocnumber">14</span> <span class="toctext">酶类测定</span></a></li>
<li class="toclevel-1 tocsection-15"><a href="#.E5.85.8D.E7.96.AB.E5.AD.A6.E6.A3.80.E9.AA.8C"><span class="tocnumber">15</span> <span class="toctext">免疫学检验</span></a></li>
<li class="toclevel-1 tocsection-16"><a href="#.E8.84.91.E8.84.8A.E6.B6.B2.E6.A3.80.E6.9F.A5"><span class="tocnumber">16</span> <span class="toctext">脑脊液检查</span></a></li>
<li class="toclevel-1 tocsection-17"><a href="#.E8.B4.AB.E8.A1.80.E7.9A.84.E5.85.B6.E4.BB.96.E6.A3.80.E6.9F.A5"><span class="tocnumber">17</span> <span class="toctext">贫血的其他检查</span></a></li>
<li class="toclevel-1 tocsection-18"><a href="#.E5.85.B6.E4.BB.96.E6.BF.80.E7.B4.A0.E5.8F.8A.E5.85.B6.E4.BB.A3.E8.B0.A2.E7.89.A9"><span class="tocnumber">18</span> <span class="toctext">其他激素及其代谢物</span></a></li>
<li class="toclevel-1 tocsection-19"><a href="#.E5.89.8D.E5.88.97.E8.85.BA.E6.B6.B2.E6.A3.80.E6.9F.A5"><span class="tocnumber">19</span> <span class="toctext">前列腺液检查</span></a></li>
<li class="toclevel-1 tocsection-20"><a href="#.E8.82.BE.E5.8A.9F.E8.83.BD"><span class="tocnumber">20</span> <span class="toctext">肾功能</span></a></li>
<li class="toclevel-1 tocsection-21"><a href="#.E8.82.BE.E4.B8.8A.E8.85.BA.E5.8A.9F.E8.83.BD.E6.A3.80.E6.B5.8B"><span class="tocnumber">21</span> <span class="toctext">肾上腺功能检测</span></a></li>
<li class="toclevel-1 tocsection-22"><a href="#.E7.97.B0.E6.B6.B2.E6.A3.80.E6.9F.A5"><span class="tocnumber">22</span> <span class="toctext">痰液检查</span></a></li>
<li class="toclevel-1 tocsection-23"><a href="#.E7.B3.96.E7.B1.BB.E5.8F.8A.E5.85.B6.E4.BB.A3.E8.B0.A2.E4.BA.A7.E7.89.A9"><span class="tocnumber">23</span> <span class="toctext">糖类及其代谢产物</span></a></li>
<li class="toclevel-1 tocsection-24"><a href="#.E5.BE.AE.E9.87.8F.E5.85.83.E7.B4.A0.E6.B5.8B.E5.AE.9A"><span class="tocnumber">24</span> <span class="toctext">微量元素测定</span></a></li>
<li class="toclevel-1 tocsection-25"><a href="#.E7.BB.86.E8.83.9E.E7.BB.84.E7.BB.87.E5.8C.96.E5.AD.A6.E6.9F.93.E8.89.B2"><span class="tocnumber">25</span> <span class="toctext">细胞组织化学染色</span></a></li>
<li class="toclevel-1 tocsection-26"><a href="#.E6.80.A7.E8.85.BA.E6.BF.80.E7.B4.A0.E6.A3.80.E6.B5.8B"><span class="tocnumber">26</span> <span class="toctext">性腺激素检测</span></a></li>
<li class="toclevel-1 tocsection-27"><a href="#.E8.83.B0.E5.B2.9B.E5.8A.9F.E8.83.BD.E6.A3.80.E6.B5.8B"><span class="tocnumber">27</span> <span class="toctext">胰岛功能检测</span></a></li>
<li class="toclevel-1 tocsection-28"><a href="#.E9.98.B4.E9.81.93.E5.88.86.E6.B3.8C.E7.89.A9.E6.A3.80.E6.9F.A5"><span class="tocnumber">28</span> <span class="toctext">阴道分泌物检查</span></a></li>
<li class="toclevel-1 tocsection-29"><a href="#.E8.84.82.E7.B1.BB.E5.92.8C.E8.BD.BD.E8.84.82.E8.9B.8B.E7.99.BD.E6.B5.8B.E5.AE.9A"><span class="tocnumber">29</span> <span class="toctext">脂类和载脂蛋白测定</span></a></li>
<li class="toclevel-1 tocsection-30"><a href="#.E6.AD.A2.E8.A1.80.E4.B8.8E.E5.87.9D.E8.A1.80.E9.9A.9C.E7.A2.8D.E6.A3.80.E6.9F.A5"><span class="tocnumber">30</span> <span class="toctext">止血与凝血障碍检查</span></a></li>
<li class="toclevel-1"><a href="#.E6.80.8E.E6.A0.B7.E7.9C.8B.E5.8C.96.E9.AA.8C.E5.8D.95.E4.B8.93.E9.A2.98"><span class="tocnumber">31</span> <span class="toctext">怎样看化验单专题</span></a></li>
</ul>
</td>
</tr>
</table>
<script type="text/javascript">
//<![CDATA[
if (window.showTocToggle) { var tocShowText = "显示"; var tocHideText = "隐藏"; showTocToggle(); } 
//]]>
</script>
<h2><span class="mw-headline" id=".E5.B0.BF.E6.B6.B2.E6.A3.80.E6.9F.A5">尿液检查</span></h2>
<p><a href="/w/%E5%B0%BF%E6%B6%B2%E6%A3%80%E6%9F%A5" title="尿液检查" class="mw-redirect">尿液检查</a></p>
<ul>
<li><a href="/w/%E9%85%9A%E7%BA%A2%E6%8E%92%E6%B3%84%E8%AF%95%E9%AA%8C" title="酚红排泄试验">酚红排泄试验</a>（<a href="/w/PSP%E8%AF%95%E9%AA%8C" title="PSP试验" class="mw-redirect">PSP试验</a>)</li>
<li><a href="/w/%E6%94%B9%E8%89%AF%E8%8E%AB%E6%B0%8F%E6%B5%93%E7%BC%A9%E2%80%94%E2%80%94%E7%A8%80%E9%87%8A%E8%AF%95%E9%AA%8C" title="改良莫氏浓缩——稀释试验">改良莫氏浓缩——稀释试验</a></li>
<li><a href="/w/%E5%B0%BF%E6%AF%94%E9%87%8D" title="尿比重">尿比重</a></li>
<li><a href="/w/%E5%B0%BF%E6%B2%89%E6%B8%A3%E6%98%BE%E5%BE%AE%E9%95%9C%E6%A3%80%E6%9F%A5" title="尿沉渣显微镜检查">尿沉渣显微镜检查</a></li>
<li><a href="/w/%E5%B0%BF%E8%83%86%E7%BA%A2%E7%B4%A0%E8%AF%95%E9%AA%8C" title="尿胆红素试验">尿胆红素试验</a></li>
<li><a href="/w/%E5%B0%BF%E8%83%86%E5%8E%9F" title="尿胆原">尿胆原</a>（<a href="/w/UU" title="UU" class="mw-redirect">UU</a>)</li>
<li><a href="/w/%E5%B0%BF%E5%A6%8A%E5%A8%A0%E6%B5%93%E7%BC%A9%E8%AF%95%E9%AA%8C" title="尿妊娠浓缩试验">尿妊娠浓缩试验</a></li>
<li><a href="/w/%E5%B0%BF%E5%A6%8A%E5%A8%A0%E8%AF%95%E9%AA%8C" title="尿妊娠试验">尿妊娠试验</a></li>
<li><a href="/w/%E5%B0%BF%E4%B9%B3%E7%B3%9C%E8%AF%95%E9%AA%8C" title="尿乳糜试验">尿乳糜试验</a></li>
<li><a href="/w/%E5%B0%BF%E4%B8%89%E6%9D%AF%E8%AF%95%E9%AA%8C" title="尿三杯试验">尿三杯试验</a></li>
<li><a href="/w/%E5%B0%BF%E9%85%AE%E4%BD%93%E8%AF%95%E9%AA%8C" title="尿酮体试验">尿酮体试验</a>（<a href="/w/UABT" title="UABT" class="mw-redirect">UABT</a>)</li>
<li><a href="/w/%E5%B0%BF%E6%B6%B2%E6%A3%80%E6%9F%A5" title="尿液检查" class="mw-redirect">尿液检查</a>
<ul>
<li><a href="/w/%E5%B0%BF%E9%87%8F" title="尿量">尿量</a>（<a href="/w/UV" title="UV">UV</a>)</li>
<li><a href="/w/%E5%B0%BF%E6%B6%B2%E9%A2%9C%E8%89%B2" title="尿液颜色">尿液颜色</a></li>
<li><a href="/w/%E5%B0%BF%E6%B6%B2%E6%B0%94%E5%91%B3" title="尿液气味">尿液气味</a></li>
<li><a href="/w/%E5%B0%BF%E8%9B%8B%E7%99%BD" title="尿蛋白">尿蛋白</a></li>
<li><a href="/w/%E5%B0%BF%E7%B3%96" title="尿糖">尿糖</a>（<a href="/w/UGlu" title="UGlu" class="mw-redirect">UGlu</a>)</li>
<li><a href="/w/%E5%B0%BF17%EF%BC%8D%E9%85%AE%E7%B1%BB%E5%9B%BA%E9%86%87" title="尿17－酮类固醇">尿17－酮类固醇</a>（<a href="/w/17-KS" title="17-KS" class="mw-redirect">17-KS</a>)</li>
<li><a href="/w/%E5%B0%BF12%E5%B0%8F%E6%97%B6%E6%B2%89%E6%B8%A3%E8%AE%A1%E6%95%B0" title="尿12小时沉渣计数">尿12小时沉渣计数</a></li>
<li><a href="/w/%E5%B0%BF%E7%BA%A2%E7%BB%86%E8%83%9E" title="尿红细胞">尿红细胞</a>（12小时)</li>
<li><a href="/w/%E7%99%BD%E7%BB%86%E8%83%9E%E5%8F%8A%E4%B8%8A%E7%9A%AE%E7%BB%86%E8%83%9E" title="白细胞及上皮细胞">白细胞及上皮细胞</a></li>
</ul>
</li>
<li><a href="/w/%E5%B0%BF%E6%B6%B2%E9%85%B8%E7%A2%B1%E5%8F%8D%E5%BA%94" title="尿液酸碱反应">尿液酸碱反应</a>（<a href="/w/%E5%B0%BFPH%E5%80%BC" title="尿PH值" class="mw-redirect">尿PH值</a>)</li>
<li><a href="/w/%E5%B0%BF%E6%B6%B2%E8%87%AA%E5%8A%A8%E5%88%86%E6%9E%90%E4%BB%AAMA-4210%E5%9E%8B%E6%B5%8B%E5%AE%9A" title="尿液自动分析仪MA-4210型测定">尿液自动分析仪MA-4210型测定</a></li>
<li><a href="/w/%E5%B0%BF%E9%9A%90%E8%A1%80%E8%AF%95%E9%AA%8C" title="尿隐血试验">尿隐血试验</a></li>
</ul>
<h2><span class="mw-headline" id=".E7.B2.AA.E4.BE.BF.E6.A3.80.E6.9F.A5">粪便检查</span></h2>
<p><a href="/w/%E7%B2%AA%E4%BE%BF%E6%A3%80%E6%9F%A5" title="粪便检查">粪便检查</a></p>
<ul>
<li><a href="/w/%E7%B2%AA%E5%AF%84%E7%94%9F%E8%99%AB" title="粪寄生虫">粪寄生虫</a></li>
<li><a href="/w/%E7%B2%AA%E4%B8%AD%E9%9E%AD%E6%AF%9B%E8%99%AB%E5%8F%8A%E7%BA%A4%E6%AF%9B%E8%99%AB" title="粪中鞭毛虫及纤毛虫">粪中鞭毛虫及纤毛虫</a></li>
<li><a href="/w/%E7%B2%AA%E4%B8%AD%E5%8E%9F%E8%99%AB" title="粪中原虫">粪中原虫</a></li>
</ul>
<h2><span class="mw-headline" id=".E8.82.9D.E7.82.8E.E7.97.85.E6.AF.92.E8.A1.80.E6.B8.85.E5.AD.A6.E6.A0.87.E8.AE.B0">肝炎病毒血清学标记</span></h2>
<p><a href="/index.php?title=%E8%82%9D%E7%82%8E%E7%97%85%E6%AF%92%E8%A1%80%E6%B8%85%E5%AD%A6%E6%A0%87%E8%AE%B0&amp;action=edit&amp;redlink=1" class="new" title="肝炎病毒血清学标记（尚未撰写）" rel="nofollow">肝炎病毒血清学标记</a></p>
<ul>
<li><a href="/index.php?title=%E8%82%9D%E7%82%8E%E7%97%85%E6%AF%92%E8%A1%80%E6%B8%85%E6%A0%87%E8%AE%B0&amp;action=edit&amp;redlink=1" class="new" title="肝炎病毒血清标记（尚未撰写）" rel="nofollow">肝炎病毒血清标记</a>
<ul>
<li><a href="/w/%E4%B9%99%E5%9E%8B%E8%82%9D%E7%82%8E%E8%A1%A8%E9%9D%A2%E6%8A%97%E5%8E%9F" title="乙型肝炎表面抗原" class="mw-redirect">乙型肝炎表面抗原</a>（<a href="/w/HBsAg" title="HBsAg" class="mw-redirect">HBsAg</a>)</li>
<li><a href="/w/%E4%B9%99%E5%9E%8B%E8%82%9D%E7%82%8E%E8%A1%A8%E9%9D%A2%E6%8A%97%E4%BD%93" title="乙型肝炎表面抗体">乙型肝炎表面抗体</a>（<a href="/w/HBsAb" title="HBsAb" class="mw-redirect">HBsAb</a>)</li>
<li><a href="/w/%E4%B9%99%E5%9E%8B%E8%82%9D%E7%82%8Ee%E6%8A%97%E5%8E%9F" title="乙型肝炎e抗原">乙型肝炎e抗原</a>（<a href="/w/HBeAg" title="HBeAg" class="mw-redirect">HBeAg</a>)</li>
<li><a href="/w/%E4%B9%99%E5%9E%8B%E8%82%9D%E7%82%8Ee%E6%8A%97%E4%BD%93" title="乙型肝炎e抗体">乙型肝炎e抗体</a>〔<a href="/w/HBeAb" title="HBeAb" class="mw-redirect">HBeAb</a>〕</li>
<li><a href="/w/%E4%B9%99%E5%9E%8B%E8%82%9D%E7%82%8E%E6%A0%B8%E5%BF%83%E6%8A%97%E4%BD%93" title="乙型肝炎核心抗体">乙型肝炎核心抗体</a>（<a href="/w/HBcAb" title="HBcAb" class="mw-redirect">HBcAb</a>)</li>
<li><a href="/w/%E4%B9%99%E5%9E%8B%E8%82%9D%E7%82%8E%E6%A0%B8%E5%BF%83%E6%8A%97%E4%BD%93IgM" title="乙型肝炎核心抗体IgM">乙型肝炎核心抗体IgM</a>和<a href="/w/%E4%B9%99%E5%9E%8B%E8%82%9D%E7%82%8E%E6%A0%B8%E5%BF%83%E6%8A%97%E4%BD%93IgG" title="乙型肝炎核心抗体IgG">乙型肝炎核心抗体IgG</a>（<a href="/w/HBc-IgM" title="HBc-IgM" class="mw-redirect">HBc-IgM</a>和<a href="/w/HBc-IgG" title="HBc-IgG" class="mw-redirect">HBc-IgG</a>)</li>
<li><a href="/w/%E4%B8%81%E5%9E%8B%E8%82%9D%E7%82%8E%E6%8A%97%E5%8E%9F" title="丁型肝炎抗原">丁型肝炎抗原</a>（<a href="/w/HDAg" title="HDAg" class="mw-redirect">HDAg</a>)</li>
<li><a href="/w/%E4%B8%81%E5%9E%8B%E8%82%9D%E7%82%8E%E6%8A%97%E4%BD%93" title="丁型肝炎抗体">丁型肝炎抗体</a>（<a href="/w/HDAb" title="HDAb" class="mw-redirect">HDAb</a>)</li>
<li><a href="/w/%E7%94%B2%E5%9E%8B%E8%82%9D%E7%82%8E%E6%8A%97%E4%BD%93IgM" title="甲型肝炎抗体IgM">甲型肝炎抗体IgM</a>和<a href="/w/%E7%94%B2%E5%9E%8B%E8%82%9D%E7%82%8E%E6%8A%97%E4%BD%93IgG" title="甲型肝炎抗体IgG">甲型肝炎抗体IgG</a>（<a href="/w/HAVIgM" title="HAVIgM" class="mw-redirect">HAVIgM</a>和<a href="/w/HAVIgG" title="HAVIgG" class="mw-redirect">HAVIgG</a>)</li>
</ul>
</li>
</ul>
<h2><span class="mw-headline" id=".E6.B0.A8.E5.9F.BA.E9.85.B8.E5.8F.8A.E5.85.B6.E4.BB.A3.E8.B0.A2.E4.BA.A7.E7.89.A9">氨基酸及其代谢产物</span></h2>
<p><a href="/index.php?title=%E6%B0%A8%E5%9F%BA%E9%85%B8%E5%8F%8A%E5%85%B6%E4%BB%A3%E8%B0%A2%E4%BA%A7%E7%89%A9&amp;action=edit&amp;redlink=1" class="new" title="氨基酸及其代谢产物（尚未撰写）" rel="nofollow">氨基酸及其代谢产物</a></p>
<ul>
<li><a href="/w/%E8%A1%80%E6%B8%85%E5%B0%BF%E9%85%B8" title="血清尿酸">血清尿酸</a>（<a href="/w/%E8%A1%80%E6%B5%86%E5%B0%BF%E9%85%B8" title="血浆尿酸" class="mw-redirect">血浆尿酸</a>)（<a href="/w/UA" title="UA" class="mw-redirect">UA</a>)</li>
<li><a href="/w/%E8%A1%80%E6%B8%85%E8%8B%AF%E4%B8%99%E6%B0%A8%E9%85%B8" title="血清苯丙氨酸">血清苯丙氨酸</a></li>
<li><a href="/w/%E8%A1%80%E6%B8%85%E9%85%AA%E6%B0%A8%E9%85%B8" title="血清酪氨酸">血清酪氨酸</a>（<a href="/w/Tyr" title="Tyr" class="mw-redirect">Tyr</a>)</li>
<li><a href="/w/%E8%A1%80%E6%B6%B2%E9%9D%9E%E8%9B%8B%E7%99%BD%E6%B0%AE" title="血液非蛋白氮">血液非蛋白氮</a>（<a href="/w/NPN" title="NPN" class="mw-redirect">NPN</a>)</li>
<li><a href="/w/%E8%A1%80%E6%B6%B2%E8%BF%98%E5%8E%9F%E5%9E%8B%E8%B0%B7%E8%83%B1%E7%94%98%E8%82%BD" title="血液还原型谷胱甘肽">血液还原型谷胱甘肽</a>（<a href="/w/GSH" title="GSH" class="mw-redirect">GSH</a>)</li>
<li><a href="/w/%E8%A1%80%E6%B6%B2%E8%82%8C%E9%85%B8" title="血液肌酸">血液肌酸</a>（<a href="/w/Cre" title="Cre" class="mw-redirect">Cre</a>)</li>
<li><a href="/w/%E8%A1%80%E6%B6%B2%E8%82%8C%E9%85%90" title="血液肌酐">血液肌酐</a>（<a href="/w/Cr" title="Cr" class="mw-redirect">Cr</a>)</li>
<li><a href="/w/%E8%A1%80%E6%B6%B2%E5%B0%BF%E7%B4%A0%E6%B0%AE" title="血液尿素氮" class="mw-redirect">血液尿素氮</a>（<a href="/w/BUN" title="BUN" class="mw-redirect">BUN</a>)</li>
</ul>
<h2><span class="mw-headline" id=".E5.9E.82.E4.BD.93.E6.BF.80.E7.B4.A0.E6.A3.80.E6.B5.8B">垂体激素检测</span></h2>
<p><a href="/index.php?title=%E5%9E%82%E4%BD%93%E6%BF%80%E7%B4%A0%E6%A3%80%E6%B5%8B&amp;action=edit&amp;redlink=1" class="new" title="垂体激素检测（尚未撰写）" rel="nofollow">垂体激素检测</a></p>
<ul>
<li><a href="/w/5%EF%BC%8D%E7%BE%9F%E8%89%B2%E8%83%BA" title="5－羟色胺">5－羟色胺</a>（<a href="/w/5HT" title="5HT" class="mw-redirect">5HT</a>)</li>
<li><a href="/w/%E9%BB%84%E4%BD%93%E7%94%9F%E6%88%90%E7%B4%A0" title="黄体生成素">黄体生成素</a>（<a href="/w/LH" title="LH" class="mw-redirect">LH</a>)</li>
<li><a href="/w/%E6%8A%97%E5%88%A9%E5%B0%BF%E6%BF%80%E7%B4%A0" title="抗利尿激素">抗利尿激素</a>，<a href="/w/%E5%8A%A0%E5%8E%8B%E7%B4%A0" title="加压素">加压素</a>（<a href="/w/ADH" title="ADH" class="mw-redirect">ADH</a>)</li>
<li><a href="/w/%E5%8D%B5%E6%B3%A1%E5%88%BA%E6%BF%80%E7%B4%A0" title="卵泡刺激素" class="mw-redirect">卵泡刺激素</a>（<a href="/w/FSH" title="FSH" class="mw-redirect">FSH</a>)</li>
<li><a href="/w/%E6%B3%8C%E4%B9%B3%E7%B4%A0" title="泌乳素" class="mw-redirect">泌乳素</a>（<a href="/w/PRL" title="PRL" class="mw-redirect">PRL</a>)</li>
<li><a href="/w/%E7%94%9F%E9%95%BF%E6%BF%80%E7%B4%A0" title="生长激素">生长激素</a>（<a href="/w/GH" title="GH" class="mw-redirect">GH</a>)</li>
</ul>
<h2><span class="mw-headline" id=".E8.83.86.E8.89.B2.E7.B4.A0.E6.A3.80.E6.9F.A5">胆色素检查</span></h2>
<p><a href="/index.php?title=%E8%83%86%E8%89%B2%E7%B4%A0%E6%A3%80%E6%9F%A5&amp;action=edit&amp;redlink=1" class="new" title="胆色素检查（尚未撰写）" rel="nofollow">胆色素检查</a></p>
<ul>
<li><a href="/w/%E8%83%86%E7%BA%A2%E7%B4%A0%E5%AE%9A%E6%80%A7%E8%AF%95%E9%AA%8C" title="胆红素定性试验">胆红素定性试验</a>（<a href="/w/VDBT" title="VDBT" class="mw-redirect">VDBT</a>)</li>
<li><a href="/w/%E7%B2%AA%E8%83%86%E5%8E%9F" title="粪胆原">粪胆原</a>（<a href="/w/FU" title="FU" class="mw-redirect">FU</a>)</li>
<li><a href="/w/%E9%BB%84%E8%83%86%E6%8C%87%E6%95%B0" title="黄胆指数">黄胆指数</a>（II)</li>
<li><a href="/w/%E5%B0%BF%E8%83%86%E7%BA%A2%E7%B4%A0%E5%AE%9A%E6%80%A7" title="尿胆红素定性">尿胆红素定性</a>（<a href="/w/UBIL" title="UBIL" class="mw-redirect">UBIL</a>)</li>
<li><a href="/w/%E5%B0%BF%E8%83%86%E5%8E%9F" title="尿胆原">尿胆原</a>（<a href="/w/UU" title="UU" class="mw-redirect">UU</a>)</li>
<li><a href="/w/%E8%A1%80%E6%B8%85%E6%80%BB%E8%83%86%E7%BA%A2%E7%B4%A0" title="血清总胆红素">血清总胆红素</a>（<a href="/w/TBIL" title="TBIL" class="mw-redirect">TBIL</a>)</li>
<li><a href="/w/%E7%9B%B4%E6%8E%A5%E8%83%86%E7%BA%A2%E7%B4%A0" title="直接胆红素">直接胆红素</a>（<a href="/w/DBIL" title="DBIL" class="mw-redirect">DBIL</a>)</li>
</ul>
<h2><span class="mw-headline" id=".E8.9B.8B.E7.99.BD.E8.B4.A8.E6.B5.8B.E5.AE.9A">蛋白质测定</span></h2>
<p><a href="/index.php?title=%E8%9B%8B%E7%99%BD%E8%B4%A8%E6%B5%8B%E5%AE%9A&amp;action=edit&amp;redlink=1" class="new" title="蛋白质测定（尚未撰写）" rel="nofollow">蛋白质测定</a></p>
<ul>
<li><a href="/w/%E7%B3%96%E5%9F%BA%E8%A1%80%E7%BA%A2%E8%9B%8B%E7%99%BD" title="糖基血红蛋白">糖基血红蛋白</a>（<a href="/w/GHb" title="GHb" class="mw-redirect">GHb</a>)</li>
<li><a href="/w/%E7%B3%96%E5%9F%BA%E8%A1%80%E6%B5%86%E8%9B%8B%E7%99%BD" title="糖基血浆蛋白">糖基血浆蛋白</a>（<a href="/w/GPP" title="GPP" class="mw-redirect">GPP</a>)</li>
<li><a href="/w/%E8%A1%80%E6%B5%86%E7%BA%A4%E7%BB%B4%E8%9B%8B%E7%99%BD%E5%8E%9F" title="血浆纤维蛋白原">血浆纤维蛋白原</a>（<a href="/w/FB" title="FB" class="mw-redirect">FB</a>)</li>
<li><a href="/w/%E8%A1%80%E6%B5%86%E6%AD%A3%E9%93%81%E7%99%BD%E8%9B%8B%E7%99%BD" title="血浆正铁白蛋白">血浆正铁白蛋白</a>（<a href="/w/MHA" title="MHA" class="mw-redirect">MHA</a>)</li>
<li><a href="/w/%E8%A1%80%E6%B8%85%E7%99%BD%E8%9B%8B%E7%99%BD/%E7%90%83%E8%9B%8B%E7%99%BD%E6%AF%94%E5%80%BC" title="血清白蛋白/球蛋白比值">血清白蛋白/球蛋白比值</a>（<a href="/w/A/G" title="A/G" class="mw-redirect">A/G</a>)</li>
<li><a href="/w/%E8%A1%80%E6%B8%85%E7%99%BD%E8%9B%8B%E7%99%BD" title="血清白蛋白">血清白蛋白</a>（<a href="/w/A1B" title="A1B" class="mw-redirect">A1B</a>)</li>
<li><a href="/w/%E8%A1%80%E6%B8%85%E8%9B%8B%E7%99%BD%E7%94%B5%E6%B3%B3" title="血清蛋白电泳">血清蛋白电泳</a>（<a href="/w/SPE" title="SPE" class="mw-redirect">SPE</a>)</li>
<li><a href="/w/%E8%A1%80%E6%B8%85%E8%82%8C%E7%BA%A2%E8%9B%8B%E7%99%BD" title="血清肌红蛋白">血清肌红蛋白</a>（<a href="/w/Mb" title="Mb" class="mw-redirect">Mb</a>)</li>
<li><a href="/w/%E8%A1%80%E6%B8%85%E7%90%83%E8%9B%8B%E7%99%BD" title="血清球蛋白">血清球蛋白</a>（<a href="/index.php?title=G&amp;action=edit&amp;redlink=1" class="new" title="G（尚未撰写）" rel="nofollow">G</a>)</li>
<li><a href="/w/%E8%A1%80%E6%B8%85%E7%B2%98%E8%9B%8B%E7%99%BD" title="血清粘蛋白">血清粘蛋白</a>（<a href="/w/SM" title="SM" class="mw-redirect">SM</a>)</li>
<li><a href="/w/%E6%80%BB%E8%9B%8B%E7%99%BD" title="总蛋白">总蛋白</a>（<a href="/w/TP" title="TP" class="mw-redirect">TP</a>)</li>
</ul>
<h2><span class="mw-headline" id=".E8.9B.8B.E7.99.BD.E8.B4.A8.E5.8F.8A.E6.B0.A8.E7.9A.84.E6.B5.8B.E5.AE.9A">蛋白质及氨的测定</span></h2>
<p><a href="/index.php?title=%E8%9B%8B%E7%99%BD%E8%B4%A8%E5%8F%8A%E6%B0%A8%E7%9A%84%E6%B5%8B%E5%AE%9A&amp;action=edit&amp;redlink=1" class="new" title="蛋白质及氨的测定（尚未撰写）" rel="nofollow">蛋白质及氨的测定</a></p>
<ul>
<li><a href="/w/%E8%A1%80%E6%B0%A8" title="血氨">血氨</a>（<a href="/w/BA" title="BA" class="mw-redirect">BA</a>)</li>
<li><a href="/w/%E8%A1%80%E6%B8%85%E8%A7%A6%E7%8F%A0%E8%9B%8B%E7%99%BD" title="血清触珠蛋白">血清触珠蛋白</a>（<a href="/w/HP" title="HP" class="mw-redirect">HP</a>)</li>
<li><a href="/w/%E8%A1%80%E6%B8%85%E5%89%8D%E7%99%BD%E8%9B%8B%E7%99%BD" title="血清前白蛋白">血清前白蛋白</a>（<a href="/w/PA" title="PA" class="mw-redirect">PA</a>)</li>
<li><a href="/w/%E8%A1%80%E6%B8%85%E8%BD%AC%E9%93%81%E8%9B%8B%E7%99%BD" title="血清转铁蛋白">血清转铁蛋白</a>（<a href="/w/%E8%BF%90%E8%BD%AC%E8%9B%8B%E7%99%BD" title="运转蛋白" class="mw-redirect">运转蛋白</a>)</li>
<li><a href="/w/%E8%A1%80%E6%B8%85%E9%BA%9D%E9%A6%99%E8%8D%89%E9%85%9A%E6%B5%8A%E5%BA%A6%E8%AF%95%E9%AA%8C" title="血清麝香草酚浊度试验">血清麝香草酚浊度试验</a>（<a href="/w/TTT" title="TTT" class="mw-redirect">TTT</a>)</li>
</ul>
<h2><span class="mw-headline" id=".E9.AA.A8.E9.AB.93.E7.BB.86.E8.83.9E.E5.AD.A6.E6.A3.80.E6.9F.A5">骨髓细胞学检查</span></h2>
<p><a href="/index.php?title=%E9%AA%A8%E9%AB%93%E7%BB%86%E8%83%9E%E5%AD%A6%E6%A3%80%E6%9F%A5&amp;action=edit&amp;redlink=1" class="new" title="骨髓细胞学检查（尚未撰写）" rel="nofollow">骨髓细胞学检查</a></p>
<ul>
<li><a href="/w/%E9%AA%A8%E9%AB%93%E6%A3%80%E6%9F%A5" title="骨髓检查">骨髓检查</a></li>
<li><a href="/w/%E9%AA%A8%E9%AB%93%E8%B1%A1%E7%9A%84%E5%88%86%E6%9E%90" title="骨髓象的分析">骨髓象的分析</a></li>
<li><a href="/w/%E9%AA%A8%E9%AB%93%E8%B1%A1%E4%B8%8E%E8%A1%80%E8%B1%A1%E7%9A%84%E5%85%B3%E7%B3%BB" title="骨髓象与血象的关系">骨髓象与血象的关系</a></li>
<li><a href="/w/%E6%AD%A3%E5%B8%B8%E9%AA%A8%E9%AB%93%E8%B1%A1" title="正常骨髓象">正常骨髓象</a></li>
</ul>
<h2><span class="mw-headline" id=".E7.94.B2.E7.8A.B6.E6.97.81.E8.85.BA.E5.8A.9F.E8.83.BD.E6.A3.80.E6.B5.8B">甲状旁腺功能检测</span></h2>
<p><a href="/index.php?title=%E7%94%B2%E7%8A%B6%E6%97%81%E8%85%BA%E5%8A%9F%E8%83%BD%E6%A3%80%E6%B5%8B&amp;action=edit&amp;redlink=1" class="new" title="甲状旁腺功能检测（尚未撰写）" rel="nofollow">甲状旁腺功能检测</a></p>
<ul>
<li><a href="/w/%E7%94%B2%E7%8A%B6%E6%97%81%E8%85%BA%E7%B4%A0" title="甲状旁腺素">甲状旁腺素</a>（<a href="/w/PTH" title="PTH" class="mw-redirect">PTH</a>)</li>
<li><a href="/w/%E9%99%8D%E9%92%99%E7%B4%A0" title="降钙素">降钙素</a>（<a href="/w/CT" title="CT">CT</a>)</li>
</ul>
<h2><span class="mw-headline" id=".E7.94.B2.E7.8A.B6.E8.85.BA.E5.8A.9F.E8.83.BD.E6.A3.80.E6.B5.8B">甲状腺功能检测</span></h2>
<p><a href="/index.php?title=%E7%94%B2%E7%8A%B6%E8%85%BA%E5%8A%9F%E8%83%BD%E6%A3%80%E6%B5%8B&amp;action=edit&amp;redlink=1" class="new" title="甲状腺功能检测（尚未撰写）" rel="nofollow">甲状腺功能检测</a></p>
<ul>
<li><a href="/w/%E4%BF%83%E7%94%B2%E7%8A%B6%E8%85%BA%E6%BF%80%E7%B4%A0" title="促甲状腺激素">促甲状腺激素</a>（<a href="/w/TSH" title="TSH" class="mw-redirect">TSH</a>)</li>
<li><a href="/w/%E4%BF%83%E7%94%B2%E7%8A%B6%E8%85%BA%E6%BF%80%E7%B4%A0%E9%87%8A%E6%94%BE%E6%BF%80%E7%B4%A0" title="促甲状腺激素释放激素">促甲状腺激素释放激素</a>（<a href="/w/TRH" title="TRH" class="mw-redirect">TRH</a>)</li>
<li><a href="/w/%E5%8F%8D%EF%BC%8D%E4%B8%89%E7%A2%98%E7%94%B2%E8%85%BA%E5%8E%9F%E6%B0%A8%E9%85%B8" title="反－三碘甲腺原氨酸">反－三碘甲腺原氨酸</a>（<a href="/w/%E5%8F%8DT3" title="反T3" class="mw-redirect">反T3</a>)</li>
<li><a href="/w/%E7%94%B2%E7%8A%B6%E8%85%BA%E7%B4%A0%E6%80%BB%E9%87%8F" title="甲状腺素总量">甲状腺素总量</a>（<a href="/w/TT4" title="TT4" class="mw-redirect">TT4</a>)</li>
<li><a href="/w/%E4%B8%89%EF%BC%8D%E7%A2%98%E7%94%B2%E8%85%BA%E5%8E%9F%E6%B0%A8%E9%85%B8%E6%80%BB%E9%87%8F" title="三－碘甲腺原氨酸总量">三－碘甲腺原氨酸总量</a>（<a href="/w/TT3" title="TT3" class="mw-redirect">TT3</a>)</li>
<li><a href="/w/%E4%B8%89%E7%A2%98%E7%94%B2%E8%85%BA%E5%8E%9F%E6%B0%A8%E9%85%B8" title="三碘甲腺原氨酸">三碘甲腺原氨酸</a>（<a href="/w/T3RU" title="T3RU" class="mw-redirect">T3RU</a>)</li>
<li><a href="/w/%E8%A1%80%E6%B8%85%E8%9B%8B%E7%99%BD%E7%BB%93%E5%90%88%E7%A2%98" title="血清蛋白结合碘">血清蛋白结合碘</a></li>
<li><a href="/w/%E6%B8%B8%E7%A6%BB%E7%94%B2%E7%8A%B6%E8%85%BA%E7%B4%A0" title="游离甲状腺素">游离甲状腺素</a>（<a href="/w/FT4" title="FT4" class="mw-redirect">FT4</a>)</li>
<li><a href="/w/%E6%B8%B8%E7%A6%BB%E7%94%B2%E7%8A%B6%E8%85%BA%E7%B4%A0%E6%8C%87%E6%95%B0" title="游离甲状腺素指数">游离甲状腺素指数</a>（<a href="/w/T4" title="T4" class="mw-redirect">T4</a>)</li>
<li><a href="/w/%E6%B8%B8%E7%A6%BB%E4%B8%89%EF%BC%8D%E7%A2%98%E7%94%B2%E8%85%BA%E5%8E%9F%E6%B0%A8%E9%85%B8" title="游离三－碘甲腺原氨酸">游离三－碘甲腺原氨酸</a>（<a href="/w/FT3" title="FT3" class="mw-redirect">FT3</a>)</li>
</ul>
<h2><span class="mw-headline" id=".E6.B5.86.E8.86.9C.E8.85.94.E7.A9.BF.E5.88.BA.E6.B6.B2.E6.A3.80.E6.9F.A5">浆膜腔穿刺液检查</span></h2>
<p><a href="/index.php?title=%E6%B5%86%E8%86%9C%E8%85%94%E7%A9%BF%E5%88%BA%E6%B6%B2%E6%A3%80%E6%9F%A5&amp;action=edit&amp;redlink=1" class="new" title="浆膜腔穿刺液检查（尚未撰写）" rel="nofollow">浆膜腔穿刺液检查</a></p>
<ul>
<li><a href="/w/%E6%B5%86%E8%86%9C%E8%85%94%E6%BC%8F%E5%87%BA%E6%B6%B2%E5%8F%8A%E6%B8%97%E5%87%BA%E6%B6%B2" title="浆膜腔漏出液及渗出液">浆膜腔漏出液及渗出液</a></li>
</ul>
<h2><span class="mw-headline" id=".E7.B2.BE.E6.B6.B2.E6.A3.80.E6.9F.A5">精液检查</span></h2>
<p><a href="/index.php?title=%E7%B2%BE%E6%B6%B2%E6%A3%80%E6%9F%A5&amp;action=edit&amp;redlink=1" class="new" title="精液检查（尚未撰写）" rel="nofollow">精液检查</a></p>
<ul>
<li><a href="/w/%E7%B2%BE%E6%B6%B2%E9%87%8F" title="精液量">精液量</a></li>
<li><a href="/w/%E7%B2%BE%E5%AD%90%E6%B4%BB%E5%8A%A8%E5%BA%A6" title="精子活动度">精子活动度</a></li>
<li><a href="/w/%E7%B2%BE%E5%AD%90%E8%AE%A1%E6%95%B0" title="精子计数">精子计数</a></li>
<li><a href="/w/%E7%B2%BE%E5%AD%90%E5%BD%A2%E6%80%81" title="精子形态">精子形态</a></li>
</ul>
<h2><span class="mw-headline" id=".E9.85.B6.E7.B1.BB.E6.B5.8B.E5.AE.9A">酶类测定</span></h2>
<p><a href="/index.php?title=%E9%85%B6%E7%B1%BB%E6%B5%8B%E5%AE%9A&amp;action=edit&amp;redlink=1" class="new" title="酶类测定（尚未撰写）" rel="nofollow">酶类测定</a></p>
<ul>
<li><a href="/w/%E4%B8%99%E6%B0%A8%E9%85%B8%E6%B0%A8%E5%9F%BA%E8%BD%AC%E7%A7%BB%E9%85%B6" title="丙氨酸氨基转移酶" class="mw-redirect">丙氨酸氨基转移酶</a>（<a href="/w/ALT" title="ALT" class="mw-redirect">ALT</a>)</li>
<li><a href="/w/%E8%A1%80%E8%B6%85%E6%B0%A7%E5%8C%96%E7%89%A9%E6%AD%A7%E5%8C%96%E9%85%B6" title="血超氧化物歧化酶">血超氧化物歧化酶</a>（<a href="/w/SOD" title="SOD" class="mw-redirect">SOD</a>)</li>
<li><a href="/w/%E8%A1%80%E6%B8%85r-%E8%B0%B7%E6%B0%A8%E9%85%B0%E8%BD%AC%E8%82%BD%E9%85%B6" title="血清r-谷氨酰转肽酶">血清r-谷氨酰转肽酶</a>或<a href="/index.php?title=R-%E8%B0%B7%E6%B0%A8%E9%85%B0%E8%BD%AC%E6%B0%A8%E9%85%B6&amp;action=edit&amp;redlink=1" class="new" title="R-谷氨酰转氨酶（尚未撰写）" rel="nofollow">r-谷氨酰转氨酶</a>（<a href="/w/R-GT" title="R-GT">r-GT</a>或<a href="/w/R-GTP" title="R-GTP">r-GTP</a>)</li>
<li><a href="/w/%E8%A1%80%E6%B8%85%E8%83%86%E7%A2%B1%E8%84%82%E9%85%B6" title="血清胆碱脂酶">血清胆碱脂酶</a>（<a href="/w/%E8%A1%80%E6%B5%86%E8%83%86%E7%A2%B1%E8%84%82%E9%85%B6" title="血浆胆碱脂酶" class="mw-redirect">血浆胆碱脂酶</a>)（<a href="/w/CHS" title="CHS" class="mw-redirect">CHS</a>)</li>
<li><a href="/w/%E8%A1%80%E6%B8%85%E5%8D%95%E8%83%BA%E6%B0%A7%E5%8C%96%E9%85%B6" title="血清单胺氧化酶">血清单胺氧化酶</a>（<a href="/w/MAO" title="MAO" class="mw-redirect">MAO</a>)</li>
<li><a href="/w/%E8%A1%80%E6%B8%85%E6%B7%80%E7%B2%89%E9%85%B6" title="血清淀粉酶">血清淀粉酶</a>（<a href="/w/AMy" title="AMy" class="mw-redirect">AMy</a>)</li>
<li><a href="/w/%E8%A1%80%E6%B8%85%E8%B0%B7-%E8%8D%89%E8%BD%AC%E6%B0%A8%E9%85%B6" title="血清谷-草转氨酶" class="mw-redirect">血清谷-草转氨酶</a>（<a href="/w/AST" title="AST" class="mw-redirect">AST</a>)</li>
<li><a href="/w/%E8%A1%80%E6%B8%85%E8%B0%B7-%E8%8D%89%E8%BD%AC%E6%B0%A8%E9%85%B6%E5%90%8C%E5%B7%A5%E9%85%B6" title="血清谷-草转氨酶同工酶">血清谷-草转氨酶同工酶</a>（<a href="/w/GOT" title="GOT" class="mw-redirect">GOT</a>)</li>
<li><a href="/w/%E8%A1%80%E6%B8%85%E7%A2%B1%E6%80%A7%E7%A3%B7%E9%85%B8%E9%85%B6" title="血清碱性磷酸酶">血清碱性磷酸酶</a>（<a href="/w/AKP" title="AKP" class="mw-redirect">AKP</a>或<a href="/w/ALP" title="ALP" class="mw-redirect">ALP</a>)</li>
<li><a href="/w/%E8%A1%80%E6%B8%85%E4%BA%AE%E6%B0%A8%E9%85%B8%E6%B0%A8%E5%9F%BA%E8%82%BD%E9%85%B6" title="血清亮氨酸氨基肽酶">血清亮氨酸氨基肽酶</a>（<a href="/w/LAP" title="LAP" class="mw-redirect">LAP</a>)</li>
<li><a href="/w/%E8%A1%80%E6%B8%85%E7%A3%B7%E9%85%B8%E8%82%8C%E9%85%B8%E6%BF%80%E9%85%B6" title="血清磷酸肌酸激酶">血清磷酸肌酸激酶</a>（<a href="/w/CKP" title="CKP" class="mw-redirect">CKP</a>)或<a href="/w/%E8%82%8C%E9%85%B8%E6%BF%80%E9%85%B6" title="肌酸激酶">肌酸激酶</a>（<a href="/w/CK" title="CK" class="mw-redirect">CK</a>)</li>
<li><a href="/w/%E8%A1%80%E6%B8%85%E7%A3%B7%E9%85%B8%E6%BF%80%E9%85%B6%E5%90%8C%E5%B7%A5%E9%85%B6" title="血清磷酸激酶同工酶">血清磷酸激酶同工酶</a>（<a href="/w/CPK" title="CPK" class="mw-redirect">CPK</a>)</li>
<li><a href="/w/%E8%A1%80%E6%B8%85%E4%B9%B3%E9%85%B8%E8%84%B1%E6%B0%A2%E9%85%B6" title="血清乳酸脱氢酶">血清乳酸脱氢酶</a>（<a href="/w/LDH" title="LDH" class="mw-redirect">LDH</a>或<a href="/w/LD" title="LD" class="mw-redirect">LD</a>)</li>
<li><a href="/w/%E8%A1%80%E6%B8%85%E5%B1%B1%E6%A2%A8%E9%86%87%E8%84%B1%E6%B0%A2%E9%85%B6" title="血清山梨醇脱氢酶">血清山梨醇脱氢酶</a>（<a href="/w/SDH" title="SDH" class="mw-redirect">SDH</a>)</li>
<li><a href="/w/%E8%A1%80%E6%B8%85%E9%85%B8%E6%80%A7%E7%A3%B7%E9%85%B8%E9%85%B6" title="血清酸性磷酸酶">血清酸性磷酸酶</a>（<a href="/w/ACP" title="ACP" class="mw-redirect">ACP</a>)</li>
<li><a href="/w/%E8%A1%80%E6%B8%85%E8%84%82%E8%82%AA%E9%85%B6" title="血清脂肪酶">血清脂肪酶</a>（<a href="/w/LIP" title="LIP" class="mw-redirect">LIP</a>)</li>
</ul>
<h2><span class="mw-headline" id=".E5.85.8D.E7.96.AB.E5.AD.A6.E6.A3.80.E9.AA.8C">免疫学检验</span></h2>
<p><a href="/index.php?title=%E5%85%8D%E7%96%AB%E5%AD%A6%E6%A3%80%E9%AA%8C&amp;action=edit&amp;redlink=1" class="new" title="免疫学检验（尚未撰写）" rel="nofollow">免疫学检验</a></p>
<ul>
<li><a href="/index.php?title=%E8%A1%A5%E4%BD%93%E3%80%81%E6%8A%97%E4%BD%93%E5%8F%8A%E6%B7%8B%E5%B7%B4%E7%BB%86%E8%83%9E&amp;action=edit&amp;redlink=1" class="new" title="补体、抗体及淋巴细胞（尚未撰写）" rel="nofollow">补体、抗体及淋巴细胞</a>
<ul>
<li><a href="/w/%E8%A1%80%E6%B8%85%E8%A1%A5%E4%BD%93C3" title="血清补体C3">血清补体C3</a></li>
<li><a href="/w/%E8%A1%80%E6%B8%85%E8%A1%A5%E4%BD%93C4" title="血清补体C4">血清补体C4</a></li>
<li><a href="/w/%E8%A1%80%E6%B8%85%E8%A1%A5%E4%BD%93C5" title="血清补体C5">血清补体C5</a></li>
<li><a href="/w/%E8%A1%80%E6%B8%85%E8%A1%A5%E4%BD%93C6" title="血清补体C6">血清补体C6</a></li>
<li><a href="/w/%E8%A1%80%E6%B8%85%E8%A1%A5%E4%BD%93C7" title="血清补体C7">血清补体C7</a></li>
<li><a href="/w/%E8%A1%80%E6%B8%85%E8%A1%A5%E4%BD%93C8" title="血清补体C8">血清补体C8</a></li>
<li><a href="/w/%E8%A1%80%E6%B8%85%E8%A1%A5%E4%BD%93C9" title="血清补体C9">血清补体C9</a></li>
<li><a href="/w/%E8%A1%80%E6%B8%85%E8%A1%A5%E4%BD%93Iq" title="血清补体Iq">血清补体Iq</a></li>
<li><a href="/w/%E8%A1%80%E6%B8%85%E6%80%BB%E8%A1%A5%E4%BD%93" title="血清总补体">血清总补体</a>（<a href="/w/CH50" title="CH50" class="mw-redirect">CH50</a>)</li>
<li><a href="/w/%E6%8A%97ENA%E6%8A%97%E4%BD%93" title="抗ENA抗体">抗ENA抗体</a></li>
<li><a href="/w/%E6%8A%97%E6%A0%B8%E6%8A%97%E4%BD%93" title="抗核抗体">抗核抗体</a>（<a href="/w/ANA" title="ANA" class="mw-redirect">ANA</a>)</li>
<li><a href="/w/%E6%8A%97%E7%94%B2%E7%8A%B6%E8%85%BA%E7%90%83%E8%9B%8B%E7%99%BD%E6%8A%97%E4%BD%93" title="抗甲状腺球蛋白抗体">抗甲状腺球蛋白抗体</a>（<a href="/w/ATA" title="ATA" class="mw-redirect">ATA</a>)</li>
<li><a href="/w/%E6%8A%97%E7%94%B2%E7%8A%B6%E8%85%BA%E5%BE%AE%E7%B2%92%E4%BD%93%E6%8A%97%E4%BD%93" title="抗甲状腺微粒体抗体">抗甲状腺微粒体抗体</a></li>
<li><a href="/w/%E6%8A%97%E7%B2%BE%E5%AD%90%E6%8A%97%E4%BD%93" title="抗精子抗体">抗精子抗体</a>（<a href="/w/AA" title="AA">AA</a>)</li>
<li><a href="/w/%E6%8A%97%E5%8D%B5%E5%AD%90%E9%80%8F%E6%98%8E%E5%B8%A6%E6%8A%97%E4%BD%93" title="抗卵子透明带抗体">抗卵子透明带抗体</a></li>
<li><a href="/w/%E6%8A%97%E5%B9%B3%E6%BB%91%E8%82%8C%E6%8A%97%E4%BD%93" title="抗平滑肌抗体">抗平滑肌抗体</a>（<a href="/w/SMA" title="SMA" class="mw-redirect">SMA</a>)</li>
<li><a href="/w/%E6%8A%97%E8%82%BE%E4%B8%8A%E8%85%BA%E7%9A%AE%E8%B4%A8%E6%8A%97%E4%BD%93" title="抗肾上腺皮质抗体">抗肾上腺皮质抗体</a>（<a href="/w/AA" title="AA">AA</a>)</li>
</ul>
</li>
<li><a href="/w/%E5%B8%83%E6%B0%8F%E6%9D%86%E8%8F%8C%E5%87%9D%E9%9B%86%E8%AF%95%E9%AA%8C" title="布氏杆菌凝集试验">布氏杆菌凝集试验</a>（<a href="/w/BAT" title="BAT" class="mw-redirect">BAT</a>)</li>
<li><a href="/w/%E8%82%A5%E8%BE%BE%E6%B0%8F%E5%8F%8D%E5%BA%94" title="肥达氏反应">肥达氏反应</a>（<a href="/w/WR" title="WR" class="mw-redirect">WR</a>)</li>
<li><a href="/w/%E6%8A%97%E9%93%BE%E7%90%83%E8%8F%8C%E6%BA%B6%E8%A1%80%E7%B4%A0O%E8%AF%95%E9%AA%8C" title="抗链球菌溶血素O试验">抗链球菌溶血素O试验</a>（<a href="/w/ASO" title="ASO" class="mw-redirect">ASO</a>)</li>
<li><a href="/w/%E5%BF%AB%E9%80%9F%E8%A1%80%E6%B5%86%E5%8F%8D%E5%BA%94%E7%B4%A0%E7%8E%AF%E7%8A%B6%E5%8D%A1%E7%89%87%E8%AF%95%E9%AA%8C" title="快速血浆反应素环状卡片试验">快速血浆反应素环状卡片试验</a>（<a href="/w/RPR" title="RPR" class="mw-redirect">RPR</a>)</li>
<li><a href="/w/%E7%B1%BB%E9%A3%8E%E6%B9%BF%E5%9B%A0%E5%AD%90" title="类风湿因子">类风湿因子</a>（<a href="/w/RF" title="RF" class="mw-redirect">RF</a>)</li>
<li><a href="/w/%E5%86%B7%E5%87%9D%E9%9B%86%E8%AF%95%E9%AA%8C" title="冷凝集试验">冷凝集试验</a>（<a href="/w/CAT" title="CAT" class="mw-redirect">CAT</a>)</li>
<li><a href="/w/%E6%A2%85%E6%AF%92%E8%A1%80%E6%B8%85%E5%AD%A6%E6%A3%80%E6%B5%8B%E6%B3%95" title="梅毒血清学检测法">梅毒血清学检测法</a>（<a href="/w/USR" title="USR" class="mw-redirect">USR</a>)</li>
<li><a href="/w/%E5%97%9C%E5%BC%82%E6%80%A7%E5%87%9D%E9%9B%86%E8%AF%95%E9%AA%8C" title="嗜异性凝集试验">嗜异性凝集试验</a>（<a href="/w/HAT" title="HAT" class="mw-redirect">HAT</a>)</li>
<li><a href="/w/%E5%97%9C%E5%BC%82%E6%80%A7%E5%87%9D%E9%9B%86%E5%90%B8%E6%94%B6%E8%AF%95%E9%AA%8C" title="嗜异性凝集吸收试验">嗜异性凝集吸收试验</a>（<a href="/w/HAAT" title="HAAT" class="mw-redirect">HAAT</a>)</li>
<li><a href="/w/%E5%A4%96-%E8%A3%B4%E6%B0%8F%E5%8F%8D%E5%BA%94" title="外-裴氏反应">外-裴氏反应</a>（<a href="/w/WFR" title="WFR" class="mw-redirect">WFR</a>)</li>
<li><a href="/w/%E7%BB%86%E8%8F%8C%E8%A1%80%E6%B8%85%E5%AD%A6%E6%A3%80%E9%AA%8C" title="细菌血清学检验">细菌血清学检验</a></li>
<li><a href="/w/%E9%B2%8E%E8%AF%95%E9%AA%8C" title="鲎试验">鲎试验</a>（<a href="/w/LLT" title="LLT" class="mw-redirect">LLT</a>)</li>
</ul>
<h2><span class="mw-headline" id=".E8.84.91.E8.84.8A.E6.B6.B2.E6.A3.80.E6.9F.A5">脑脊液检查</span></h2>
<p><a href="/index.php?title=%E8%84%91%E8%84%8A%E6%B6%B2%E6%A3%80%E6%9F%A5&amp;action=edit&amp;redlink=1" class="new" title="脑脊液检查（尚未撰写）" rel="nofollow">脑脊液检查</a></p>
<ul>
<li><a href="/w/%E8%84%91%E8%84%8A%E6%B6%B2%E5%B8%B8%E8%A7%84" title="脑脊液常规">脑脊液常规</a></li>
<li><a href="/w/%E8%84%91%E8%84%8A%E6%B6%B2%E8%83%B6%E4%BD%93%E9%87%91%E8%AF%95%E9%AA%8C" title="脑脊液胶体金试验">脑脊液胶体金试验</a></li>
<li><a href="/w/%E8%84%91%E8%84%8A%E6%B6%B2%E6%BD%98%E6%B0%8F%E8%AF%95%E9%AA%8C" title="脑脊液潘氏试验">脑脊液潘氏试验</a>（<a href="/w/Pandy%E8%AF%95%E9%AA%8C" title="Pandy试验" class="mw-redirect">Pandy试验</a>)</li>
<li><a href="/w/%E8%84%91%E8%84%8A%E6%B6%B2%E8%89%B2%E6%B0%A8%E9%85%B8%E8%AF%95%E9%AA%8C" title="脑脊液色氨酸试验">脑脊液色氨酸试验</a>（<a href="/w/TrPT" title="TrPT" class="mw-redirect">TrPT</a>)</li>
</ul>
<h2><span class="mw-headline" id=".E8.B4.AB.E8.A1.80.E7.9A.84.E5.85.B6.E4.BB.96.E6.A3.80.E6.9F.A5">贫血的其他检查</span></h2>
<p><a href="/index.php?title=%E8%B4%AB%E8%A1%80%E7%9A%84%E5%85%B6%E4%BB%96%E6%A3%80%E6%9F%A5&amp;action=edit&amp;redlink=1" class="new" title="贫血的其他检查（尚未撰写）" rel="nofollow">贫血的其他检查</a></p>
<ul>
<li><a href="/w/%E5%8F%98%E6%80%A7%E7%8F%A0%E8%9B%8B%E7%99%BD%E5%B0%8F%E4%BD%93" title="变性珠蛋白小体">变性珠蛋白小体</a>（<a href="/w/Heinz%E4%BD%93" title="Heinz体" class="mw-redirect">Heinz体</a>)</li>
<li><a href="/w/%E7%BA%A2%E7%BB%86%E8%83%9E%E5%B9%B3%E5%9D%87%E5%8E%9A%E5%BA%A6" title="红细胞平均厚度">红细胞平均厚度</a>（<a href="/w/MCT" title="MCT" class="mw-redirect">MCT</a>)</li>
<li><a href="/w/%E7%BA%A2%E7%BB%86%E8%83%9E%E5%B9%B3%E5%9D%87%E4%BD%93%E7%A7%AF" title="红细胞平均体积">红细胞平均体积</a>（<a href="/w/MCV" title="MCV" class="mw-redirect">MCV</a>)</li>
<li><a href="/w/%E7%BA%A2%E7%BB%86%E8%83%9E%E5%B9%B3%E5%9D%87%E8%A1%80%E7%BA%A2%E8%9B%8B%E7%99%BD%E9%87%8F" title="红细胞平均血红蛋白量">红细胞平均血红蛋白量</a>（<a href="/w/MCH" title="MCH" class="mw-redirect">MCH</a>)</li>
<li><a href="/w/%E7%BA%A2%E7%BB%86%E8%83%9E%E5%B9%B3%E5%9D%87%E8%A1%80%E7%BA%A2%E8%9B%8B%E7%99%BD%E6%B5%93%E5%BA%A6" title="红细胞平均血红蛋白浓度">红细胞平均血红蛋白浓度</a>（<a href="/w/MCHC" title="MCHC" class="mw-redirect">MCHC</a>)</li>
<li><a href="/w/%E7%BA%A2%E7%BB%86%E8%83%9E%E5%B9%B3%E5%9D%87%E7%9B%B4%E5%BE%84" title="红细胞平均直径">红细胞平均直径</a>（<a href="/w/MCD" title="MCD" class="mw-redirect">MCD</a>)</li>
<li><a href="/w/%E7%BA%A2%E7%BB%86%E8%83%9E%E6%B8%97%E9%80%8F%E8%84%86%E6%80%A7%E8%AF%95%E9%AA%8C" title="红细胞渗透脆性试验">红细胞渗透脆性试验</a>（<a href="/w/EFT" title="EFT" class="mw-redirect">EFT</a>)</li>
<li><a href="/w/%E5%87%9D%E8%A1%80%E9%85%B6%E5%8E%9F%E6%B6%88%E8%80%97%E8%AF%95%E9%AA%8C" title="凝血酶原消耗试验">凝血酶原消耗试验</a>（<a href="/w/PCT" title="PCT" class="mw-redirect">PCT</a>)</li>
<li><a href="/w/%E7%83%AD%E6%BA%B6%E8%A1%80%E8%AF%95%E9%AA%8C" title="热溶血试验">热溶血试验</a>（<a href="/w/Heat_hemolysis_test" title="Heat hemolysis test" class="mw-redirect">Heat hemolysis test</a>)</li>
<li><a href="/w/%E5%97%9C%E7%A2%B1%E6%80%A7%E7%82%B9%E5%BD%A9%E7%BA%A2%E7%BB%86%E8%83%9E%E8%AE%A1%E6%95%B0" title="嗜碱性点彩红细胞计数">嗜碱性点彩红细胞计数</a></li>
<li><a href="/w/%E9%85%B8%E6%BA%B6%E8%A1%80%E8%AF%95%E9%AA%8C" title="酸溶血试验">酸溶血试验</a>（<a href="/w/%E6%B5%B7%E5%A7%86%E6%B0%8F%E8%AF%95%E9%AA%8C" title="海姆氏试验" class="mw-redirect">海姆氏试验</a>、<a href="/w/Ham%E2%80%99s_test" title="Ham’s test" class="mw-redirect">Ham’s test</a>)</li>
<li><a href="/w/%E7%BD%91%E7%BB%87%E7%BA%A2%E7%BB%86%E8%83%9E%E8%AE%A1%E6%95%B0" title="网织红细胞计数">网织红细胞计数</a>（<a href="/w/ReT" title="ReT" class="mw-redirect">ReT</a>)</li>
</ul>
<h2><span class="mw-headline" id=".E5.85.B6.E4.BB.96.E6.BF.80.E7.B4.A0.E5.8F.8A.E5.85.B6.E4.BB.A3.E8.B0.A2.E7.89.A9">其他激素及其代谢物</span></h2>
<p><a href="/index.php?title=%E5%85%B6%E4%BB%96%E6%BF%80%E7%B4%A0%E5%8F%8A%E5%85%B6%E4%BB%A3%E8%B0%A2%E7%89%A9&amp;action=edit&amp;redlink=1" class="new" title="其他激素及其代谢物（尚未撰写）" rel="nofollow">其他激素及其代谢物</a></p>
<ul>
<li><a href="/w/%CE%92%EF%BC%8D%E8%83%A1%E8%90%9D%E5%8D%9C%E7%B4%A0" title="Β－胡萝卜素">β－胡萝卜素</a></li>
<li><a href="/w/%E8%82%A0%E4%BF%83%E8%83%B0%E6%B6%B2%E7%B4%A0" title="肠促胰液素">肠促胰液素</a>，<a href="/w/%E8%83%B0%E6%B3%8C%E7%B4%A0" title="胰泌素" class="mw-redirect">胰泌素</a></li>
<li><a href="/w/%E7%BA%A2%E7%BB%86%E8%83%9E%E7%94%9F%E6%88%90%E7%B4%A0" title="红细胞生成素">红细胞生成素</a></li>
<li><a href="/w/%E7%8E%AF%E4%B8%80%E7%A3%B7%E9%85%B8%E9%B8%9F%E7%94%98" title="环一磷酸鸟甘">环一磷酸鸟甘</a>（<a href="/w/CGMP" title="CGMP" class="mw-redirect">cGMP</a>)</li>
<li><a href="/w/%E7%8E%AF%E4%B8%80%E7%A3%B7%E9%85%B8%E8%85%BA%E7%94%98" title="环一磷酸腺甘">环一磷酸腺甘</a>（<a href="/w/CAMP" title="CAMP" class="mw-redirect">cAMP</a>)</li>
<li><a href="/w/%E5%89%8D%E5%88%97%E8%85%BA%E7%B4%A0" title="前列腺素">前列腺素</a>（<a href="/w/PG" title="PG" class="mw-redirect">PG</a>)</li>
<li><a href="/w/%E8%82%BE%E7%B4%A0%E6%B4%BB%E5%BA%A6" title="肾素活度">肾素活度</a>（<a href="/w/PRA" title="PRA" class="mw-redirect">PRA</a>)</li>
<li><a href="/w/%E7%94%9F%E9%95%BF%E6%BF%80%E7%B4%A0%E4%BB%8B%E7%B4%A0%EF%BC%8DC" title="生长激素介素－C">生长激素介素－C</a></li>
<li><a href="/w/%E8%83%83%E6%B3%8C%E7%B4%A0" title="胃泌素">胃泌素</a></li>
<li><a href="/w/%E5%BF%83%E9%92%A0%E7%B4%A0" title="心钠素">心钠素</a>（<a href="/w/ANP" title="ANP" class="mw-redirect">ANP</a>)</li>
<li><a href="/w/%E8%A1%80%E7%AE%A1%E7%B4%A7%E5%BC%A0%E7%B4%A0%E2%85%A0" title="血管紧张素Ⅰ">血管紧张素Ⅰ</a></li>
<li><a href="/w/%E8%A1%80%E7%AE%A1%E7%B4%A7%E5%BC%A0%E7%B4%A0II" title="血管紧张素II" class="mw-redirect">血管紧张素II</a></li>
<li><a href="/w/%E8%A1%80%E6%B8%85%E7%B4%A0" title="血清素" class="mw-redirect">血清素</a>、<a href="/w/%E4%BA%94-%E7%BE%9F%E8%89%B2%E8%83%BA" title="五-羟色胺" class="mw-redirect">五-羟色胺</a>（<a href="/w/5-HT" title="5-HT" class="mw-redirect">5-HT</a>)</li>
<li><a href="/w/%E8%A1%80%E6%A0%93%E7%83%B7%E7%B4%A0B2" title="血栓烷素B2">血栓烷素B2</a>（<a href="/w/TXB2" title="TXB2" class="mw-redirect">TXB2</a>)</li>
</ul>
<h2><span class="mw-headline" id=".E5.89.8D.E5.88.97.E8.85.BA.E6.B6.B2.E6.A3.80.E6.9F.A5">前列腺液检查</span></h2>
<p><a href="/w/%E5%89%8D%E5%88%97%E8%85%BA%E6%B6%B2%E6%A3%80%E6%9F%A5" title="前列腺液检查">前列腺液检查</a></p>
<ul>
<li><a href="/w/%E5%89%8D%E5%88%97%E8%85%BA%E6%B6%B2%E5%8D%B5%E7%A3%B7%E8%84%82%E5%B0%8F%E4%BD%93" title="前列腺液卵磷脂小体">前列腺液卵磷脂小体</a></li>
<li><a href="/w/%E5%89%8D%E5%88%97%E8%85%BA%E6%B6%B2%E9%A2%9C%E8%89%B2" title="前列腺液颜色">前列腺液颜色</a></li>
<li><a href="/w/%E5%89%8D%E5%88%97%E8%85%BA%E6%B6%B2%E4%B8%AD%E7%9A%84%E7%99%BD%E7%BB%86%E8%83%9E" title="前列腺液中的白细胞">前列腺液中的白细胞</a></li>
<li><a href="/w/%E5%89%8D%E5%88%97%E8%85%BA%E6%B6%B2%E4%B8%AD%E7%9A%84%E6%BB%B4%E8%99%AB" title="前列腺液中的滴虫">前列腺液中的滴虫</a></li>
<li><a href="/w/%E5%89%8D%E5%88%97%E8%85%BA%E6%B6%B2%E4%B8%AD%E7%9A%84%E7%BA%A2%E7%BB%86%E8%83%9E" title="前列腺液中的红细胞">前列腺液中的红细胞</a></li>
<li><a href="/w/%E5%89%8D%E5%88%97%E8%85%BA%E6%B6%B2%E4%B8%AD%E7%9A%84%E7%B2%BE%E5%AD%90" title="前列腺液中的精子">前列腺液中的精子</a></li>
<li><a href="/w/%E5%89%8D%E5%88%97%E8%85%BA%E6%B6%B2%E4%B8%AD%E7%9A%84%E9%A2%97%E7%B2%92%E7%BB%86%E8%83%9E" title="前列腺液中的颗粒细胞">前列腺液中的颗粒细胞</a></li>
<li><a href="/w/%E5%89%8D%E5%88%97%E8%85%BA%E6%B6%B2%E4%B8%AD%E6%B7%80%E7%B2%89%E6%A0%B7%E4%BD%93" title="前列腺液中淀粉样体">前列腺液中淀粉样体</a></li>
<li><a href="/w/%E5%89%8D%E5%88%97%E8%85%BA%E6%B6%B2%E4%B8%AD%E4%B8%8A%E7%9A%AE%E7%BB%86%E8%83%9E" title="前列腺液中上皮细胞">前列腺液中上皮细胞</a></li>
<li><a href="/w/%E5%89%8D%E5%88%97%E8%85%BA%E6%B6%B2%E4%B8%AD%E7%BB%86%E8%8F%8C" title="前列腺液中细菌">前列腺液中细菌</a></li>
</ul>
<h2><span class="mw-headline" id=".E8.82.BE.E5.8A.9F.E8.83.BD">肾功能</span></h2>
<p><a href="/w/%E8%82%BE%E5%8A%9F%E8%83%BD" title="肾功能">肾功能</a></p>
<ul>
<li><a href="/w/N-%E4%B9%99%E9%85%B0-%CE%B2-D-%E6%B0%A8%E5%9F%BA%E8%91%A1%E8%90%84%E7%B3%96%E8%8B%B7%E9%85%B6" title="N-乙酰-β-D-氨基葡萄糖苷酶">N-乙酰-β-D-氨基葡萄糖苷酶</a>（<a href="/w/NAG" title="NAG" class="mw-redirect">NAG</a>)</li>
<li><a href="/w/%CE%922-%E5%BE%AE%E7%90%83%E8%9B%8B%E7%99%BD" title="Β2-微球蛋白">β2-微球蛋白</a>（<a href="/w/%CE%922-MG" title="Β2-MG" class="mw-redirect">β2-MG</a>)</li>
<li><a href="/w/%E8%9B%8B%E7%99%BD%E5%B0%BF%E6%8C%87%E6%95%B0" title="蛋白尿指数">蛋白尿指数</a>（<a href="/w/SPI" title="SPI" class="mw-redirect">SPI</a>)</li>
<li><a href="/w/%E5%86%85%E7%94%9F%E8%82%8C%E9%85%90%E6%B8%85%E9%99%A4%E7%8E%87" title="内生肌酐清除率">内生肌酐清除率</a>（<a href="/w/Ccr" title="Ccr" class="mw-redirect">Ccr</a>)</li>
<li><a href="/w/%E5%B0%BF%E6%B8%97%E9%87%8F%E6%B5%8B%E5%AE%9A" title="尿渗量测定">尿渗量测定</a>（<a href="/w/Uosm" title="Uosm" class="mw-redirect">Uosm</a>)</li>
<li><a href="/w/%E8%82%BE%E5%B0%8F%E7%AE%A1%E6%80%A7%E9%85%B8%E4%B8%AD%E6%AF%92%E8%AF%95%E9%AA%8C" title="肾小管性酸中毒试验">肾小管性酸中毒试验</a>（<a href="/w/RTA" title="RTA" class="mw-redirect">RTA</a>)</li>
</ul>
<h2><span class="mw-headline" id=".E8.82.BE.E4.B8.8A.E8.85.BA.E5.8A.9F.E8.83.BD.E6.A3.80.E6.B5.8B">肾上腺功能检测</span></h2>
<p><a href="/index.php?title=%E8%82%BE%E4%B8%8A%E8%85%BA%E5%8A%9F%E8%83%BD%E6%A3%80%E6%B5%8B&amp;action=edit&amp;redlink=1" class="new" title="肾上腺功能检测（尚未撰写）" rel="nofollow">肾上腺功能检测</a></p>
<ul>
<li><a href="/w/%E4%BF%83%E8%82%BE%E4%B8%8A%E8%85%BA%E7%9A%AE%E8%B4%A8%E6%BF%80%E7%B4%A0" title="促肾上腺皮质激素">促肾上腺皮质激素</a>（<a href="/w/ACTH" title="ACTH" class="mw-redirect">ACTH</a>)</li>
<li><a href="/w/%E5%84%BF%E8%8C%B6%E9%85%9A%E8%83%BA" title="儿茶酚胺">儿茶酚胺</a>、<a href="/w/%E5%A4%9A%E5%B7%B4%E8%83%BA" title="多巴胺">多巴胺</a></li>
<li><a href="/w/%E7%9A%AE%E8%B4%A8%E9%86%87%E6%80%BB%E9%87%8F" title="皮质醇总量">皮质醇总量</a></li>
<li><a href="/w/%E7%9A%AE%E8%B4%A8%E9%85%AE" title="皮质酮">皮质酮</a></li>
<li><a href="/w/%E5%8E%BB%E7%94%B2%E8%82%BE%E4%B8%8A%E8%85%BA%E7%B4%A0" title="去甲肾上腺素">去甲肾上腺素</a></li>
<li><a href="/w/%E9%86%9B%E5%9B%BA%E9%85%AE" title="醛固酮">醛固酮</a>（<a href="/w/Ald" title="Ald" class="mw-redirect">Ald</a>，<a href="/w/ALS" title="ALS" class="mw-redirect">ALS</a>)</li>
<li><a href="/w/%E8%82%BE%E4%B8%8A%E8%85%BA%E7%B4%A0" title="肾上腺素">肾上腺素</a></li>
<li><a href="/w/%E8%82%BE%E4%B8%8A%E8%85%BA%E7%B4%A0%E6%BF%80%E5%8F%91%E8%AF%95%E9%AA%8C" title="肾上腺素激发试验">肾上腺素激发试验</a></li>
</ul>
<h2><span class="mw-headline" id=".E7.97.B0.E6.B6.B2.E6.A3.80.E6.9F.A5">痰液检查</span></h2>
<p><a href="/index.php?title=%E7%97%B0%E6%B6%B2%E6%A3%80%E6%9F%A5&amp;action=edit&amp;redlink=1" class="new" title="痰液检查（尚未撰写）" rel="nofollow">痰液检查</a></p>
<ul>
<li><a href="/w/%E7%97%B0%E6%B6%B2%E9%87%8F" title="痰液量">痰液量</a></li>
<li><a href="/w/%E7%97%B0%E6%B6%B2%E6%B0%94%E5%91%B3" title="痰液气味">痰液气味</a></li>
<li><a href="/w/%E7%97%B0%E6%B6%B2%E6%80%A7%E7%8A%B6" title="痰液性状">痰液性状</a>（<a href="/w/%E7%97%B0%E6%B6%B2%E7%B2%98%E7%A8%A0%E5%BA%A6" title="痰液粘稠度" class="mw-redirect">痰液粘稠度</a>)</li>
<li><a href="/w/%E7%97%B0%E6%B6%B2%E4%B8%AD%E5%BC%B9%E5%8A%9B%E7%BA%A4%E7%BB%B4" title="痰液中弹力纤维">痰液中弹力纤维</a></li>
<li><a href="/w/%E7%97%B0%E6%B6%B2%E4%B8%AD%E5%AF%84%E7%94%9F%E8%99%AB" title="痰液中寄生虫">痰液中寄生虫</a></li>
<li><a href="/w/%E7%97%B0%E6%B6%B2%E4%B8%AD%E7%BB%93%E6%99%B6" title="痰液中结晶">痰液中结晶</a></li>
<li><a href="/w/%E7%97%B0%E6%B6%B2%E4%B8%AD%E7%BB%86%E8%83%9E" title="痰液中细胞">痰液中细胞</a></li>
<li><a href="/w/%E7%97%B0%E6%B6%B2%E4%B8%AD%E7%BB%86%E8%8F%8C%E9%95%9C%E6%A3%80" title="痰液中细菌镜检">痰液中细菌镜检</a></li>
</ul>
<h2><span class="mw-headline" id=".E7.B3.96.E7.B1.BB.E5.8F.8A.E5.85.B6.E4.BB.A3.E8.B0.A2.E4.BA.A7.E7.89.A9">糖类及其代谢产物</span></h2>
<p><a href="/index.php?title=%E7%B3%96%E7%B1%BB%E5%8F%8A%E5%85%B6%E4%BB%A3%E8%B0%A2%E4%BA%A7%E7%89%A9&amp;action=edit&amp;redlink=1" class="new" title="糖类及其代谢产物（尚未撰写）" rel="nofollow">糖类及其代谢产物</a></p>
<ul>
<li><a href="/w/%E8%A1%80%E6%B5%86%E9%85%AE%E4%BD%93" title="血浆酮体">血浆酮体</a></li>
<li><a href="/w/%E8%A1%80%E6%B8%85%E8%91%A1%E8%90%84%E7%B3%96" title="血清葡萄糖">血清葡萄糖</a>（<a href="/w/%E8%A1%80%E6%B5%86%E8%91%A1%E8%90%84%E7%B3%96" title="血浆葡萄糖" class="mw-redirect">血浆葡萄糖</a>)（<a href="/w/BS" title="BS" class="mw-redirect">BS</a>)</li>
<li><a href="/w/%E8%A1%80%E4%B9%B3%E9%85%B8" title="血乳酸">血乳酸</a>（<a href="/w/BL" title="BL" class="mw-redirect">BL</a>)</li>
</ul>
<h2><span class="mw-headline" id=".E5.BE.AE.E9.87.8F.E5.85.83.E7.B4.A0.E6.B5.8B.E5.AE.9A">微量元素测定</span></h2>
<p><a href="/index.php?title=%E5%BE%AE%E9%87%8F%E5%85%83%E7%B4%A0%E6%B5%8B%E5%AE%9A&amp;action=edit&amp;redlink=1" class="new" title="微量元素测定（尚未撰写）" rel="nofollow">微量元素测定</a></p>
<ul>
<li><a href="/w/%E9%92%BE" title="钾">钾</a>（<a href="/w/K" title="K" class="mw-redirect">K</a>)</li>
<li><a href="/w/%E8%A1%80%E6%B8%85%E9%92%99" title="血清钙">血清钙</a>（<a href="/w/Ca" title="Ca" class="mw-redirect">Ca</a>)</li>
<li><a href="/w/%E8%A1%80%E6%B8%85%E6%99%B6%E4%BD%93%E6%B8%97%E9%80%8F%E5%8E%8B" title="血清晶体渗透压">血清晶体渗透压</a></li>
<li><a href="/w/%E8%A1%80%E6%B8%85%E6%B0%AF" title="血清氯">血清氯</a>（<a href="/w/CL" title="CL" class="mw-redirect">CL</a>)</li>
<li><a href="/w/%E8%A1%80%E6%B8%85%E9%95%81" title="血清镁">血清镁</a>（<a href="/w/Mg" title="Mg" class="mw-redirect">Mg</a>)</li>
<li><a href="/w/%E8%A1%80%E6%B8%85%E9%92%A0" title="血清钠">血清钠</a>（<a href="/w/Na" title="Na" class="mw-redirect">Na</a>)</li>
<li><a href="/w/%E8%A1%80%E6%B8%85%E9%93%81/%E9%93%9C%E6%AF%94%E5%80%BC" title="血清铁/铜比值">血清铁/铜比值</a>（<a href="/w/Fe/Cu" title="Fe/Cu" class="mw-redirect">Fe/Cu</a>)</li>
<li><a href="/w/%E8%A1%80%E6%B8%85%E9%93%81" title="血清铁">血清铁</a>（<a href="/w/T_1RON" title="T 1RON" class="mw-redirect">T 1RON</a>)</li>
<li><a href="/w/%E8%A1%80%E6%B8%85%E9%93%9C" title="血清铜">血清铜</a>（<a href="/w/Cu" title="Cu" class="mw-redirect">Cu</a>)</li>
<li><a href="/w/%E8%A1%80%E6%B8%85%E6%97%A0%E6%9C%BA%E7%A3%B7" title="血清无机磷">血清无机磷</a>（<a href="/w/I_PHOS" title="I PHOS" class="mw-redirect">I PHOS</a>)</li>
<li><a href="/w/%E8%A1%80%E6%B8%85%E9%94%8C" title="血清锌">血清锌</a>（<a href="/w/Zn" title="Zn" class="mw-redirect">Zn</a>)</li>
<li><a href="/w/%E8%A1%80%E6%B8%85%E6%80%BB%E9%93%81%E7%BB%93%E5%90%88%E5%8A%9B" title="血清总铁结合力">血清总铁结合力</a>（<a href="/w/T1BC" title="T1BC" class="mw-redirect">T1BC</a>)</li>
</ul>
<h2><span class="mw-headline" id=".E7.BB.86.E8.83.9E.E7.BB.84.E7.BB.87.E5.8C.96.E5.AD.A6.E6.9F.93.E8.89.B2">细胞组织化学染色</span></h2>
<p><a href="/index.php?title=%E7%BB%86%E8%83%9E%E7%BB%84%E7%BB%87%E5%8C%96%E5%AD%A6%E6%9F%93%E8%89%B2&amp;action=edit&amp;redlink=1" class="new" title="细胞组织化学染色（尚未撰写）" rel="nofollow">细胞组织化学染色</a></p>
<ul>
<li><a href="/w/%E9%9D%9E%E7%89%B9%E5%BC%82%E6%80%A7%E9%85%AF%E9%85%B6%E6%9F%93%E8%89%B2" title="非特异性酯酶染色">非特异性酯酶染色</a></li>
<li><a href="/w/%E8%BF%87%E6%B0%A7%E5%8C%96%E9%85%B6%E6%9F%93%E8%89%B2" title="过氧化酶染色">过氧化酶染色</a></li>
<li><a href="/w/%E7%A2%B1%E6%80%A7%E7%A3%B7%E9%85%B8%E9%85%B6%E6%9F%93%E8%89%B2" title="碱性磷酸酶染色">碱性磷酸酶染色</a></li>
<li><a href="/w/%E7%B3%96%E5%8E%9F%E6%9F%93%E8%89%B2" title="糖原染色">糖原染色</a></li>
<li><a href="/w/%E9%93%81%E7%B2%92%E6%9F%93%E8%89%B2" title="铁粒染色">铁粒染色</a></li>
</ul>
<h2><span class="mw-headline" id=".E6.80.A7.E8.85.BA.E6.BF.80.E7.B4.A0.E6.A3.80.E6.B5.8B">性腺激素检测</span></h2>
<p><a href="/index.php?title=%E6%80%A7%E8%85%BA%E6%BF%80%E7%B4%A0%E6%A3%80%E6%B5%8B&amp;action=edit&amp;redlink=1" class="new" title="性腺激素检测（尚未撰写）" rel="nofollow">性腺激素检测</a></p>
<ul>
<li><a href="/w/17%EF%BC%8D%E7%BE%9F%E5%AD%95%E9%85%AE" title="17－羟孕酮">17－羟孕酮</a></li>
<li><a href="/w/%E9%9B%8C%E4%BA%8C%E9%86%87%E6%80%BB%E9%87%8F" title="雌二醇总量">雌二醇总量</a>（<a href="/w/TE2" title="TE2" class="mw-redirect">TE2</a>)</li>
<li><a href="/w/%E9%9B%8C%E4%B8%89%E9%86%87%E6%80%BB%E9%87%8F" title="雌三醇总量">雌三醇总量</a>（<a href="/w/TE3" title="TE3" class="mw-redirect">TE3</a>)</li>
<li><a href="/w/%E9%9B%8C%E9%85%AE" title="雌酮" class="mw-redirect">雌酮</a>（<a href="/w/E1" title="E1" class="mw-redirect">E1</a>)</li>
<li><a href="/w/%E7%BB%92%E6%AF%9B%E8%86%9C%E4%BF%83%E6%80%A7%E8%85%BA%E6%BF%80%E7%B4%A0" title="绒毛膜促性腺激素" class="mw-redirect">绒毛膜促性腺激素</a>（<a href="/w/HCG" title="HCG" class="mw-redirect">HCG</a>)</li>
<li><a href="/w/%E8%83%8E%E7%9B%98%E5%82%AC%E4%B9%B3%E7%B4%A0" title="胎盘催乳素">胎盘催乳素</a>（<a href="/w/PL" title="PL" class="mw-redirect">PL</a>)</li>
<li><a href="/w/%E9%9B%84%E7%83%AF%E4%BA%8C%E9%85%AE" title="雄烯二酮">雄烯二酮</a></li>
<li><a href="/w/%E8%A1%80%E6%B8%85%E6%A3%8B%E6%AF%9B%E8%86%9C%E4%BF%83%E6%80%A7%E8%85%BA%E6%BF%80%E7%B4%A0B%EF%BC%8D%E4%BA%9A%E5%8D%95%E4%BD%8D" title="血清棋毛膜促性腺激素B－亚单位">血清棋毛膜促性腺激素B－亚单位</a>（<a href="/w/B-HCG" title="B-HCG" class="mw-redirect">b-HCG</a>)</li>
<li><a href="/w/%E5%AD%95%E9%85%AE" title="孕酮" class="mw-redirect">孕酮</a>（<a href="/w/P" title="P">P</a>)</li>
<li><a href="/w/%E7%9D%BE%E9%85%AE%E6%80%BB%E9%87%8F" title="睾酮总量">睾酮总量</a>（<a href="/w/T" title="T">T</a>)</li>
</ul>
<h2><span class="mw-headline" id=".E8.83.B0.E5.B2.9B.E5.8A.9F.E8.83.BD.E6.A3.80.E6.B5.8B">胰岛功能检测</span></h2>
<p><a href="/index.php?title=%E8%83%B0%E5%B2%9B%E5%8A%9F%E8%83%BD%E6%A3%80%E6%B5%8B&amp;action=edit&amp;redlink=1" class="new" title="胰岛功能检测（尚未撰写）" rel="nofollow">胰岛功能检测</a></p>
<ul>
<li><a href="/w/C%EF%BC%8D%E5%A4%AA" title="C－太">C－太</a></li>
<li>糖化血红蛋白；血红蛋白A1C</li>
<li><a href="/w/%E8%83%B0%E5%B2%9B%E7%B4%A0" title="胰岛素">胰岛素</a></li>
<li><a href="/w/%E8%83%B0%E5%B2%9B%E7%B4%A0%E5%8E%9F" title="胰岛素原">胰岛素原</a></li>
<li><a href="/w/%E8%83%B0%E9%AB%98%E8%A1%80%E7%B3%96%E7%B4%A0" title="胰高血糖素">胰高血糖素</a></li>
</ul>
<h2><span class="mw-headline" id=".E9.98.B4.E9.81.93.E5.88.86.E6.B3.8C.E7.89.A9.E6.A3.80.E6.9F.A5">阴道分泌物检查</span></h2>
<p><a href="/w/%E9%98%B4%E9%81%93%E5%88%86%E6%B3%8C%E7%89%A9%E6%A3%80%E6%9F%A5" title="阴道分泌物检查">阴道分泌物检查</a></p>
<ul>
<li><a href="/w/%E7%99%BD%E5%B8%A6" title="白带">白带</a></li>
<li><a href="/w/%E9%98%B4%E9%81%93%E6%B8%85%E6%B4%81%E5%BA%A6" title="阴道清洁度">阴道清洁度</a></li>
<li><a href="/w/%E5%AD%90%E5%AE%AB%E9%A2%88%E7%B2%98%E6%B6%B2" title="子宫颈粘液">子宫颈粘液</a></li>
</ul>
<h2><span class="mw-headline" id=".E8.84.82.E7.B1.BB.E5.92.8C.E8.BD.BD.E8.84.82.E8.9B.8B.E7.99.BD.E6.B5.8B.E5.AE.9A">脂类和载脂蛋白测定</span></h2>
<p><a href="/index.php?title=%E8%84%82%E7%B1%BB%E5%92%8C%E8%BD%BD%E8%84%82%E8%9B%8B%E7%99%BD%E6%B5%8B%E5%AE%9A&amp;action=edit&amp;redlink=1" class="new" title="脂类和载脂蛋白测定（尚未撰写）" rel="nofollow">脂类和载脂蛋白测定</a></p>
<ul>
<li><a href="/w/%E9%AB%98%E5%AF%86%E5%BA%A6%E8%84%82%E8%9B%8B%E7%99%BD%E8%83%86%E5%9B%BA%E9%86%87" title="高密度脂蛋白胆固醇">高密度脂蛋白胆固醇</a>（<a href="/w/HDL-ch" title="HDL-ch" class="mw-redirect">HDL-ch</a>)</li>
<li><a href="/w/%E8%A1%80%E6%B8%85ApoA-I/ApoB%E6%AF%94%E5%80%BC" title="血清ApoA-I/ApoB比值">血清ApoA-I/ApoB比值</a></li>
<li><a href="/w/%E8%A1%80%E6%B8%85%E8%BF%87%E6%B0%A7%E5%8C%96%E8%84%82%E8%B4%A8" title="血清过氧化脂质">血清过氧化脂质</a>（<a href="/w/%E8%A1%80%E6%B5%86%E8%BF%87%E6%B0%A7%E5%8C%96%E8%84%82%E8%B4%A8" title="血浆过氧化脂质" class="mw-redirect">血浆过氧化脂质</a>)（<a href="/w/LPO" title="LPO" class="mw-redirect">LPO</a>)</li>
<li><a href="/w/%E8%83%86%E7%A2%B1%E9%85%AF%E9%85%B6" title="胆碱酯酶">胆碱酯酶</a>（<a href="/index.php?title=CHE&amp;action=edit&amp;redlink=1" class="new" title="CHE（尚未撰写）" rel="nofollow">CHE</a>或<a href="/w/CE" title="CE" class="mw-redirect">CE</a>)</li>
<li><a href="/w/%E8%A1%80%E6%B8%85%E8%83%86%E5%9B%BA%E9%86%87" title="血清胆固醇">血清胆固醇</a>（Ch或<a href="/w/Tch" title="Tch" class="mw-redirect">Tch</a>或<a href="/w/TC" title="TC" class="mw-redirect">TC</a>)</li>
<li><a href="/w/%E8%A1%80%E6%B8%85%E9%9D%9E%E8%84%82%E5%8C%96%E8%84%82%E8%82%AA%E9%85%B8" title="血清非脂化脂肪酸">血清非脂化脂肪酸</a>（<a href="/w/FFA" title="FFA" class="mw-redirect">FFA</a>)</li>
<li><a href="/w/%E8%A1%80%E6%B8%85%E7%94%98%E6%B2%B9%E4%B8%89%E8%84%82" title="血清甘油三脂">血清甘油三脂</a>（<a href="/w/TG" title="TG" class="mw-redirect">TG</a>)</li>
<li><a href="/w/%E8%A1%80%E6%B8%85%E7%A3%B7%E8%84%82" title="血清磷脂">血清磷脂</a>（<a href="/w/PL" title="PL" class="mw-redirect">PL</a>或<a href="/w/PHL" title="PHL" class="mw-redirect">PHL</a>)</li>
<li><a href="/w/%E8%A1%80%E6%B8%85%E8%BD%BD%E8%84%82%E8%9B%8B%E7%99%BDA-I" title="血清载脂蛋白A-I">血清载脂蛋白A-I</a>（<a href="/w/ApoA-I" title="ApoA-I" class="mw-redirect">ApoA-I</a>)</li>
<li><a href="/w/%E8%A1%80%E6%B8%85%E8%BD%BD%E8%84%82%E8%9B%8B%E7%99%BDB" title="血清载脂蛋白B">血清载脂蛋白B</a>（<a href="/w/ApoB" title="ApoB" class="mw-redirect">ApoB</a>)</li>
<li><a href="/w/%E8%A1%80%E6%B8%85%E8%84%82%E8%9B%8B%E7%99%BD-X" title="血清脂蛋白-X">血清脂蛋白-X</a>（<a href="/w/LP-X" title="LP-X" class="mw-redirect">LP-X</a>)</li>
<li><a href="/w/%E8%A1%80%E6%B8%85%E6%80%BB%E8%83%86%E8%84%82" title="血清总胆脂">血清总胆脂</a>（<a href="/w/TL" title="TL" class="mw-redirect">TL</a>)</li>
<li><a href="/w/%E4%BD%8E%E5%AF%86%E5%BA%A6%E8%84%82%E8%9B%8B%E7%99%BD%E8%83%86%E5%9B%BA%E9%86%87" title="低密度脂蛋白胆固醇">低密度脂蛋白胆固醇</a>(<a href="/index.php?title=LDL-C&amp;action=edit&amp;redlink=1" class="new" title="LDL-C（尚未撰写）" rel="nofollow">LDL-C</a>)</li>
</ul>
<h2><span class="mw-headline" id=".E6.AD.A2.E8.A1.80.E4.B8.8E.E5.87.9D.E8.A1.80.E9.9A.9C.E7.A2.8D.E6.A3.80.E6.9F.A5">止血与凝血障碍检查</span></h2>
<p><a href="/index.php?title=%E6%AD%A2%E8%A1%80%E4%B8%8E%E5%87%9D%E8%A1%80%E9%9A%9C%E7%A2%8D%E6%A3%80%E6%9F%A5&amp;action=edit&amp;redlink=1" class="new" title="止血与凝血障碍检查（尚未撰写）" rel="nofollow">止血与凝血障碍检查</a></p>
<ul>
<li><a href="/w/%E5%87%BA%E8%A1%80%E6%97%B6%E9%97%B4" title="出血时间">出血时间</a>（<a href="/w/BT" title="BT" class="mw-redirect">BT</a>)</li>
<li><a href="/w/%E5%A4%8D%E9%92%99%E6%97%B6%E9%97%B4" title="复钙时间">复钙时间</a></li>
<li><a href="/w/%E6%AF%9B%E7%BB%86%E8%A1%80%E7%AE%A1%E8%84%86%E6%80%A7%E8%AF%95%E9%AA%8C" title="毛细血管脆性试验">毛细血管脆性试验</a>（<a href="/w/%E6%9D%9F%E8%87%82%E8%AF%95%E9%AA%8C" title="束臂试验" class="mw-redirect">束臂试验</a>)</li>
<li><a href="/w/%E5%87%9D%E8%A1%80%E9%85%B6%E5%8E%9F%E6%97%B6%E9%97%B4" title="凝血酶原时间">凝血酶原时间</a>（<a href="/w/PT" title="PT" class="mw-redirect">PT</a>)</li>
<li><a href="/w/%E5%87%9D%E8%A1%80%E9%85%B6%E5%8E%9F%E6%B6%88%E8%80%97%E8%AF%95%E9%AA%8C" title="凝血酶原消耗试验">凝血酶原消耗试验</a>（<a href="/w/PCT" title="PCT" class="mw-redirect">PCT</a>)</li>
<li><a href="/w/%E5%87%9D%E8%A1%80%E6%97%B6%E9%97%B4" title="凝血时间">凝血时间</a>（<a href="/w/CT" title="CT">CT</a>)</li>
<li><a href="/w/%E5%97%9C%E7%A2%B1%E6%80%A7%E7%82%B9%E5%BD%A9%E7%BA%A2%E7%BB%86%E8%83%9E%E8%AE%A1%E6%95%B0" title="嗜碱性点彩红细胞计数">嗜碱性点彩红细胞计数</a></li>
<li><a href="/w/%E7%BA%A4%E7%BB%B4%E8%9B%8B%E7%99%BD%E5%8E%9F%E9%99%8D%E8%A7%A3%E4%BA%A7%E7%89%A9" title="纤维蛋白原降解产物">纤维蛋白原降解产物</a>（<a href="/w/FDP" title="FDP" class="mw-redirect">FDP</a>)</li>
<li><a href="/w/%E8%A1%80%E6%B5%86%E9%B1%BC%E7%B2%BE%E8%9B%8B%E7%99%BD%E5%89%AF%E5%87%9D%E9%9B%86%E8%AF%95%E9%AA%8C" title="血浆鱼精蛋白副凝集试验">血浆鱼精蛋白副凝集试验</a>（<a href="/w/PPP%E8%AF%95%E9%AA%8C" title="PPP试验" class="mw-redirect">PPP试验</a>或<a href="/w/3P%E8%AF%95%E9%AA%8C" title="3P试验" class="mw-redirect">3P试验</a>)</li>
<li><a href="/w/%E8%A1%80%E5%9D%97%E6%94%B6%E7%BC%A9%E6%97%B6%E9%97%B4" title="血块收缩时间">血块收缩时间</a>（<a href="/w/CRT" title="CRT" class="mw-redirect">CRT</a>)</li>
<li><a href="/w/%E8%A1%80%E5%B0%8F%E6%9D%BF%E8%AE%A1%E6%95%B0" title="血小板计数">血小板计数</a>（<a href="/w/BPC" title="BPC" class="mw-redirect">BPC</a>)</li>
<li><a href="/w/%E8%A1%80%E5%B0%8F%E6%9D%BF%E5%87%9D%E9%9B%86%E5%8A%9F%E8%83%BD%E8%AF%95%E9%AA%8C" title="血小板凝集功能试验">血小板凝集功能试验</a>（<a href="/w/PAGT" title="PAGT" class="mw-redirect">PAGT</a>)</li>
<li><a href="/w/%E8%A1%80%E5%B0%8F%E6%9D%BF%E7%B2%98%E9%99%84%E5%8A%9F%E8%83%BD" title="血小板粘附功能">血小板粘附功能</a>（<a href="/w/%E8%A1%80%E5%B0%8F%E6%9D%BF%E6%BB%9E%E7%95%99%E5%8A%9F%E8%83%BD" title="血小板滞留功能" class="mw-redirect">血小板滞留功能</a>)（<a href="/w/PADT" title="PADT" class="mw-redirect">PADT</a>)</li>
<li><a href="/w/%E4%BC%98%E7%90%83%E8%9B%8B%E7%99%BD%E6%BA%B6%E8%A7%A3%E6%97%B6%E9%97%B4" title="优球蛋白溶解时间">优球蛋白溶解时间</a>（<a href="/w/ELT" title="ELT" class="mw-redirect">ELT</a>)</li>
</ul>
<h2><span class="mw-headline" id=".E6.80.8E.E6.A0.B7.E7.9C.8B.E5.8C.96.E9.AA.8C.E5.8D.95.E4.B8.93.E9.A2.98">怎样看化验单专题</span></h2>
<p>专题主页<a href="/w/%E6%80%8E%E6%A0%B7%E7%9C%8B%E5%8C%96%E9%AA%8C%E5%8D%95" title="怎样看化验单">怎样看化验单</a>, <a href="/w/%E7%96%BE%E7%97%85%E8%AF%8A%E6%96%AD" title="疾病诊断">疾病诊断</a></p>
<p>关于医学化验单：</p>
<ul>
<li><strong class="selflink">常见化验指标及意义</strong></li>
<li><a href="/w/%E6%80%8E%E6%A0%B7%E7%90%86%E8%A7%A3%E6%A3%80%E9%AA%8C%E7%BB%93%E6%9E%9C" title="怎样理解检验结果">怎样理解检验结果‎</a></li>
<li><a href="/w/%E6%80%8E%E6%A0%B7%E7%9C%8B%E5%8C%96%E9%AA%8C%E5%8D%95%E4%B8%8A%E7%9A%84%E5%8A%A0%E5%8F%B7%E5%92%8C%E5%87%8F%E5%8F%B7" title="怎样看化验单上的加号和减号">怎样看化验单上的加号和减号</a></li>
</ul>
<p>常见的化验单：</p>
<ul>
<li><a href="/w/%E6%80%8E%E6%A0%B7%E7%9C%8B%E8%A1%80%E5%B8%B8%E8%A7%84%E5%8C%96%E9%AA%8C%E5%8D%95" title="怎样看血常规化验单">怎样看血常规化验单</a></li>
<li><a href="/w/%E5%A6%82%E4%BD%95%E7%9C%8B%E4%B9%99%E8%82%9D%E4%B8%A4%E5%AF%B9%E5%8D%8A%E5%8C%96%E9%AA%8C%E5%8D%95" title="如何看乙肝两对半化验单">如何看乙肝两对半化验单</a></li>
<li><a href="/w/%E6%80%8E%E6%A0%B7%E7%9C%8B%E8%82%9D%E5%8A%9F%E8%83%BD%E5%8C%96%E9%AA%8C%E5%8D%95" title="怎样看肝功能化验单">怎样看肝功能化验单</a></li>
<li><a href="/w/%E6%80%8E%E6%A0%B7%E7%9C%8B%E7%B3%96%E5%B0%BF%E7%97%85%E6%A3%80%E9%AA%8C%E5%8D%95" title="怎样看糖尿病检验单">怎样看糖尿病检验单</a></li>
<li><a href="/w/%E5%A6%82%E4%BD%95%E7%9C%8B%E5%B0%BF%E5%B8%B8%E8%A7%84%E6%A3%80%E6%9F%A5%E5%8C%96%E9%AA%8C%E5%8D%95" title="如何看尿常规检查化验单">如何看尿常规检查化验单</a></li>
<li><a href="/w/%E6%80%8E%E6%A0%B7%E7%9C%8B%E7%B2%AA%E4%BE%BF%E5%B8%B8%E8%A7%84%E6%A3%80%E6%9F%A5%E5%8C%96%E9%AA%8C%E5%8D%95" title="怎样看粪便常规检查化验单">怎样看粪便常规检查化验单</a></li>
<li><a href="/w/%E6%80%8E%E6%A0%B7%E7%9C%8B%E5%89%8D%E5%88%97%E8%85%BA%E6%B6%B2%E5%8C%96%E9%AA%8C%E5%8D%95" title="怎样看前列腺液化验单">怎样看前列腺液化验单</a></li>
<li><a href="/w/%E5%A6%82%E4%BD%95%E7%9C%8B%E8%82%BE%E5%8A%9F%E8%83%BD%E6%A3%80%E6%B5%8B%E5%8C%96%E9%AA%8C%E7%BB%93%E6%9E%9C" title="如何看肾功能检测化验结果">如何看肾功能检测化验结果</a></li>
<li><a href="/w/%E6%80%8E%E6%A0%B7%E7%9C%8B%E7%BB%93%E6%A0%B8%E8%8F%8C%E7%B4%A0%E7%9A%AE%E8%AF%95%E7%BB%93%E6%9E%9C" title="怎样看结核菌素皮试结果">怎样看结核菌素皮试结果</a></li>
<li><a href="/w/%E6%80%8E%E6%A0%B7%E7%9C%8B%E8%84%91%E8%84%8A%E6%B6%B2%E5%B8%B8%E8%A7%84%E6%A3%80%E5%8C%96%E9%AA%8C%E5%8D%95" title="怎样看脑脊液常规检化验单">怎样看脑脊液常规检化验单</a></li>
<li><a href="/w/%E6%80%8E%E6%A0%B7%E7%9C%8B%E6%B5%86%E8%86%9C%E8%85%94%E6%B6%B2%E6%A3%80%E9%AA%8C%E7%BB%93%E6%9E%9C" title="怎样看浆膜腔液检验结果">怎样看浆膜腔液检验结果</a></li>
<li><a href="/w/%E6%80%8E%E6%A0%B7%E7%9C%8B%E8%A1%80%E6%B0%94%E5%88%86%E6%9E%90%E7%BB%93%E6%9E%9C" title="怎样看血气分析结果">怎样看血气分析结果</a></li>
</ul>

<!-- 
NewPP limit report
Preprocessor node count: 122/1000000
Post-expand include size: 749/2097152 bytes
Template argument size: 0/2097152 bytes
Expensive parser function count: 0/100
-->

<!-- Saved in parser cache with key ahospital:pcache:idhash:82939-0!1!0!!zh-hans!2!edit=0 and timestamp 20190608031138 -->
<div id="fromlink">出自A+医学百科 “常见化验指标及意义”条目 <a href="http://www.a-hospital.com/w/%E5%B8%B8%E8%A7%81%E5%8C%96%E9%AA%8C%E6%8C%87%E6%A0%87%E5%8F%8A%E6%84%8F%E4%B9%89" class="external free" target="_blank">http://www.a-hospital.com/w/%E5%B8%B8%E8%A7%81%E5%8C%96%E9%AA%8C%E6%8C%87%E6%A0%87%E5%8F%8A%E6%84%8F%E4%B9%89</a> 转载请保留此链接</div><div class="bdsharebuttonbox"><a href="#" class="bds_qzone" data-cmd="qzone" title="分享到QQ空间"></a><a href="#" class="bds_weixin" data-cmd="weixin" title="分享到微信"></a><a href="#" class="bds_tqq" data-cmd="tqq" title="分享到腾讯微博"></a><a href="#" class="bds_tsina" data-cmd="tsina" title="分享到新浪微博"></a><a href="#" class="bds_fbook" data-cmd="fbook" title="分享到Facebook"></a><a href="#" class="bds_copy" data-cmd="copy" title="分享到复制网址"></a><a href="#" class="bds_more" data-cmd="more"></a><a href="#" class="bds_count" data-cmd="count"></a></div>
<table class="msg-table">

<tr style="background-color:rgb(206, 223, 242);">
<td><b>关于“<strong class="selflink">常见化验指标及意义</strong>”的留言：</b>
</td><td align="right"><img alt="Feed-icon.png" src="http://p.ayxbk.com/images/f/f4/Feed-icon.png" width="12" height="12" /> <a href="http://www.a-hospital.com/index.php?title=%E8%AE%A8%E8%AE%BA:%E5%B8%B8%E8%A7%81%E5%8C%96%E9%AA%8C%E6%8C%87%E6%A0%87%E5%8F%8A%E6%84%8F%E4%B9%89&amp;feed=rss&amp;action=history" class="external text" target="_blank">订阅讨论RSS</a>
</td></tr>
<tr>
<td colspan="2" style="background-color:#ffffff;">
<h2> <span class="mw-headline" id=".E7.BB.99.E5.B8.B8.E8.A7.81.E5.8C.96.E9.AA.8C.E6.8C.87.E6.A0.87.E5.8F.8A.E6.84.8F.E4.B9.89.E6.9D.A1.E7.9B.AE.E7.9A.84.E7.95.99.E8.A8.80"> 给常见化验指标及意义条目的留言 </span></h2>
<p>--<a href="/w/%E7%89%B9%E6%AE%8A:%E7%94%A8%E6%88%B7%E8%B4%A1%E7%8C%AE/219.137.26.182" title="特殊:用户贡献/219.137.26.182">219.137.26.182</a> 2013年9月16日 (一) 14:15 (CST)
</p><p>留言：
</p><p><br />
血小板计数（BPC)
</p><p>这个英文缩写是否有误？一般来说应该是PLT。
</p>
</td></tr>
<tr>
<td colspan="2"><a href="http://www.a-hospital.com/index.php?title=%E8%AE%A8%E8%AE%BA:%E5%B8%B8%E8%A7%81%E5%8C%96%E9%AA%8C%E6%8C%87%E6%A0%87%E5%8F%8A%E6%84%8F%E4%B9%89&amp;action=edit&amp;section=new&amp;preload=%E6%A8%A1%E6%9D%BF%3A%E7%AD%BE%E5%90%8D&amp;editintro=%E6%A8%A1%E6%9D%BF%3A%E7%AD%BE%E5%90%8D%E8%AF%B4%E6%98%8E&amp;preloadtitle=%E7%BB%99%E5%B8%B8%E8%A7%81%E5%8C%96%E9%AA%8C%E6%8C%87%E6%A0%87%E5%8F%8A%E6%84%8F%E4%B9%89%E6%9D%A1%E7%9B%AE%E7%9A%84%E7%95%99%E8%A8%80" class="external text" target="_blank">添加留言</a>
</td></tr></table>
<h2> <span class="mw-headline" id=".E6.9B.B4.E5.A4.9A.E5.8C.BB.E5.AD.A6.E7.99.BE.E7.A7.91.E6.9D.A1.E7.9B.AE">更多医学百科条目</span></h2>
				<!-- /bodytext -->
								<!-- catlinks -->
				<div id='catlinks' class='catlinks'><div id="mw-normal-catlinks"><a href="/w/%E7%89%B9%E6%AE%8A:%E9%A1%B5%E9%9D%A2%E5%88%86%E7%B1%BB" title="特殊:页面分类">1个分类</a>: <span dir='ltr'><a href="/w/%E5%88%86%E7%B1%BB:%E6%A3%80%E9%AA%8C%E5%8C%BB%E5%AD%A6" title="分类:检验医学">检验医学</a></span></div></div>				<!-- /catlinks -->
												<div class="visualClear"></div>
			</div>
			<!-- /bodyContent -->
		</div>
		<!-- /content -->
		<!-- header -->
		<div id="mw-head" class="noprint">
			
<!-- 0 -->
<div id="p-personal" class="">
	<h5>个人工具</h5>
	<ul>
					<li  id="pt-login"><a href="/index.php?title=%E7%89%B9%E6%AE%8A:%E7%94%A8%E6%88%B7%E7%99%BB%E5%BD%95&amp;returnto=%E5%B8%B8%E8%A7%81%E5%8C%96%E9%AA%8C%E6%8C%87%E6%A0%87%E5%8F%8A%E6%84%8F%E4%B9%89" title="我们鼓励您登录，但这并不是必须的 [o]" accesskey="o" rel="nofollow">登录／创建账户</a></li>
			</ul>
</div>

<!-- /0 -->
			<div id="left-navigation">
				
<!-- 0 -->
<div id="p-namespaces" class="vectorTabs">
	<h5>名字空间</h5>
	<ul>
					<li  id="ca-nstab-main" class="selected"><a href="/w/%E5%B8%B8%E8%A7%81%E5%8C%96%E9%AA%8C%E6%8C%87%E6%A0%87%E5%8F%8A%E6%84%8F%E4%B9%89" rel="nofollow"  title="查看页面内容 [c]" accesskey="c"><span>页面</span></a></li>
					<li  id="ca-talk"><a href="/w/%E8%AE%A8%E8%AE%BA:%E5%B8%B8%E8%A7%81%E5%8C%96%E9%AA%8C%E6%8C%87%E6%A0%87%E5%8F%8A%E6%84%8F%E4%B9%89" rel="nofollow"  title="关于页面正文的讨论 [t]" accesskey="t"><span>讨论</span></a></li>
			</ul>
</div>

<!-- /0 -->

<!-- 1 -->

<!-- /1 -->
			</div>
			<div id="right-navigation">
				
<!-- 0 -->
<div id="p-views" class="vectorTabs">
	<h5>查看</h5>
	<ul>
					<li id="ca-view" class="selected"><a href="/w/%E5%B8%B8%E8%A7%81%E5%8C%96%E9%AA%8C%E6%8C%87%E6%A0%87%E5%8F%8A%E6%84%8F%E4%B9%89" rel="nofollow"><span>阅读</span></a></li>
					<li id="ca-trans"><a href="http://cht.a-hospital.com/w/%E5%B8%B8%E8%A7%81%E5%8C%96%E9%AA%8C%E6%8C%87%E6%A0%87%E5%8F%8A%E6%84%8F%E4%B9%89" rel="alternate" hreflang="zh-Hant"><span>繁体/正体</span></a></li>
					<li id="ca-viewsource"><a href="/index.php?title=%E5%B8%B8%E8%A7%81%E5%8C%96%E9%AA%8C%E6%8C%87%E6%A0%87%E5%8F%8A%E6%84%8F%E4%B9%89&amp;action=edit" rel="nofollow" title="修正、补充或整理本条目。 [e]" accesskey="e"><span>编辑修改</span></a></li>
					<li id="ca-history" class="collapsible "><a href="/index.php?title=%E5%B8%B8%E8%A7%81%E5%8C%96%E9%AA%8C%E6%8C%87%E6%A0%87%E5%8F%8A%E6%84%8F%E4%B9%89&amp;action=history" rel="nofollow" title="此页面的早前修订版本 [h]" accesskey="h"><span>修订历史</span></a></li>
			</ul>
</div>

<!-- /0 -->

<!-- 1 -->
<div id="p-cactions" class="vectorMenu emptyPortlet">
	<h5><span>动作</span><a href="#"></a></h5>
	<div class="menu">
		<ul>
					</ul>
	</div>
</div>

<!-- /1 -->

<!-- 2 -->
<div id="p-search">
	<h5><label for="searchInput">搜索</label></h5>
	<form action="/index.php" id="searchform">
		<input type='hidden' name="title" value="特殊:搜索"/>
		<div id="simpleSearch">
							<input id="searchInput"  onfocus="if (this.value == '搜索') {this.value = '';}" onblur="if (this.value == '') {this.value = '搜索';}" name="search" type="text"  title="搜索该网站 [f]" accesskey="f"  value="搜索"  />
						<button id="searchButton" type='submit' name='button'  title="搜索该文字的页面">&nbsp;</button>
		</div>
	</form>
</div>

<!-- /2 -->
			</div>
		</div>
		<!-- /header -->
		<!-- panel -->
			<div id="mw-panel" class="noprint">
				<!-- logo -->
					<div id="p-logo"><a style="background-image: url(http://s.ayxbk.com/common/images/logo.png);" href="/w/%E9%A6%96%E9%A1%B5"  title="访问首页"></a></div>
				<!-- /logo -->
				  
<div class="portal" id='p-navigation'>
	<h5>导航</h5>
	<div class="body">
				<ul>
					<li><a href="/w/%E9%A6%96%E9%A1%B5" title="访问首页 [z]" accesskey="z">首页</a></li>
					<li><a href="/w/%E5%A4%A7%E5%8C%BB%E7%B2%BE%E8%AF%9A">大医精诚</a></li>
					<li><a href="/w/%E4%BA%BA%E4%BD%93%E7%A9%B4%E4%BD%8D%E5%9B%BE">人体穴位图</a></li>
					<li><a href="/w/%E4%B8%AD%E8%8D%AF%E5%9B%BE%E5%85%B8">中药图典</a></li>
					<li><a href="/w/%E5%85%A8%E5%9B%BD%E5%8C%BB%E9%99%A2%E5%88%97%E8%A1%A8">全国医院列表</a></li>
					<li><a href="/w/%E5%8C%BB%E5%AD%A6%E7%94%B5%E5%AD%90%E4%B9%A6">医学电子书</a></li>
					<li><a href="/w/%E8%8D%AF%E5%93%81">药品百科</a></li>
					<li><a href="/w/%E4%B8%AD%E5%8C%BB">中医百科</a></li>
					<li><a href="/w/%E7%96%BE%E7%97%85%E8%AF%8A%E6%96%AD">疾病诊断</a></li>
					<li><a href="/w/%E6%80%A5%E6%95%91%E5%B8%B8%E8%AF%86">急救常识</a></li>
					<li><a href="/w/%E7%96%BE%E7%97%85">疾病查询</a></li>
					<li><a href="/w/%E4%B8%AD%E8%8D%AF">中药百科</a></li>
					<li><a href="/w/%E4%B8%AD%E8%8D%AF%E6%96%B9%E5%89%82">中医方剂大全</a></li>
					<li><a href="/w/%E6%80%8E%E6%A0%B7%E7%9C%8B%E5%8C%96%E9%AA%8C%E5%8D%95">怎样看化验单</a></li>
					<li><a href="/w/%E5%85%A8%E5%9B%BD%E5%88%B6%E8%8D%AF%E4%BC%81%E4%B8%9A%E5%88%97%E8%A1%A8">全国制药企业</a></li>
					<li><a href="/w/%E5%85%A8%E5%9B%BD%E5%8C%BB%E7%A7%91%E9%99%A2%E6%A0%A1%E5%88%97%E8%A1%A8">医科院校大全</a></li>
					<li><a href="/w/%E5%8C%BB%E4%BA%8B%E6%BC%AB%E8%B0%88">医事漫谈</a></li>
					<li><a href="/w/%E5%8C%BB%E5%AD%A6%E4%B8%8B%E8%BD%BD">医学下载</a></li>
					<li><a href="/w/%E5%8C%BB%E5%AD%A6%E8%A7%86%E9%A2%91">医学视频</a></li>
				</ul>
			</div>
</div>
  
<div class="portal" id='p-.E6.8E.A8.E8.8D.90.E5.B7.A5.E5.85.B7'>
	<h5>推荐工具</h5>
	<div class="body">
				<ul>
					<li><a href="http://www.adaohang.com/health.html">医学网站大全</a></li>
					<li><a href="http://www.mcd8.com/">医学词典</a></li>
					<li><a href="http://blog.a-hospital.com/">医学资讯博客</a></li>
				</ul>
			</div>
</div>
  
<div class="portal" id='p-.E5.8A.9F.E8.83.BD.E8.8F.9C.E5.8D.95'>
	<h5>功能菜单</h5>
	<div class="body">
				<ul>
					<li><a href="/w/A%2B%E5%8C%BB%E5%AD%A6%E7%99%BE%E7%A7%91:%E6%B7%BB%E5%8A%A0%E6%9D%A1%E7%9B%AE" rel="nofollow">添加页面</a></li>
					<li><a href="/w/A%2B%E5%8C%BB%E5%AD%A6%E7%99%BE%E7%A7%91:%E6%8B%9B%E5%8B%9F%E7%99%BE%E7%A7%91%E5%BF%97%E6%84%BF%E8%80%85" rel="nofollow">志愿者招募中</a></li>
					<li><a href="/w/%E7%89%B9%E6%AE%8A:ContributionScores" rel="nofollow">积分排名</a></li>
					<li><a href="/w/A%2B%E5%8C%BB%E5%AD%A6%E7%99%BE%E7%A7%91:%E5%85%B3%E4%BA%8E%E5%B9%BF%E5%91%8A" rel="nofollow">关于广告</a></li>
					<li><a href="/w/A%2B%E5%8C%BB%E5%AD%A6%E7%99%BE%E7%A7%91:%E7%BD%91%E7%AB%99%E4%BA%8B%E5%8A%A1">网站事务</a></li>
					<li><a href="/w/%E7%89%B9%E6%AE%8A:%E6%9C%80%E8%BF%91%E6%9B%B4%E6%94%B9" title="列出该网站的最近修改 [r]" accesskey="r">最近更改</a></li>
				</ul>
			</div>
</div>
<div class="portal" id="p-tb">
	<h5>工具箱</h5>
	<div class="body">
		<ul>
					<li id="t-whatlinkshere"><a href="/w/%E7%89%B9%E6%AE%8A:%E9%93%BE%E5%85%A5%E9%A1%B5%E9%9D%A2/%E5%B8%B8%E8%A7%81%E5%8C%96%E9%AA%8C%E6%8C%87%E6%A0%87%E5%8F%8A%E6%84%8F%E4%B9%89" title="列出所有与此页相链的页面 [j]" accesskey="j">链入页面</a></li>
						<li id="t-recentchangeslinked"><a href="/w/%E7%89%B9%E6%AE%8A:%E9%93%BE%E5%87%BA%E6%9B%B4%E6%94%B9/%E5%B8%B8%E8%A7%81%E5%8C%96%E9%AA%8C%E6%8C%87%E6%A0%87%E5%8F%8A%E6%84%8F%E4%B9%89" title="从此页链出的所有页面的更改 [k]" accesskey="k">链出更改</a></li>
																																												<li id="t-specialpages"><a href="/w/%E7%89%B9%E6%AE%8A:%E7%89%B9%E6%AE%8A%E9%A1%B5%E9%9D%A2" title="所有特殊页面列表 [q]" accesskey="q">所有特殊页面</a></li>
									<li id="t-print"><a href="/index.php?title=%E5%B8%B8%E8%A7%81%E5%8C%96%E9%AA%8C%E6%8C%87%E6%A0%87%E5%8F%8A%E6%84%8F%E4%B9%89&amp;printable=yes" rel="nofollow" title="这个页面的可打印版本 [p]" accesskey="p">可打印版</a></li>
						</ul>
	</div>
</div>
			</div>
		<!-- /panel -->
		<!-- footer -->
		<div id="footer">
											<ul id="footer-info">
																	<li id="footer-info-credits">此页由A+医学百科用户<a rel="nofollow" href="/w/%E7%94%A8%E6%88%B7:%E5%8C%BB%E8%80%85" title="用户:医者">医者</a>于2019年6月8日 (星期六) 10:34最后更改。 在<a rel="nofollow" href="/index.php?title=%E7%94%A8%E6%88%B7:Lydy&amp;action=edit&amp;redlink=1" class="new" title="用户:Lydy（尚未撰写）" rel="nofollow">免责声明</a>和<a rel="nofollow" href="/index.php?title=%E7%94%A8%E6%88%B7:Wailia&amp;action=edit&amp;redlink=1" class="new" title="用户:Wailia（尚未撰写）" rel="nofollow">中国</a>和A+医学百科用户<a rel="nofollow" href="/w/%E7%94%A8%E6%88%B7:%E8%A1%8C%E5%8C%BB" title="用户:行医">行医</a>的工作基础上。</li>
																							<li id="footer-info-copyright"><br />本站内容由网友添加和整理，仅供学习和参考。站内信息不一定准确、全面或最新。<br />
网站内容不应成为诊断或治疗疾病的最终依据。A+医学百科提醒网友，如有身体不适，请及时就医。<br />
本站的全部文本内容在<a rel="nofollow" href="/w/A%2B%E5%8C%BB%E5%AD%A6%E7%99%BE%E7%A7%91:%E7%89%88%E6%9D%83" title="A+医学百科:版权">知识共享 署名-相同方式共享 3.0协议</a>之条款下提供。<br /></li>
															</ul>
															<ul id="footer-places">
																	<li id="footer-places-privacy"><a rel="nofollow" href="/w/A%2B%E5%8C%BB%E5%AD%A6%E7%99%BE%E7%A7%91:%E9%9A%90%E7%A7%81%E6%94%BF%E7%AD%96" title="A+医学百科:隐私政策">隐私政策</a></li>
																							<li id="footer-places-about"><a rel="nofollow" href="/w/A%2B%E5%8C%BB%E5%AD%A6%E7%99%BE%E7%A7%91:%E5%85%B3%E4%BA%8E" title="A+医学百科:关于">关于A+医学百科</a></li>
																							<li id="footer-places-disclaimer"><a rel="nofollow" href="/w/A%2B%E5%8C%BB%E5%AD%A6%E7%99%BE%E7%A7%91:%E5%85%8D%E8%B4%A3%E5%A3%B0%E6%98%8E" title="A+医学百科:免责声明">免责声明</a></li>
															</ul>
										<div style="clear:both"></div>
		</div>
		<!-- /footer -->
						<script>window._bd_share_config={"common":{"bdSign":"off","bdSnsKey":{},"bdText":"","bdMini":"2","bdMiniList":false,"bdPic":"","bdStyle":"0","bdSize":"32"},"share":{},"image":{"viewList":["qzone","weixin","tqq","tsina","fbook"],"viewText":"分享到：","viewSize":"16"},"selectShare":{"bdContainerClass":null,"bdSelectMiniList":["qzone","weixin","tqq","tsina","fbook"]}};with(document)0[(getElementsByTagName('head')[0]||body).appendChild(createElement('script')).src='http://bdimg.share.baidu.com/static/api/js/share.js?v=89860593.js?cdnversion='+~(-new Date()/36e5)];</script>
				
<script>
var skin="vector",
stylepath="http://s.ayxbk.com",
wgUrlProtocols="http\\:\\/\\/|https\\:\\/\\/|ftp\\:\\/\\/|irc\\:\\/\\/|mailto\\:",
wgArticlePath="/w/$1",
wgScriptPath="",
wgScriptExtension=".php",
wgScript="/index.php",
wgVariantArticlePath=false,
wgActionPaths={},
wgServer="http://www.a-hospital.com",
wgCanonicalNamespace="",
wgCanonicalSpecialPageName=false,
wgNamespaceNumber=0,
wgPageName="常见化验指标及意义",
wgTitle="常见化验指标及意义",
wgAction="view",
wgArticleId=82939,
wgIsArticle=true,
wgUserName=null,
wgUserGroups=null,
wgUserLanguage="zh-hans",
wgContentLanguage="zh-hans",
wgBreakFrames=true,
wgCurRevisionId=545661,
wgVersion="1.16.0",
wgEnableAPI=true,
wgEnableWriteAPI=true,
wgSeparatorTransformTable=["", ""],
wgDigitTransformTable=["", ""],
wgMainPageTitle="首页",
wgFormattedNamespaces={"-2": "媒体", "-1": "特殊", "0": "", "1": "讨论", "2": "用户", "3": "用户讨论", "4": "A+医学百科", "5": "A+医学百科讨论", "6": "文件", "7": "文件讨论", "8": "MediaWiki", "9": "MediaWiki讨论", "10": "模板", "11": "模板讨论", "12": "帮助", "13": "帮助讨论", "14": "分类", "15": "分类讨论", "420": "Layer", "421": "Layer talk"},
wgSiteName="A+医学百科",
wgCategories=["检验医学"],
wgMWSuggestTemplate="http://www.a-hospital.com/api.php?action=opensearch\x26search={searchTerms}\x26namespace={namespaces}\x26suggest",
wgDBname="ahospital",
wgSearchNamespaces=[0],
wgMWSuggestMessages=["有建议", "无建议"],
wgRestrictionEdit=[],
wgRestrictionMove=[];
</script><script src="http://s.ayxbk.com/common/main-mini.js?278"></script>
<!--[if lt IE 7]><style type="text/css">body{behavior:url("http://s.ayxbk.com/vector/csshover.htc")}</style><![endif]-->
<script type="text/javascript">
window.google_analytics_uacct = "UA-1856547-6";
</script>
<script>if (window.runOnloadHook) runOnloadHook();</script>
<script type="text/javascript">
var gaJsHost = (("https:" == document.location.protocol) ? "https://ssl." : "http://www.");
document.write(unescape("%3Cscript src='" + gaJsHost + "google-analytics.com/ga.js' type='text/javascript'%3E%3C/script%3E"));
</script>
<script type="text/javascript">
var pageTracker = _gat._getTracker("UA-1856547-6");
pageTracker._initData();
pageTracker._trackPageview();
</script>		<script type="text/javascript"> if ( window.isMSIE55 ) fixalpha(); </script>
		<!-- Served in 0.383 secs. -->			</body>
<!-- Cached/compressed 20190608031138 -->
</html>
"""
    response = HtmlResponse(url='http://www.a-hospital.com/w/%E5%B8%B8%E8%A7%81%E5%8C%96%E9%AA%8C%E6%8C%87%E6%A0%87%E5%8F%8A%E6%84%8F%E4%B9%89',
                            body=body, encoding='utf8')
    ppl = AhospitalPipeline()
    spider = HospitalSpider() 
    ppl.open_spider(spider)
    resp_iter = spider.parse(response)
    page = next(resp_iter)
    assert page is not None
    assert not isinstance(page, AhospitalItem)
    # assert len(page.get("paragragh")) > 0

    next_url = next(resp_iter)
    assert isinstance(next_url, Request)

def test_spider2():
    body = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html lang="zh-hans" dir="ltr">
<head>
<title>白细胞分类计数 - A+医学百科</title>
<meta name="viewport" content="width=device-width, initial-scale=1" />
<meta name="applicable-device" content="pc,mobile" />
<meta http-equiv="Cache-Control" content="no-transform" />
<meta http-equiv="Cache-Control" content="no-siteapp" />
<meta name="generator" content="MediaWiki 1.16.0" />
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<link rel="canonical" href="/w/%E7%99%BD%E7%BB%86%E8%83%9E%E5%88%86%E7%B1%BB%E8%AE%A1%E6%95%B0" />
<link rel="apple-touch-icon" href="http://s.ayxbk.com/common/images/apple-touch-icon.png" />
<link rel="shortcut icon" href="http://s.ayxbk.com/favicon.ico" />
<link rel="search" type="application/opensearchdescription+xml" href="/opensearch_desc.php" title="A+医学百科 (zh-hans)" />
<link rel="copyright" href="/w/A%2B%E5%8C%BB%E5%AD%A6%E7%99%BE%E7%A7%91:%E7%89%88%E6%9D%83" />
<link rel="stylesheet" href="http://s.ayxbk.com/vector/main-mini.css?278" media="screen" />

</head>
<body class="mediawiki ltr ns-0 ns-subject page-白细胞分类计数 skin-vector">
		<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
		<script>
		     (adsbygoogle = window.adsbygoogle || []).push({
		          google_ad_client: "ca-pub-4174070858627065",
		          enable_page_level_ads: true
		     });
		</script>
		<div id="mw-page-base" class="noprint"></div>
		<div id="mw-head-base" class="noprint"></div>
		<!-- content -->
		<div id="content" >
			<a id="top"></a>
			<div id="mw-js-message" style="display:none;"></div>
						<!-- firstHeading -->
			<h1 id="firstHeading" class="firstHeading">白细胞分类计数</h1>
			<!-- /firstHeading -->
			<!-- bodyContent -->
			<div id="bodyContent">
				<!-- subtitle -->
				<div id="contentSub">（重定向自<a href="/index.php?title=DC&amp;redirect=no" title="DC">DC</a>）</div>
				<!-- /subtitle -->
																<!-- jumpto -->
				<div id="jump-to-nav">
					跳转到： <a href="#mw-head">导航</a>,
					<a href="#p-search">搜索</a>
				</div>
				<!-- /jumpto -->
								<!-- bodytext -->
				<table class="nav">

<tr>
<td><a href="/w/%E9%A6%96%E9%A1%B5" title="首页">A+医学百科</a> &gt;&gt; 白细胞分类计数
</td></tr></table>
<p><a href="/w/%E4%B8%AD%E5%9B%BD%E5%8D%AB%E7%94%9F%E9%83%A8" title="中国卫生部" class="mw-redirect">中国卫生部</a>医政司编的《<a href="/index.php?title=%E5%85%A8%E5%9B%BD%E4%B8%B4%E5%BA%8A%E6%A3%80%E9%AA%8C%E6%93%8D%E4%BD%9C%E8%A7%84%E7%A8%8B&amp;action=edit&amp;redlink=1" class="new" title="全国临床检验操作规程（尚未撰写）" rel="nofollow">全国临床检验操作规程</a>》，关于白细胞分类计数正常参考值如下：</p>
<table>
<tr>
<th>细胞类别　</th>
<th>成　人</th>
</tr>
<tr>
<td><a href="/w/%E4%B8%AD%E6%80%A7%E7%B2%92%E7%BB%86%E8%83%9E" title="中性粒细胞">中性粒细胞</a></td>
<td>法定比例　</td>
<td>百分率</td>
</tr>
<tr>
<td><a href="/index.php?title=%E6%9D%86%E7%8A%B6%E6%A0%B8&amp;action=edit&amp;redlink=1" class="new" title="杆状核（尚未撰写）" rel="nofollow">杆状核</a></td>
<td>0.01～0.05</td>
<td>1～5％</td>
</tr>
<tr>
<td><a href="/index.php?title=%E5%88%86%E5%8F%B6%E6%A0%B8&amp;action=edit&amp;redlink=1" class="new" title="分叶核（尚未撰写）" rel="nofollow">分叶核</a></td>
<td>0.50～0.70</td>
<td>50～70％</td>
</tr>
<tr>
<td><a href="/w/%E5%97%9C%E9%85%B8%E6%80%A7%E7%B2%92%E7%BB%86%E8%83%9E" title="嗜酸性粒细胞">嗜酸性粒细胞</a></td>
<td>0.005～0.05</td>
<td>0.5～5％</td>
</tr>
<tr>
<td><a href="/w/%E5%97%9C%E7%A2%B1%E6%80%A7%E7%B2%92%E7%BB%86%E8%83%9E" title="嗜碱性粒细胞">嗜碱性粒细胞</a></td>
<td>0～0.01</td>
<td>0～1％</td>
</tr>
<tr>
<td><a href="/w/%E6%B7%8B%E5%B7%B4%E7%BB%86%E8%83%9E" title="淋巴细胞">淋巴细胞</a></td>
<td>0.20～0.40</td>
<td>20～40％</td>
</tr>
<tr>
<td><a href="/w/%E5%8D%95%E6%A0%B8%E7%BB%86%E8%83%9E" title="单核细胞">单核细胞</a></td>
<td>0.03～0.08</td>
<td>3～8％</td>
</tr>
</table>
<h2><span class="mw-headline" id=".E7.99.BD.E7.BB.86.E8.83.9E.E5.88.86.E7.B1.BB.E8.AE.A1.E6.95.B0.E7.9A.84.E4.B8.B4.E5.BA.8A.E6.84.8F.E4.B9.89">白细胞分类计数的临床意义</span></h2>
<p>白细胞分类计数的临床意义如下：</p>
<ul>
<li><a href="/w/%E4%B8%AD%E6%80%A7%E7%B2%92%E7%BB%86%E8%83%9E" title="中性粒细胞">中性粒细胞</a>：增多和减少的临床意义与<a href="/w/%E7%99%BD%E7%BB%86%E8%83%9E%E8%AE%A1%E6%95%B0" title="白细胞计数">白细胞计数</a>相同。</li>
<li><a href="/w/%E5%97%9C%E9%85%B8%E6%80%A7%E7%B2%92%E7%BB%86%E8%83%9E" title="嗜酸性粒细胞">嗜酸性粒细胞</a>：增多见于<a href="/w/%E5%8F%98%E6%80%81%E5%8F%8D%E5%BA%94" title="变态反应">变态反应</a>，<a href="/w/%E5%AF%84%E7%94%9F%E8%99%AB%E7%97%85" title="寄生虫病">寄生虫病</a>、某些<a href="/w/%E7%9A%AE%E8%82%A4%E7%97%85" title="皮肤病">皮肤病</a>、创伤等；减少见于<a href="/w/%E4%BC%A4%E5%AF%92" title="伤寒">伤寒</a>、<a href="/w/%E5%89%AF%E4%BC%A4%E5%AF%92" title="副伤寒">副伤寒</a>、使用<a href="/w/%E8%82%BE%E4%B8%8A%E8%85%BA%E7%9A%AE%E8%B4%A8%E6%BF%80%E7%B4%A0" title="肾上腺皮质激素">肾上腺皮质激素</a>后。</li>
<li><a href="/w/%E5%97%9C%E7%A2%B1%E6%80%A7%E7%B2%92%E7%BB%86%E8%83%9E" title="嗜碱性粒细胞">嗜碱性粒细胞</a>：增多见于慢性粒细胞性<a href="/w/%E7%99%BD%E8%A1%80%E7%97%85" title="白血病">白血病</a>、<a href="/w/%E4%BD%95%E6%9D%B0%E9%87%91%E6%B0%8F%E7%97%85" title="何杰金氏病" class="mw-redirect">何杰金氏病</a>、<a href="/w/%E7%99%8C" title="癌" class="mw-redirect">癌</a>转移、<a href="/index.php?title=%E9%93%85%E9%93%8B%E4%B8%AD%E6%AF%92&amp;action=edit&amp;redlink=1" class="new" title="铅铋中毒（尚未撰写）" rel="nofollow">铅铋中毒</a>等。</li>
<li><a href="/w/%E6%B7%8B%E5%B7%B4%E7%BB%86%E8%83%9E" title="淋巴细胞">淋巴细胞</a>：增多见于<a href="/w/%E7%99%BE%E6%97%A5%E5%92%B3" title="百日咳">百日咳</a>、传染性<a href="/w/%E5%8D%95%E6%A0%B8%E7%BB%86%E8%83%9E%E5%A2%9E%E5%A4%9A%E7%97%87" title="单核细胞增多症" class="mw-redirect">单核细胞增多症</a>，慢性淋巴细胞性<a href="/w/%E7%99%BD%E8%A1%80%E7%97%85" title="白血病">白血病</a>，<a href="/w/%E9%BA%BB%E7%96%B9" title="麻疹">麻疹</a>、<a href="/w/%E8%85%AE%E8%85%BA%E7%82%8E" title="腮腺炎">腮腺炎</a>、<a href="/w/%E7%BB%93%E6%A0%B8" title="结核">结核</a>、传染性<a href="/w/%E8%82%9D%E7%82%8E" title="肝炎">肝炎</a>；减少多见于传染急性期、<a href="/w/%E6%94%BE%E5%B0%84%E7%97%85" title="放射病">放射病</a>、<a href="/index.php?title=%E7%BB%86%E8%83%9E%E5%85%8D%E7%96%AB%E7%BC%BA%E9%99%B7&amp;action=edit&amp;redlink=1" class="new" title="细胞免疫缺陷（尚未撰写）" rel="nofollow">细胞免疫缺陷</a>等。</li>
<li><a href="/w/%E5%8D%95%E6%A0%B8%E7%BB%86%E8%83%9E" title="单核细胞">单核细胞</a>：增多见于<a href="/w/%E7%BB%93%E6%A0%B8" title="结核">结核</a>、<a href="/w/%E4%BC%A4%E5%AF%92" title="伤寒">伤寒</a>、<a href="/w/%E7%96%9F%E7%96%BE" title="疟疾">疟疾</a>、<a href="/w/%E9%BB%91%E7%83%AD%E7%97%85" title="黑热病">黑热病</a>、急性传染病恢复期，单核细胞性<a href="/w/%E7%99%BD%E8%A1%80%E7%97%85" title="白血病">白血病</a>、亚急性感染性<a href="/w/%E5%BF%83%E5%86%85%E8%86%9C%E7%82%8E" title="心内膜炎">心内膜炎</a>等；减少无意义。</li>
</ul>
<h2><span class="mw-headline" id=".E5.8F.82.E7.9C.8B">参看</span></h2>
<ul>
<li><a href="/w/%E5%9F%BA%E7%A1%80%E6%A3%80%E9%AA%8C%E5%AD%A6/%E7%99%BD%E7%BB%86%E8%83%9E%E5%88%86%E7%B1%BB%E8%AE%A1%E6%95%B0" title="基础检验学/白细胞分类计数">《临床基础检验学》- 白细胞分类计数</a></li>
<li><a href="/w/%E7%99%BD%E7%BB%86%E8%83%9E%E8%AE%A1%E6%95%B0" title="白细胞计数">白细胞计数</a></li>
<li><a href="/w/%E7%99%BD%E7%BB%86%E8%83%9E" title="白细胞">白细胞</a></li>
</ul>
<h2><span class="mw-headline" id=".E6.80.8E.E6.A0.B7.E7.9C.8B.E5.8C.96.E9.AA.8C.E5.8D.95.E4.B8.93.E9.A2.98">怎样看化验单专题</span></h2>
<p>专题主页<a href="/w/%E6%80%8E%E6%A0%B7%E7%9C%8B%E5%8C%96%E9%AA%8C%E5%8D%95" title="怎样看化验单">怎样看化验单</a>, <a href="/w/%E7%96%BE%E7%97%85%E8%AF%8A%E6%96%AD" title="疾病诊断">疾病诊断</a></p>
<p>关于医学化验单：</p>
<ul>
<li><a href="/w/%E5%B8%B8%E8%A7%81%E5%8C%96%E9%AA%8C%E6%8C%87%E6%A0%87%E5%8F%8A%E6%84%8F%E4%B9%89" title="常见化验指标及意义">常见化验指标及意义</a></li>
<li><a href="/w/%E6%80%8E%E6%A0%B7%E7%90%86%E8%A7%A3%E6%A3%80%E9%AA%8C%E7%BB%93%E6%9E%9C" title="怎样理解检验结果">怎样理解检验结果‎</a></li>
<li><a href="/w/%E6%80%8E%E6%A0%B7%E7%9C%8B%E5%8C%96%E9%AA%8C%E5%8D%95%E4%B8%8A%E7%9A%84%E5%8A%A0%E5%8F%B7%E5%92%8C%E5%87%8F%E5%8F%B7" title="怎样看化验单上的加号和减号">怎样看化验单上的加号和减号</a></li>
</ul>
<p>常见的化验单：</p>
<ul>
<li><a href="/w/%E6%80%8E%E6%A0%B7%E7%9C%8B%E8%A1%80%E5%B8%B8%E8%A7%84%E5%8C%96%E9%AA%8C%E5%8D%95" title="怎样看血常规化验单">怎样看血常规化验单</a></li>
<li><a href="/w/%E5%A6%82%E4%BD%95%E7%9C%8B%E4%B9%99%E8%82%9D%E4%B8%A4%E5%AF%B9%E5%8D%8A%E5%8C%96%E9%AA%8C%E5%8D%95" title="如何看乙肝两对半化验单">如何看乙肝两对半化验单</a></li>
<li><a href="/w/%E6%80%8E%E6%A0%B7%E7%9C%8B%E8%82%9D%E5%8A%9F%E8%83%BD%E5%8C%96%E9%AA%8C%E5%8D%95" title="怎样看肝功能化验单">怎样看肝功能化验单</a></li>
<li><a href="/w/%E6%80%8E%E6%A0%B7%E7%9C%8B%E7%B3%96%E5%B0%BF%E7%97%85%E6%A3%80%E9%AA%8C%E5%8D%95" title="怎样看糖尿病检验单">怎样看糖尿病检验单</a></li>
<li><a href="/w/%E5%A6%82%E4%BD%95%E7%9C%8B%E5%B0%BF%E5%B8%B8%E8%A7%84%E6%A3%80%E6%9F%A5%E5%8C%96%E9%AA%8C%E5%8D%95" title="如何看尿常规检查化验单">如何看尿常规检查化验单</a></li>
<li><a href="/w/%E6%80%8E%E6%A0%B7%E7%9C%8B%E7%B2%AA%E4%BE%BF%E5%B8%B8%E8%A7%84%E6%A3%80%E6%9F%A5%E5%8C%96%E9%AA%8C%E5%8D%95" title="怎样看粪便常规检查化验单">怎样看粪便常规检查化验单</a></li>
<li><a href="/w/%E6%80%8E%E6%A0%B7%E7%9C%8B%E5%89%8D%E5%88%97%E8%85%BA%E6%B6%B2%E5%8C%96%E9%AA%8C%E5%8D%95" title="怎样看前列腺液化验单">怎样看前列腺液化验单</a></li>
<li><a href="/w/%E5%A6%82%E4%BD%95%E7%9C%8B%E8%82%BE%E5%8A%9F%E8%83%BD%E6%A3%80%E6%B5%8B%E5%8C%96%E9%AA%8C%E7%BB%93%E6%9E%9C" title="如何看肾功能检测化验结果">如何看肾功能检测化验结果</a></li>
<li><a href="/w/%E6%80%8E%E6%A0%B7%E7%9C%8B%E7%BB%93%E6%A0%B8%E8%8F%8C%E7%B4%A0%E7%9A%AE%E8%AF%95%E7%BB%93%E6%9E%9C" title="怎样看结核菌素皮试结果">怎样看结核菌素皮试结果</a></li>
<li><a href="/w/%E6%80%8E%E6%A0%B7%E7%9C%8B%E8%84%91%E8%84%8A%E6%B6%B2%E5%B8%B8%E8%A7%84%E6%A3%80%E5%8C%96%E9%AA%8C%E5%8D%95" title="怎样看脑脊液常规检化验单">怎样看脑脊液常规检化验单</a></li>
<li><a href="/w/%E6%80%8E%E6%A0%B7%E7%9C%8B%E6%B5%86%E8%86%9C%E8%85%94%E6%B6%B2%E6%A3%80%E9%AA%8C%E7%BB%93%E6%9E%9C" title="怎样看浆膜腔液检验结果">怎样看浆膜腔液检验结果</a></li>
<li><a href="/w/%E6%80%8E%E6%A0%B7%E7%9C%8B%E8%A1%80%E6%B0%94%E5%88%86%E6%9E%90%E7%BB%93%E6%9E%9C" title="怎样看血气分析结果">怎样看血气分析结果</a></li>
</ul>

<!-- 
NewPP limit report
Preprocessor node count: 10/1000000
Post-expand include size: 746/2097152 bytes
Template argument size: 0/2097152 bytes
Expensive parser function count: 0/100
-->

<!-- Saved in parser cache with key ahospital:pcache:idhash:534-0!1!0!!zh-hans!2!edit=0 and timestamp 20230708134146 -->
<div id="fromlink">出自A+医学百科 “白细胞分类计数”条目 <a href="http://www.a-hospital.com/w/%E7%99%BD%E7%BB%86%E8%83%9E%E5%88%86%E7%B1%BB%E8%AE%A1%E6%95%B0" class="external free" target="_blank">http://www.a-hospital.com/w/%E7%99%BD%E7%BB%86%E8%83%9E%E5%88%86%E7%B1%BB%E8%AE%A1%E6%95%B0</a> 转载请保留此链接</div><div class="bdsharebuttonbox"><a href="#" class="bds_qzone" data-cmd="qzone" title="分享到QQ空间"></a><a href="#" class="bds_weixin" data-cmd="weixin" title="分享到微信"></a><a href="#" class="bds_tqq" data-cmd="tqq" title="分享到腾讯微博"></a><a href="#" class="bds_tsina" data-cmd="tsina" title="分享到新浪微博"></a><a href="#" class="bds_fbook" data-cmd="fbook" title="分享到Facebook"></a><a href="#" class="bds_copy" data-cmd="copy" title="分享到复制网址"></a><a href="#" class="bds_more" data-cmd="more"></a><a href="#" class="bds_count" data-cmd="count"></a></div>
<table class="msg-table">

<tr style="background-color:rgb(206, 223, 242);">
<td><b>关于“<strong class="selflink">白细胞分类计数</strong>”的留言：</b>
</td><td align="right"><img alt="Feed-icon.png" src="http://p.ayxbk.com/images/f/f4/Feed-icon.png" width="12" height="12" /> <a href="http://www.a-hospital.com/index.php?title=%E8%AE%A8%E8%AE%BA:%E7%99%BD%E7%BB%86%E8%83%9E%E5%88%86%E7%B1%BB%E8%AE%A1%E6%95%B0&amp;feed=rss&amp;action=history" class="external text" target="_blank">订阅讨论RSS</a>
</td></tr>
<tr>
<td colspan="2" style="background-color:#ffffff;">
<p>目前暂无留言
</p>
</td></tr>
<tr>
<td colspan="2"><a href="http://www.a-hospital.com/index.php?title=%E8%AE%A8%E8%AE%BA:%E7%99%BD%E7%BB%86%E8%83%9E%E5%88%86%E7%B1%BB%E8%AE%A1%E6%95%B0&amp;action=edit&amp;section=new&amp;preload=%E6%A8%A1%E6%9D%BF%3A%E7%AD%BE%E5%90%8D&amp;editintro=%E6%A8%A1%E6%9D%BF%3A%E7%AD%BE%E5%90%8D%E8%AF%B4%E6%98%8E&amp;preloadtitle=%E7%BB%99%E7%99%BD%E7%BB%86%E8%83%9E%E5%88%86%E7%B1%BB%E8%AE%A1%E6%95%B0%E6%9D%A1%E7%9B%AE%E7%9A%84%E7%95%99%E8%A8%80" class="external text" target="_blank">添加留言</a>
</td></tr></table>
<h2> <span class="mw-headline" id=".E6.9B.B4.E5.A4.9A.E5.8C.BB.E5.AD.A6.E7.99.BE.E7.A7.91.E6.9D.A1.E7.9B.AE">更多医学百科条目</span></h2>
				<!-- /bodytext -->
								<!-- catlinks -->
				<div id='catlinks' class='catlinks'><div id="mw-normal-catlinks"><a href="/w/%E7%89%B9%E6%AE%8A:%E9%A1%B5%E9%9D%A2%E5%88%86%E7%B1%BB" title="特殊:页面分类">2个分类</a>: <span dir='ltr'><a href="/w/%E5%88%86%E7%B1%BB:%E6%A3%80%E6%9F%A5" title="分类:检查">检查</a></span> | <span dir='ltr'><a href="/w/%E5%88%86%E7%B1%BB:%E6%A3%80%E9%AA%8C%E5%8C%BB%E5%AD%A6" title="分类:检验医学">检验医学</a></span></div></div>				<!-- /catlinks -->
												<div class="visualClear"></div>
			</div>
			<!-- /bodyContent -->
		</div>
		<!-- /content -->
		<!-- header -->
		<div id="mw-head" class="noprint">
			
<!-- 0 -->
<div id="p-personal" class="">
	<h5>个人工具</h5>
	<ul>
					<li  id="pt-login"><a href="/index.php?title=%E7%89%B9%E6%AE%8A:%E7%94%A8%E6%88%B7%E7%99%BB%E5%BD%95&amp;returnto=%E7%99%BD%E7%BB%86%E8%83%9E%E5%88%86%E7%B1%BB%E8%AE%A1%E6%95%B0" title="我们鼓励您登录，但这并不是必须的 [o]" accesskey="o" rel="nofollow">登录／创建账户</a></li>
			</ul>
</div>

<!-- /0 -->
			<div id="left-navigation">
				
<!-- 0 -->
<div id="p-namespaces" class="vectorTabs">
	<h5>名字空间</h5>
	<ul>
					<li  id="ca-nstab-main" class="selected"><a href="/w/%E7%99%BD%E7%BB%86%E8%83%9E%E5%88%86%E7%B1%BB%E8%AE%A1%E6%95%B0" rel="nofollow"  title="查看页面内容 [c]" accesskey="c"><span>页面</span></a></li>
					<li  id="ca-talk" class="new"><a href="/index.php?title=%E8%AE%A8%E8%AE%BA:%E7%99%BD%E7%BB%86%E8%83%9E%E5%88%86%E7%B1%BB%E8%AE%A1%E6%95%B0&amp;action=edit&amp;redlink=1" rel="nofollow"  title="关于页面正文的讨论 [t]" accesskey="t"><span>讨论</span></a></li>
			</ul>
</div>

<!-- /0 -->

<!-- 1 -->

<!-- /1 -->
			</div>
			<div id="right-navigation">
				
<!-- 0 -->
<div id="p-views" class="vectorTabs">
	<h5>查看</h5>
	<ul>
					<li id="ca-view" class="selected"><a href="/w/%E7%99%BD%E7%BB%86%E8%83%9E%E5%88%86%E7%B1%BB%E8%AE%A1%E6%95%B0" rel="nofollow"><span>阅读</span></a></li>
					<li id="ca-trans"><a href="http://cht.a-hospital.com/w/%E7%99%BD%E7%BB%86%E8%83%9E%E5%88%86%E7%B1%BB%E8%AE%A1%E6%95%B0" rel="alternate" hreflang="zh-Hant"><span>繁体/正体</span></a></li>
					<li id="ca-viewsource"><a href="/index.php?title=%E7%99%BD%E7%BB%86%E8%83%9E%E5%88%86%E7%B1%BB%E8%AE%A1%E6%95%B0&amp;action=edit" rel="nofollow" title="修正、补充或整理本条目。 [e]" accesskey="e"><span>编辑修改</span></a></li>
					<li id="ca-history" class="collapsible "><a href="/index.php?title=%E7%99%BD%E7%BB%86%E8%83%9E%E5%88%86%E7%B1%BB%E8%AE%A1%E6%95%B0&amp;action=history" rel="nofollow" title="此页面的早前修订版本 [h]" accesskey="h"><span>修订历史</span></a></li>
			</ul>
</div>

<!-- /0 -->

<!-- 1 -->
<div id="p-cactions" class="vectorMenu emptyPortlet">
	<h5><span>动作</span><a href="#"></a></h5>
	<div class="menu">
		<ul>
					</ul>
	</div>
</div>

<!-- /1 -->

<!-- 2 -->
<div id="p-search">
	<h5><label for="searchInput">搜索</label></h5>
	<form action="/index.php" id="searchform">
		<input type='hidden' name="title" value="特殊:搜索"/>
		<div id="simpleSearch">
							<input id="searchInput"  onfocus="if (this.value == '搜索') {this.value = '';}" onblur="if (this.value == '') {this.value = '搜索';}" name="search" type="text"  title="搜索该网站 [f]" accesskey="f"  value="搜索"  />
						<button id="searchButton" type='submit' name='button'  title="搜索该文字的页面">&nbsp;</button>
		</div>
	</form>
</div>

<!-- /2 -->
			</div>
		</div>
		<!-- /header -->
		<!-- panel -->
			<div id="mw-panel" class="noprint">
				<!-- logo -->
					<div id="p-logo"><a style="background-image: url(http://s.ayxbk.com/common/images/logo.png);" href="/w/%E9%A6%96%E9%A1%B5"  title="访问首页"></a></div>
				<!-- /logo -->
				  
<div class="portal" id='p-navigation'>
	<h5>导航</h5>
	<div class="body">
				<ul>
					<li><a href="/w/%E9%A6%96%E9%A1%B5" title="访问首页 [z]" accesskey="z">首页</a></li>
					<li><a href="/w/%E5%A4%A7%E5%8C%BB%E7%B2%BE%E8%AF%9A">大医精诚</a></li>
					<li><a href="/w/%E4%BA%BA%E4%BD%93%E7%A9%B4%E4%BD%8D%E5%9B%BE">人体穴位图</a></li>
					<li><a href="/w/%E4%B8%AD%E8%8D%AF%E5%9B%BE%E5%85%B8">中药图典</a></li>
					<li><a href="/w/%E5%85%A8%E5%9B%BD%E5%8C%BB%E9%99%A2%E5%88%97%E8%A1%A8">全国医院列表</a></li>
					<li><a href="/w/%E5%8C%BB%E5%AD%A6%E7%94%B5%E5%AD%90%E4%B9%A6">医学电子书</a></li>
					<li><a href="/w/%E8%8D%AF%E5%93%81">药品百科</a></li>
					<li><a href="/w/%E4%B8%AD%E5%8C%BB">中医百科</a></li>
					<li><a href="/w/%E7%96%BE%E7%97%85%E8%AF%8A%E6%96%AD">疾病诊断</a></li>
					<li><a href="/w/%E6%80%A5%E6%95%91%E5%B8%B8%E8%AF%86">急救常识</a></li>
					<li><a href="/w/%E7%96%BE%E7%97%85">疾病查询</a></li>
					<li><a href="/w/%E4%B8%AD%E8%8D%AF">中药百科</a></li>
					<li><a href="/w/%E4%B8%AD%E8%8D%AF%E6%96%B9%E5%89%82">中医方剂大全</a></li>
					<li><a href="/w/%E6%80%8E%E6%A0%B7%E7%9C%8B%E5%8C%96%E9%AA%8C%E5%8D%95">怎样看化验单</a></li>
					<li><a href="/w/%E5%85%A8%E5%9B%BD%E5%88%B6%E8%8D%AF%E4%BC%81%E4%B8%9A%E5%88%97%E8%A1%A8">全国制药企业</a></li>
					<li><a href="/w/%E5%85%A8%E5%9B%BD%E5%8C%BB%E7%A7%91%E9%99%A2%E6%A0%A1%E5%88%97%E8%A1%A8">医科院校大全</a></li>
					<li><a href="/w/%E5%8C%BB%E4%BA%8B%E6%BC%AB%E8%B0%88">医事漫谈</a></li>
					<li><a href="/w/%E5%8C%BB%E5%AD%A6%E4%B8%8B%E8%BD%BD">医学下载</a></li>
					<li><a href="/w/%E5%8C%BB%E5%AD%A6%E8%A7%86%E9%A2%91">医学视频</a></li>
				</ul>
			</div>
</div>
  
<div class="portal" id='p-.E6.8E.A8.E8.8D.90.E5.B7.A5.E5.85.B7'>
	<h5>推荐工具</h5>
	<div class="body">
				<ul>
					<li><a href="http://www.adaohang.com/health.html">医学网站大全</a></li>
					<li><a href="http://www.mcd8.com/">医学词典</a></li>
					<li><a href="http://blog.a-hospital.com/">医学资讯博客</a></li>
				</ul>
			</div>
</div>
  
<div class="portal" id='p-.E5.8A.9F.E8.83.BD.E8.8F.9C.E5.8D.95'>
	<h5>功能菜单</h5>
	<div class="body">
				<ul>
					<li><a href="/w/A%2B%E5%8C%BB%E5%AD%A6%E7%99%BE%E7%A7%91:%E6%B7%BB%E5%8A%A0%E6%9D%A1%E7%9B%AE" rel="nofollow">添加页面</a></li>
					<li><a href="/w/A%2B%E5%8C%BB%E5%AD%A6%E7%99%BE%E7%A7%91:%E6%8B%9B%E5%8B%9F%E7%99%BE%E7%A7%91%E5%BF%97%E6%84%BF%E8%80%85" rel="nofollow">志愿者招募中</a></li>
					<li><a href="/w/%E7%89%B9%E6%AE%8A:ContributionScores" rel="nofollow">积分排名</a></li>
					<li><a href="/w/A%2B%E5%8C%BB%E5%AD%A6%E7%99%BE%E7%A7%91:%E5%85%B3%E4%BA%8E%E5%B9%BF%E5%91%8A" rel="nofollow">关于广告</a></li>
					<li><a href="/w/A%2B%E5%8C%BB%E5%AD%A6%E7%99%BE%E7%A7%91:%E7%BD%91%E7%AB%99%E4%BA%8B%E5%8A%A1">网站事务</a></li>
					<li><a href="/w/%E7%89%B9%E6%AE%8A:%E6%9C%80%E8%BF%91%E6%9B%B4%E6%94%B9" title="列出该网站的最近修改 [r]" accesskey="r">最近更改</a></li>
				</ul>
			</div>
</div>
<div class="portal" id="p-tb">
	<h5>工具箱</h5>
	<div class="body">
		<ul>
					<li id="t-whatlinkshere"><a href="/w/%E7%89%B9%E6%AE%8A:%E9%93%BE%E5%85%A5%E9%A1%B5%E9%9D%A2/%E7%99%BD%E7%BB%86%E8%83%9E%E5%88%86%E7%B1%BB%E8%AE%A1%E6%95%B0" title="列出所有与此页相链的页面 [j]" accesskey="j">链入页面</a></li>
						<li id="t-recentchangeslinked"><a href="/w/%E7%89%B9%E6%AE%8A:%E9%93%BE%E5%87%BA%E6%9B%B4%E6%94%B9/%E7%99%BD%E7%BB%86%E8%83%9E%E5%88%86%E7%B1%BB%E8%AE%A1%E6%95%B0" title="从此页链出的所有页面的更改 [k]" accesskey="k">链出更改</a></li>
																																												<li id="t-specialpages"><a href="/w/%E7%89%B9%E6%AE%8A:%E7%89%B9%E6%AE%8A%E9%A1%B5%E9%9D%A2" title="所有特殊页面列表 [q]" accesskey="q">所有特殊页面</a></li>
									<li id="t-print"><a href="/index.php?title=%E7%99%BD%E7%BB%86%E8%83%9E%E5%88%86%E7%B1%BB%E8%AE%A1%E6%95%B0&amp;printable=yes" rel="nofollow" title="这个页面的可打印版本 [p]" accesskey="p">可打印版</a></li>
						</ul>
	</div>
</div>
			</div>
		<!-- /panel -->
		<!-- footer -->
		<div id="footer">
											<ul id="footer-info">
																	<li id="footer-info-credits">此页由A+医学百科用户<a rel="nofollow" href="/w/%E7%94%A8%E6%88%B7:%E8%A1%8C%E5%8C%BB" title="用户:行医">行医</a>于2011年9月19日 (星期一) 10:29最后更改。 </li>
																							<li id="footer-info-copyright"><br />本站内容由网友添加和整理，仅供学习和参考。站内信息不一定准确、全面或最新。<br />
网站内容不应成为诊断或治疗疾病的最终依据。A+医学百科提醒网友，如有身体不适，请及时就医。<br />
本站的全部文本内容在<a rel="nofollow" href="/w/A%2B%E5%8C%BB%E5%AD%A6%E7%99%BE%E7%A7%91:%E7%89%88%E6%9D%83" title="A+医学百科:版权">知识共享 署名-相同方式共享 3.0协议</a>之条款下提供。<br /></li>
															</ul>
															<ul id="footer-places">
																	<li id="footer-places-privacy"><a rel="nofollow" href="/w/A%2B%E5%8C%BB%E5%AD%A6%E7%99%BE%E7%A7%91:%E9%9A%90%E7%A7%81%E6%94%BF%E7%AD%96" title="A+医学百科:隐私政策">隐私政策</a></li>
																							<li id="footer-places-about"><a rel="nofollow" href="/w/A%2B%E5%8C%BB%E5%AD%A6%E7%99%BE%E7%A7%91:%E5%85%B3%E4%BA%8E" title="A+医学百科:关于">关于A+医学百科</a></li>
																							<li id="footer-places-disclaimer"><a rel="nofollow" href="/w/A%2B%E5%8C%BB%E5%AD%A6%E7%99%BE%E7%A7%91:%E5%85%8D%E8%B4%A3%E5%A3%B0%E6%98%8E" title="A+医学百科:免责声明">免责声明</a></li>
															</ul>
										<div style="clear:both"></div>
		</div>
		<!-- /footer -->
						<script>window._bd_share_config={"common":{"bdSign":"off","bdSnsKey":{},"bdText":"","bdMini":"2","bdMiniList":false,"bdPic":"","bdStyle":"0","bdSize":"32"},"share":{},"image":{"viewList":["qzone","weixin","tqq","tsina","fbook"],"viewText":"分享到：","viewSize":"16"},"selectShare":{"bdContainerClass":null,"bdSelectMiniList":["qzone","weixin","tqq","tsina","fbook"]}};with(document)0[(getElementsByTagName('head')[0]||body).appendChild(createElement('script')).src='http://bdimg.share.baidu.com/static/api/js/share.js?v=89860593.js?cdnversion='+~(-new Date()/36e5)];</script>
				
<script>
var skin="vector",
stylepath="http://s.ayxbk.com",
wgUrlProtocols="http\\:\\/\\/|https\\:\\/\\/|ftp\\:\\/\\/|irc\\:\\/\\/|mailto\\:",
wgArticlePath="/w/$1",
wgScriptPath="",
wgScriptExtension=".php",
wgScript="/index.php",
wgVariantArticlePath=false,
wgActionPaths={},
wgServer="http://www.a-hospital.com",
wgCanonicalNamespace="",
wgCanonicalSpecialPageName=false,
wgNamespaceNumber=0,
wgPageName="白细胞分类计数",
wgTitle="白细胞分类计数",
wgAction="view",
wgArticleId=534,
wgIsArticle=true,
wgUserName=null,
wgUserGroups=null,
wgUserLanguage="zh-hans",
wgContentLanguage="zh-hans",
wgBreakFrames=true,
wgCurRevisionId=243124,
wgVersion="1.16.0",
wgEnableAPI=true,
wgEnableWriteAPI=true,
wgSeparatorTransformTable=["", ""],
wgDigitTransformTable=["", ""],
wgMainPageTitle="首页",
wgFormattedNamespaces={"-2": "媒体", "-1": "特殊", "0": "", "1": "讨论", "2": "用户", "3": "用户讨论", "4": "A+医学百科", "5": "A+医学百科讨论", "6": "文件", "7": "文件讨论", "8": "MediaWiki", "9": "MediaWiki讨论", "10": "模板", "11": "模板讨论", "12": "帮助", "13": "帮助讨论", "14": "分类", "15": "分类讨论", "420": "Layer", "421": "Layer talk"},
wgSiteName="A+医学百科",
wgCategories=["检查", "检验医学"],
wgMWSuggestTemplate="http://www.a-hospital.com/api.php?action=opensearch\x26search={searchTerms}\x26namespace={namespaces}\x26suggest",
wgDBname="ahospital",
wgSearchNamespaces=[0],
wgMWSuggestMessages=["有建议", "无建议"],
wgRestrictionEdit=[],
wgRestrictionMove=[];
</script><script src="http://s.ayxbk.com/common/main-mini.js?278"></script>
<!--[if lt IE 7]><style type="text/css">body{behavior:url("http://s.ayxbk.com/vector/csshover.htc")}</style><![endif]-->
<script type="text/javascript">
window.google_analytics_uacct = "UA-1856547-6";
</script>
<script>if (window.runOnloadHook) runOnloadHook();</script>
<script type="text/javascript">
var gaJsHost = (("https:" == document.location.protocol) ? "https://ssl." : "http://www.");
document.write(unescape("%3Cscript src='" + gaJsHost + "google-analytics.com/ga.js' type='text/javascript'%3E%3C/script%3E"));
</script>
<script type="text/javascript">
var pageTracker = _gat._getTracker("UA-1856547-6");
pageTracker._initData();
pageTracker._trackPageview();
</script>		<script type="text/javascript"> if ( window.isMSIE55 ) fixalpha(); </script>
		<!-- Served in 0.047 secs. -->			</body>
</html>
"""
    response = HtmlResponse(url='http://www.a-hospital.com/w/DC',
                            body=body, encoding='utf8')
    ppl = AhospitalPipeline()
    spider = HospitalSpider() 
    ppl.open_spider(spider)
    resp_iter = spider.parse(response)
    page = next(resp_iter)
    assert page is not None
    assert isinstance(page, AhospitalItem)
    assert len(page.get("paragragh")) > 0

    next_url = next(resp_iter)
    assert isinstance(next_url, Request)

def test_spider3():
    body = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html lang="zh-hans" dir="ltr">
<head>
<title>常见病自测 - A+医学百科</title>
<meta name="viewport" content="width=device-width, initial-scale=1" />
<meta name="applicable-device" content="pc,mobile" />
<meta http-equiv="Cache-Control" content="no-transform" />
<meta http-equiv="Cache-Control" content="no-siteapp" />
<meta name="generator" content="MediaWiki 1.16.0" />
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<link rel="apple-touch-icon" href="http://s.ayxbk.com/common/images/apple-touch-icon.png" />
<link rel="shortcut icon" href="http://s.ayxbk.com/favicon.ico" />
<link rel="search" type="application/opensearchdescription+xml" href="/opensearch_desc.php" title="A+医学百科 (zh-hans)" />
<link rel="copyright" href="/w/A%2B%E5%8C%BB%E5%AD%A6%E7%99%BE%E7%A7%91:%E7%89%88%E6%9D%83" />
<link rel="stylesheet" href="http://s.ayxbk.com/vector/main-mini.css?278" media="screen" />

</head>
<body class="mediawiki ltr ns-0 ns-subject page-常见病自测 skin-vector">
		<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
		<script>
		     (adsbygoogle = window.adsbygoogle || []).push({
		          google_ad_client: "ca-pub-4174070858627065",
		          enable_page_level_ads: true
		     });
		</script>
		<div id="mw-page-base" class="noprint"></div>
		<div id="mw-head-base" class="noprint"></div>
		<!-- content -->
		<div id="content" >
			<a id="top"></a>
			<div id="mw-js-message" style="display:none;"></div>
						<!-- firstHeading -->
			<h1 id="firstHeading" class="firstHeading">常见病自测</h1>
			<!-- /firstHeading -->
			<!-- bodyContent -->
			<div id="bodyContent">
				<!-- subtitle -->
				<div id="contentSub"></div>
				<!-- /subtitle -->
																<!-- jumpto -->
				<div id="jump-to-nav">
					跳转到： <a href="#mw-head">导航</a>,
					<a href="#p-search">搜索</a>
				</div>
				<!-- /jumpto -->
								<!-- bodytext -->
				<p></p>
<table width="100%" class="hierarchy-breadcrumb">
<tr>
<td width="95%" align="left nowrap"><small><a href="/w/%E5%8C%BB%E5%AD%A6%E7%94%B5%E5%AD%90%E4%B9%A6" title="医学电子书">医学电子书</a> &gt;&gt; 常见病自测</small></td>
</tr>
</table>
<table class="hierarchy-list" align="right">
<tr>
<td style="background: #cedff2; padding: 0.2em; white-space: nowrap;"><b><strong class="selflink">常见病自测</strong></b></td>
</tr>
<tr>
<td style="text-align:left; white-space: nowrap;">
<ul>
<li><a href="/w/%E5%B8%B8%E8%A7%81%E7%97%85%E8%87%AA%E6%B5%8B/%E5%B8%B8%E8%A7%81%E7%97%87%E7%8A%B6%E8%BE%A8%E7%97%85" title="常见病自测/常见症状辨病">常见症状辨病</a></li>
<li><a href="/w/%E5%B8%B8%E8%A7%81%E7%97%85%E8%87%AA%E6%B5%8B/%E7%A5%9E%E8%89%B2%E5%BD%A2%E6%80%81%E8%BE%A8%E7%97%85" title="常见病自测/神色形态辨病">神色形态辨病</a></li>
<li><a href="/w/%E5%B8%B8%E8%A7%81%E7%97%85%E8%87%AA%E6%B5%8B/%E8%A7%82%E5%AF%9F%E6%9C%BA%E4%BD%93%E5%B1%80%E9%83%A8%E8%BE%A8%E7%97%85" title="常见病自测/观察机体局部辨病">观察机体局部辨病</a></li>
<li><a href="/w/%E5%B8%B8%E8%A7%81%E7%97%85%E8%87%AA%E6%B5%8B/%E8%A7%82%E5%AF%9F%E5%88%86%E6%B3%8C%E7%89%A9%E6%8E%92%E6%B3%84%E7%89%A9%E8%BE%A8%E7%97%85" title="常见病自测/观察分泌物排泄物辨病">观察分泌物排泄物辨病</a></li>
<li><a href="/w/%E5%B8%B8%E8%A7%81%E7%97%85%E8%87%AA%E6%B5%8B/%E9%A5%AE%E9%A3%9F%E8%B5%B7%E5%B1%85%E8%BE%A8%E7%97%85" title="常见病自测/饮食起居辨病">饮食起居辨病</a></li>
<li><a href="/w/%E5%B8%B8%E8%A7%81%E7%97%85%E8%87%AA%E6%B5%8B/%E5%A6%87%E7%A7%91%E7%96%BE%E7%97%85" title="常见病自测/妇科疾病">妇科疾病</a></li>
<li><a href="/w/%E5%B8%B8%E8%A7%81%E7%97%85%E8%87%AA%E6%B5%8B/%E5%84%BF%E7%AB%A5%E7%96%BE%E7%97%85" title="常见病自测/儿童疾病">儿童疾病</a></li>
</ul>
</td>
</tr>
<tr>
<td>
<hr />
<p><a href="/w/%E5%B8%B8%E8%A7%81%E7%97%85%E8%87%AA%E6%B5%8B%E7%9B%AE%E5%BD%95" title="常见病自测目录">常见病自测目录</a></p>
</td>
</tr>
</table>
<p>这是我们专门给非医学专业的普通读者写的一本书。在日常生活中，去<a href="/w/%E5%8C%BB%E9%99%A2" title="医院">医院</a>不值得或不方便的情况经常存在。本书的目的就是在这个时候帮助医学知识不多的读者成为自己和家人的医生，从而少跑几趟医院，少看几回医生。为了达到这个目的，我们做了以下几个方面的努力。</p>
<p>第一是力求全面。本书涉及十种<a href="/w/%E5%B8%B8%E8%A7%81%E7%97%85" title="常见病" class="mw-redirect">常见病</a>，在生活中可能遇到的病证几乎都可以在书中找到。</p>
<p>第二是力求方便。本书是以<a href="/w/%E7%97%87%E7%8A%B6" title="症状">症状</a>为线索来安排全书内容的，就是说，只要您有一种不舒服的感觉，您就可以在书中迅速找到您可能得了什么病，非常方便。</p>
<p>第三是力求通俗。全书您几乎找不到自己读起来费劲的文字，为的是在您身体欠佳的时候不必再因读书而劳神，就像面对一位经验丰富的医生一样。</p>
<p>本书专门给读者讲了有关如何测病的问题，如果您在得知病情后需要用药，我们向您推荐另一本书：《给自己开药——常见病用药指南》。</p>
<p>编者</p>
<div style="clear:both;"></div>
<div class="book_index">
<ol>
<li><a href="/w/%E5%B8%B8%E8%A7%81%E7%97%85%E8%87%AA%E6%B5%8B/%E5%B8%B8%E8%A7%81%E7%97%87%E7%8A%B6%E8%BE%A8%E7%97%85" title="常见病自测/常见症状辨病">常见症状辨病</a>
<ol>
<li><a href="/w/%E5%B8%B8%E8%A7%81%E7%97%85%E8%87%AA%E6%B5%8B/%E5%B8%B8%E8%A7%81%E7%97%87%E7%8A%B6%E8%BE%A8%E7%97%85/%E5%8F%91%E7%83%AD" title="常见病自测/常见症状辨病/发热">常见症状辨病/发热</a></li>
<li><a href="/w/%E5%B8%B8%E8%A7%81%E7%97%85%E8%87%AA%E6%B5%8B/%E5%B8%B8%E8%A7%81%E7%97%87%E7%8A%B6%E8%BE%A8%E7%97%85/%E7%96%BC%E7%97%9B" title="常见病自测/常见症状辨病/疼痛">常见症状辨病/疼痛</a>
<ol>
<li><a href="/w/%E5%B8%B8%E8%A7%81%E7%97%85%E8%87%AA%E6%B5%8B/%E5%B8%B8%E8%A7%81%E7%97%87%E7%8A%B6%E8%BE%A8%E7%97%85/%E7%96%BC%E7%97%9B/%E5%A4%B4%E7%97%9B" title="常见病自测/常见症状辨病/疼痛/头痛">常见症状辨病/疼痛/头痛</a></li>
<li><a href="/w/%E5%B8%B8%E8%A7%81%E7%97%85%E8%87%AA%E6%B5%8B/%E5%B8%B8%E8%A7%81%E7%97%87%E7%8A%B6%E8%BE%A8%E7%97%85/%E7%96%BC%E7%97%9B/%E8%83%B8%E7%97%9B" title="常见病自测/常见症状辨病/疼痛/胸痛">常见症状辨病/疼痛/胸痛</a></li>
<li><a href="/w/%E5%B8%B8%E8%A7%81%E7%97%85%E8%87%AA%E6%B5%8B/%E5%B8%B8%E8%A7%81%E7%97%87%E7%8A%B6%E8%BE%A8%E7%97%85/%E7%96%BC%E7%97%9B/%E8%85%B9%E7%97%9B" title="常见病自测/常见症状辨病/疼痛/腹痛">常见症状辨病/疼痛/腹痛</a></li>
<li><a href="/w/%E5%B8%B8%E8%A7%81%E7%97%85%E8%87%AA%E6%B5%8B/%E5%B8%B8%E8%A7%81%E7%97%87%E7%8A%B6%E8%BE%A8%E7%97%85/%E7%96%BC%E7%97%9B/%E8%85%B0%E8%83%8C%E7%97%9B" title="常见病自测/常见症状辨病/疼痛/腰背痛">常见症状辨病/疼痛/腰背痛</a></li>
</ol>
</li>
<li><a href="/w/%E5%B8%B8%E8%A7%81%E7%97%85%E8%87%AA%E6%B5%8B/%E5%B8%B8%E8%A7%81%E7%97%87%E7%8A%B6%E8%BE%A8%E7%97%85/%E6%B0%B4%E8%82%BF" title="常见病自测/常见症状辨病/水肿">常见症状辨病/水肿</a></li>
<li><a href="/w/%E5%B8%B8%E8%A7%81%E7%97%85%E8%87%AA%E6%B5%8B/%E5%B8%B8%E8%A7%81%E7%97%87%E7%8A%B6%E8%BE%A8%E7%97%85/%E5%92%B3%E5%97%BD" title="常见病自测/常见症状辨病/咳嗽">常见症状辨病/咳嗽</a></li>
<li><a href="/w/%E5%B8%B8%E8%A7%81%E7%97%85%E8%87%AA%E6%B5%8B/%E5%B8%B8%E8%A7%81%E7%97%87%E7%8A%B6%E8%BE%A8%E7%97%85/%E5%87%BA%E8%A1%80" title="常见病自测/常见症状辨病/出血">常见症状辨病/出血</a>
<ol>
<li><a href="/w/%E5%B8%B8%E8%A7%81%E7%97%85%E8%87%AA%E6%B5%8B/%E5%B8%B8%E8%A7%81%E7%97%87%E7%8A%B6%E8%BE%A8%E7%97%85/%E7%9A%AE%E8%82%A4%E7%B2%98%E8%86%9C%E5%87%BA%E8%A1%80" title="常见病自测/常见症状辨病/皮肤粘膜出血">常见症状辨病/皮肤粘膜出血</a></li>
<li><a href="/w/%E5%B8%B8%E8%A7%81%E7%97%85%E8%87%AA%E6%B5%8B/%E5%B8%B8%E8%A7%81%E7%97%87%E7%8A%B6%E8%BE%A8%E7%97%85/%E5%92%AF%E8%A1%80" title="常见病自测/常见症状辨病/咯血">常见症状辨病/咯血</a></li>
<li><a href="/w/%E5%B8%B8%E8%A7%81%E7%97%85%E8%87%AA%E6%B5%8B/%E5%B8%B8%E8%A7%81%E7%97%87%E7%8A%B6%E8%BE%A8%E7%97%85/%E5%91%95%E8%A1%80" title="常见病自测/常见症状辨病/呕血">常见症状辨病/呕血</a></li>
<li><a href="/w/%E5%B8%B8%E8%A7%81%E7%97%85%E8%87%AA%E6%B5%8B/%E5%B8%B8%E8%A7%81%E7%97%87%E7%8A%B6%E8%BE%A8%E7%97%85/%E4%BE%BF%E8%A1%80" title="常见病自测/常见症状辨病/便血">常见症状辨病/便血</a></li>
<li><a href="/w/%E5%B8%B8%E8%A7%81%E7%97%85%E8%87%AA%E6%B5%8B/%E5%B8%B8%E8%A7%81%E7%97%87%E7%8A%B6%E8%BE%A8%E7%97%85/%E5%B0%BF%E8%A1%80" title="常见病自测/常见症状辨病/尿血">常见症状辨病/尿血</a></li>
<li><a href="/w/%E5%B8%B8%E8%A7%81%E7%97%85%E8%87%AA%E6%B5%8B/%E5%B8%B8%E8%A7%81%E7%97%87%E7%8A%B6%E8%BE%A8%E7%97%85/%E9%BC%BB%E5%87%BA%E8%A1%80" title="常见病自测/常见症状辨病/鼻出血">常见症状辨病/鼻出血</a></li>
</ol>
</li>
<li><a href="/w/%E5%B8%B8%E8%A7%81%E7%97%85%E8%87%AA%E6%B5%8B/%E5%B8%B8%E8%A7%81%E7%97%87%E7%8A%B6%E8%BE%A8%E7%97%85/%E6%81%B6%E5%BF%83%E4%B8%8E%E5%91%95%E5%90%90" title="常见病自测/常见症状辨病/恶心与呕吐">常见症状辨病/恶心与呕吐</a></li>
<li><a href="/w/%E5%B8%B8%E8%A7%81%E7%97%85%E8%87%AA%E6%B5%8B/%E5%B8%B8%E8%A7%81%E7%97%87%E7%8A%B6%E8%BE%A8%E7%97%85/%E6%84%9F%E8%A7%89%E5%99%A8%E5%AE%98%E5%8A%9F%E8%83%BD%E5%BC%82%E5%B8%B8" title="常见病自测/常见症状辨病/感觉器官功能异常">常见症状辨病/感觉器官功能异常</a></li>
<li><a href="/w/%E5%B8%B8%E8%A7%81%E7%97%85%E8%87%AA%E6%B5%8B/%E5%B8%B8%E8%A7%81%E7%97%87%E7%8A%B6%E8%BE%A8%E7%97%85/%E5%BF%83%E6%82%B8" title="常见病自测/常见症状辨病/心悸">常见症状辨病/心悸</a></li>
</ol>
</li>
<li><a href="/w/%E5%B8%B8%E8%A7%81%E7%97%85%E8%87%AA%E6%B5%8B/%E7%A5%9E%E8%89%B2%E5%BD%A2%E6%80%81%E8%BE%A8%E7%97%85" title="常见病自测/神色形态辨病">神色形态辨病</a>
<ol>
<li><a href="/w/%E5%B8%B8%E8%A7%81%E7%97%85%E8%87%AA%E6%B5%8B/%E7%A5%9E%E8%89%B2%E5%BD%A2%E6%80%81%E8%BE%A8%E7%97%85/%E6%9C%9B%E7%A5%9E" title="常见病自测/神色形态辨病/望神">神色形态辨病/望神</a></li>
<li><a href="/w/%E5%B8%B8%E8%A7%81%E7%97%85%E8%87%AA%E6%B5%8B/%E7%A5%9E%E8%89%B2%E5%BD%A2%E6%80%81%E8%BE%A8%E7%97%85/%E6%9C%9B%E9%9D%A2%E8%89%B2%E3%80%81%E9%9D%A2%E5%AE%B9" title="常见病自测/神色形态辨病/望面色、面容">神色形态辨病/望面色、面容</a></li>
<li><a href="/w/%E5%B8%B8%E8%A7%81%E7%97%85%E8%87%AA%E6%B5%8B/%E7%A5%9E%E8%89%B2%E5%BD%A2%E6%80%81%E8%BE%A8%E7%97%85/%E5%8F%91%E8%82%B2%E5%92%8C%E8%90%A5%E5%85%BB%E7%8A%B6%E6%80%81" title="常见病自测/神色形态辨病/发育和营养状态">神色形态辨病/发育和营养状态</a></li>
<li><a href="/w/%E5%B8%B8%E8%A7%81%E7%97%85%E8%87%AA%E6%B5%8B/%E7%A5%9E%E8%89%B2%E5%BD%A2%E6%80%81%E8%BE%A8%E7%97%85/%E4%BD%93%E4%BD%8D%E5%92%8C%E5%A7%BF%E6%80%81" title="常见病自测/神色形态辨病/体位和姿态">神色形态辨病/体位和姿态</a></li>
</ol>
</li>
<li><a href="/w/%E5%B8%B8%E8%A7%81%E7%97%85%E8%87%AA%E6%B5%8B/%E8%A7%82%E5%AF%9F%E6%9C%BA%E4%BD%93%E5%B1%80%E9%83%A8%E8%BE%A8%E7%97%85" title="常见病自测/观察机体局部辨病">观察机体局部辨病</a>
<ol>
<li><a href="/w/%E5%B8%B8%E8%A7%81%E7%97%85%E8%87%AA%E6%B5%8B/%E8%A7%82%E5%AF%9F%E6%9C%BA%E4%BD%93%E5%B1%80%E9%83%A8%E8%BE%A8%E7%97%85/%E7%9A%AE%E8%82%A4" title="常见病自测/观察机体局部辨病/皮肤">观察机体局部辨病/皮肤</a></li>
<li><a href="/w/%E5%B8%B8%E8%A7%81%E7%97%85%E8%87%AA%E6%B5%8B/%E8%A7%82%E5%AF%9F%E6%9C%BA%E4%BD%93%E5%B1%80%E9%83%A8%E8%BE%A8%E7%97%85/%E6%AF%9B%E5%8F%91" title="常见病自测/观察机体局部辨病/毛发">观察机体局部辨病/毛发</a></li>
<li><a href="/w/%E5%B8%B8%E8%A7%81%E7%97%85%E8%87%AA%E6%B5%8B/%E8%A7%82%E5%AF%9F%E6%9C%BA%E4%BD%93%E5%B1%80%E9%83%A8%E8%BE%A8%E7%97%85/%E5%A4%B4%E9%A2%85" title="常见病自测/观察机体局部辨病/头颅">观察机体局部辨病/头颅</a></li>
<li><a href="/w/%E5%B8%B8%E8%A7%81%E7%97%85%E8%87%AA%E6%B5%8B/%E8%A7%82%E5%AF%9F%E6%9C%BA%E4%BD%93%E5%B1%80%E9%83%A8%E8%BE%A8%E7%97%85/%E7%9C%89%E6%AF%9B" title="常见病自测/观察机体局部辨病/眉毛">观察机体局部辨病/眉毛</a></li>
<li><a href="/w/%E5%B8%B8%E8%A7%81%E7%97%85%E8%87%AA%E6%B5%8B/%E8%A7%82%E5%AF%9F%E6%9C%BA%E4%BD%93%E5%B1%80%E9%83%A8%E8%BE%A8%E7%97%85/%E7%9C%BC%E7%9D%9B" title="常见病自测/观察机体局部辨病/眼睛">观察机体局部辨病/眼睛</a></li>
<li><a href="/w/%E5%B8%B8%E8%A7%81%E7%97%85%E8%87%AA%E6%B5%8B/%E8%A7%82%E5%AF%9F%E6%9C%BA%E4%BD%93%E5%B1%80%E9%83%A8%E8%BE%A8%E7%97%85/%E9%BC%BB" title="常见病自测/观察机体局部辨病/鼻">观察机体局部辨病/鼻</a></li>
<li><a href="/w/%E5%B8%B8%E8%A7%81%E7%97%85%E8%87%AA%E6%B5%8B/%E8%A7%82%E5%AF%9F%E6%9C%BA%E4%BD%93%E5%B1%80%E9%83%A8%E8%BE%A8%E7%97%85/%E5%8F%A3%E8%85%94" title="常见病自测/观察机体局部辨病/口腔">观察机体局部辨病/口腔</a></li>
<li><a href="/w/%E5%B8%B8%E8%A7%81%E7%97%85%E8%87%AA%E6%B5%8B/%E8%A7%82%E5%AF%9F%E6%9C%BA%E4%BD%93%E5%B1%80%E9%83%A8%E8%BE%A8%E7%97%85/%E9%A2%88%E9%83%A8" title="常见病自测/观察机体局部辨病/颈部">观察机体局部辨病/颈部</a></li>
<li><a href="/w/%E5%B8%B8%E8%A7%81%E7%97%85%E8%87%AA%E6%B5%8B/%E8%A7%82%E5%AF%9F%E6%9C%BA%E4%BD%93%E5%B1%80%E9%83%A8%E8%BE%A8%E7%97%85/%E8%83%B8%E5%BB%93%E5%BD%A2%E6%80%81" title="常见病自测/观察机体局部辨病/胸廓形态">观察机体局部辨病/胸廓形态</a></li>
<li><a href="/w/%E5%B8%B8%E8%A7%81%E7%97%85%E8%87%AA%E6%B5%8B/%E8%A7%82%E5%AF%9F%E6%9C%BA%E4%BD%93%E5%B1%80%E9%83%A8%E8%BE%A8%E7%97%85/%E8%84%89%E6%90%8F" title="常见病自测/观察机体局部辨病/脉搏">观察机体局部辨病/脉搏</a></li>
<li><a href="/w/%E5%B8%B8%E8%A7%81%E7%97%85%E8%87%AA%E6%B5%8B/%E8%A7%82%E5%AF%9F%E6%9C%BA%E4%BD%93%E5%B1%80%E9%83%A8%E8%BE%A8%E7%97%85/%E8%85%B9%E9%83%A8" title="常见病自测/观察机体局部辨病/腹部">观察机体局部辨病/腹部</a></li>
<li><a href="/w/%E5%B8%B8%E8%A7%81%E7%97%85%E8%87%AA%E6%B5%8B/%E8%A7%82%E5%AF%9F%E6%9C%BA%E4%BD%93%E5%B1%80%E9%83%A8%E8%BE%A8%E7%97%85/%E8%84%8A%E6%9F%B1" title="常见病自测/观察机体局部辨病/脊柱">观察机体局部辨病/脊柱</a></li>
<li><a href="/w/%E5%B8%B8%E8%A7%81%E7%97%85%E8%87%AA%E6%B5%8B/%E8%A7%82%E5%AF%9F%E6%9C%BA%E4%BD%93%E5%B1%80%E9%83%A8%E8%BE%A8%E7%97%85/%E5%9B%9B%E8%82%A2%E5%BD%A2%E6%80%81" title="常见病自测/观察机体局部辨病/四肢形态">观察机体局部辨病/四肢形态</a></li>
</ol>
</li>
<li><a href="/w/%E5%B8%B8%E8%A7%81%E7%97%85%E8%87%AA%E6%B5%8B/%E8%A7%82%E5%AF%9F%E5%88%86%E6%B3%8C%E7%89%A9%E6%8E%92%E6%B3%84%E7%89%A9%E8%BE%A8%E7%97%85" title="常见病自测/观察分泌物排泄物辨病">观察分泌物排泄物辨病</a>
<ol>
<li><a href="/w/%E5%B8%B8%E8%A7%81%E7%97%85%E8%87%AA%E6%B5%8B/%E8%A7%82%E5%AF%9F%E5%88%86%E6%B3%8C%E7%89%A9%E6%8E%92%E6%B3%84%E7%89%A9%E8%BE%A8%E7%97%85/%E6%B1%97%E6%B6%B2%E5%BC%82%E5%B8%B8" title="常见病自测/观察分泌物排泄物辨病/汗液异常">观察分泌物排泄物辨病/汗液异常</a></li>
<li><a href="/w/%E5%B8%B8%E8%A7%81%E7%97%85%E8%87%AA%E6%B5%8B/%E8%A7%82%E5%AF%9F%E5%88%86%E6%B3%8C%E7%89%A9%E6%8E%92%E6%B3%84%E7%89%A9%E8%BE%A8%E7%97%85/%E5%B0%8F%E4%BE%BF" title="常见病自测/观察分泌物排泄物辨病/小便">观察分泌物排泄物辨病/小便</a></li>
<li><a href="/w/%E5%B8%B8%E8%A7%81%E7%97%85%E8%87%AA%E6%B5%8B/%E8%A7%82%E5%AF%9F%E5%88%86%E6%B3%8C%E7%89%A9%E6%8E%92%E6%B3%84%E7%89%A9%E8%BE%A8%E7%97%85/%E5%A4%A7%E4%BE%BF" title="常见病自测/观察分泌物排泄物辨病/大便">观察分泌物排泄物辨病/大便</a></li>
<li><a href="/w/%E5%B8%B8%E8%A7%81%E7%97%85%E8%87%AA%E6%B5%8B/%E8%A7%82%E5%AF%9F%E5%88%86%E6%B3%8C%E7%89%A9%E6%8E%92%E6%B3%84%E7%89%A9%E8%BE%A8%E7%97%85/%E9%BC%BB%E6%B6%95" title="常见病自测/观察分泌物排泄物辨病/鼻涕">观察分泌物排泄物辨病/鼻涕</a></li>
<li><a href="/w/%E5%B8%B8%E8%A7%81%E7%97%85%E8%87%AA%E6%B5%8B/%E8%A7%82%E5%AF%9F%E5%88%86%E6%B3%8C%E7%89%A9%E6%8E%92%E6%B3%84%E7%89%A9%E8%BE%A8%E7%97%85/%E7%97%B0%E6%B6%B2" title="常见病自测/观察分泌物排泄物辨病/痰液">观察分泌物排泄物辨病/痰液</a></li>
</ol>
</li>
<li><a href="/w/%E5%B8%B8%E8%A7%81%E7%97%85%E8%87%AA%E6%B5%8B/%E9%A5%AE%E9%A3%9F%E8%B5%B7%E5%B1%85%E8%BE%A8%E7%97%85" title="常见病自测/饮食起居辨病">饮食起居辨病</a>
<ol>
<li><a href="/w/%E5%B8%B8%E8%A7%81%E7%97%85%E8%87%AA%E6%B5%8B/%E9%A5%AE%E9%A3%9F%E8%B5%B7%E5%B1%85%E8%BE%A8%E7%97%85/%E9%A5%AE%E9%A3%9F" title="常见病自测/饮食起居辨病/饮食">饮食起居辨病/饮食</a></li>
<li><a href="/w/%E5%B8%B8%E8%A7%81%E7%97%85%E8%87%AA%E6%B5%8B/%E9%A5%AE%E9%A3%9F%E8%B5%B7%E5%B1%85%E8%BE%A8%E7%97%85/%E7%9D%A1%E7%9C%A0" title="常见病自测/饮食起居辨病/睡眠">饮食起居辨病/睡眠</a>
<ol>
<li><a href="/w/%E5%B8%B8%E8%A7%81%E7%97%85%E8%87%AA%E6%B5%8B/%E9%A5%AE%E9%A3%9F%E8%B5%B7%E5%B1%85%E8%BE%A8%E7%97%85/%E5%A4%B1%E7%9C%A0" title="常见病自测/饮食起居辨病/失眠">饮食起居辨病/失眠</a></li>
<li><a href="/w/%E5%B8%B8%E8%A7%81%E7%97%85%E8%87%AA%E6%B5%8B/%E9%A5%AE%E9%A3%9F%E8%B5%B7%E5%B1%85%E8%BE%A8%E7%97%85/%E5%97%9C%E7%9D%A1" title="常见病自测/饮食起居辨病/嗜睡">饮食起居辨病/嗜睡</a></li>
</ol>
</li>
<li><a href="/w/%E5%B8%B8%E8%A7%81%E7%97%85%E8%87%AA%E6%B5%8B/%E9%A5%AE%E9%A3%9F%E8%B5%B7%E5%B1%85%E8%BE%A8%E7%97%85/%E8%AF%B4%E8%AF%9D%E5%BC%82%E5%B8%B8" title="常见病自测/饮食起居辨病/说话异常">饮食起居辨病/说话异常</a></li>
<li><a href="/w/%E5%B8%B8%E8%A7%81%E7%97%85%E8%87%AA%E6%B5%8B/%E9%A5%AE%E9%A3%9F%E8%B5%B7%E5%B1%85%E8%BE%A8%E7%97%85/%E8%BF%90%E5%8A%A8%E5%BC%82%E5%B8%B8" title="常见病自测/饮食起居辨病/运动异常">饮食起居辨病/运动异常</a></li>
</ol>
</li>
<li><a href="/w/%E5%B8%B8%E8%A7%81%E7%97%85%E8%87%AA%E6%B5%8B/%E5%A6%87%E7%A7%91%E7%96%BE%E7%97%85" title="常见病自测/妇科疾病">妇科疾病</a>
<ol>
<li><a href="/w/%E5%B8%B8%E8%A7%81%E7%97%85%E8%87%AA%E6%B5%8B/%E5%A6%87%E7%A7%91%E7%96%BE%E7%97%85/%E6%9C%88%E7%BB%8F%E5%92%8C%E7%99%BD%E5%B8%A6" title="常见病自测/妇科疾病/月经和白带">妇科疾病/月经和白带</a></li>
<li><a href="/w/%E5%B8%B8%E8%A7%81%E7%97%85%E8%87%AA%E6%B5%8B/%E5%A6%87%E7%A7%91%E7%96%BE%E7%97%85/%E4%B9%B3%E6%88%BF" title="常见病自测/妇科疾病/乳房">妇科疾病/乳房</a></li>
<li><a href="/w/%E5%B8%B8%E8%A7%81%E7%97%85%E8%87%AA%E6%B5%8B/%E5%A6%87%E7%A7%91%E7%96%BE%E7%97%85/%E9%9D%9E%E7%BB%8F%E6%9C%9F%E9%98%B4%E9%81%93%E5%87%BA%E8%A1%80%E5%92%8C%E8%85%B9%E7%97%9B" title="常见病自测/妇科疾病/非经期阴道出血和腹痛">妇科疾病/非经期阴道出血和腹痛</a></li>
</ol>
</li>
<li><a href="/w/%E5%B8%B8%E8%A7%81%E7%97%85%E8%87%AA%E6%B5%8B/%E5%84%BF%E7%AB%A5%E7%96%BE%E7%97%85" title="常见病自测/儿童疾病">儿童疾病</a>
<ol>
<li><a href="/w/%E5%B8%B8%E8%A7%81%E7%97%85%E8%87%AA%E6%B5%8B/%E5%84%BF%E7%AB%A5%E7%96%BE%E7%97%85/%E5%85%A8%E8%BA%AB%E7%8A%B6%E6%80%81%E5%BC%82%E5%B8%B8" title="常见病自测/儿童疾病/全身状态异常">儿童疾病/全身状态异常</a></li>
<li><a href="/w/%E5%B8%B8%E8%A7%81%E7%97%85%E8%87%AA%E6%B5%8B/%E5%84%BF%E7%AB%A5%E7%96%BE%E7%97%85/%E6%9C%9B%E6%9C%BA%E4%BD%93%E5%B1%80%E9%83%A8" title="常见病自测/儿童疾病/望机体局部">儿童疾病/望机体局部</a></li>
<li><a href="/w/%E5%B8%B8%E8%A7%81%E7%97%85%E8%87%AA%E6%B5%8B/%E5%84%BF%E7%AB%A5%E7%96%BE%E7%97%85/%E5%B8%B8%E8%A7%81%E7%97%87%E7%8A%B6" title="常见病自测/儿童疾病/常见症状">儿童疾病/常见症状</a></li>
</ol>
</li>
</ol>
</div>
<h2><span class="mw-headline" id=".E5.8F.82.E8.80.83">参考</span></h2>
<ul>
<li><a href="/w/%E7%97%87%E7%8A%B6" title="症状">症状查询</a></li>
<li><a href="/w/%E6%80%8E%E6%A0%B7%E7%9C%8B%E5%8C%96%E9%AA%8C%E5%8D%95" title="怎样看化验单">怎样看化验单</a></li>
<li><a href="/w/%E7%96%BE%E7%97%85" title="疾病">疾病查询</a></li>
</ul>
<p><br /></p>
<table width="100%" class="hierarchy-nav">
<tr>
<td align="center" width="100%" nowrap="nowrap"><a href="/w/%E5%B8%B8%E8%A7%81%E7%97%85%E8%87%AA%E6%B5%8B/%E5%B8%B8%E8%A7%81%E7%97%87%E7%8A%B6%E8%BE%A8%E7%97%85" title="常见病自测/常见症状辨病">常见症状辨病</a> <a href="/w/%E5%B8%B8%E8%A7%81%E7%97%85%E8%87%AA%E6%B5%8B/%E5%B8%B8%E8%A7%81%E7%97%87%E7%8A%B6%E8%BE%A8%E7%97%85" title="32"><img alt="32" src="http://p.ayxbk.com/images/5/53/Gonext.gif" width="32" height="32" /></a></td>
</tr>
</table>

<!-- 
NewPP limit report
Preprocessor node count: 26/1000000
Post-expand include size: 7182/2097152 bytes
Template argument size: 0/2097152 bytes
Expensive parser function count: 0/100
-->

<!-- Saved in parser cache with key ahospital:pcache:idhash:82286-0!1!0!!zh-hans!2!edit=0 and timestamp 20181018200336 -->
<div id="fromlink">出自A+医学百科 “常见病自测”条目 <a href="http://www.a-hospital.com/w/%E5%B8%B8%E8%A7%81%E7%97%85%E8%87%AA%E6%B5%8B" class="external free" target="_blank">http://www.a-hospital.com/w/%E5%B8%B8%E8%A7%81%E7%97%85%E8%87%AA%E6%B5%8B</a> 转载请保留此链接</div><div class="bdsharebuttonbox"><a href="#" class="bds_qzone" data-cmd="qzone" title="分享到QQ空间"></a><a href="#" class="bds_weixin" data-cmd="weixin" title="分享到微信"></a><a href="#" class="bds_tqq" data-cmd="tqq" title="分享到腾讯微博"></a><a href="#" class="bds_tsina" data-cmd="tsina" title="分享到新浪微博"></a><a href="#" class="bds_fbook" data-cmd="fbook" title="分享到Facebook"></a><a href="#" class="bds_copy" data-cmd="copy" title="分享到复制网址"></a><a href="#" class="bds_more" data-cmd="more"></a><a href="#" class="bds_count" data-cmd="count"></a></div>
<table class="msg-table">

<tr style="background-color:rgb(206, 223, 242);">
<td><b>关于“<strong class="selflink">常见病自测</strong>”的留言：</b>
</td><td align="right"><img alt="Feed-icon.png" src="http://p.ayxbk.com/images/f/f4/Feed-icon.png" width="12" height="12" /> <a href="http://www.a-hospital.com/index.php?title=%E8%AE%A8%E8%AE%BA:%E5%B8%B8%E8%A7%81%E7%97%85%E8%87%AA%E6%B5%8B&amp;feed=rss&amp;action=history" class="external text" target="_blank">订阅讨论RSS</a>
</td></tr>
<tr>
<td colspan="2" style="background-color:#ffffff;">
<h2> <span class="mw-headline" id=".E7.BB.99.E5.B8.B8.E8.A7.81.E7.97.85.E8.87.AA.E6.B5.8B.E6.9D.A1.E7.9B.AE.E7.9A.84.E7.95.99.E8.A8.80"> 给常见病自测条目的留言 </span></h2>
<p>--<a href="/w/%E7%89%B9%E6%AE%8A:%E7%94%A8%E6%88%B7%E8%B4%A1%E7%8C%AE/60.4.46.116" title="特殊:用户贡献/60.4.46.116">60.4.46.116</a> 2013年4月15日 (一) 15:51 (CST)
</p><p>留言：很好应多著此类书谢谢
内容丰富，实用，好用。感谢提供！
</p>
<h2> <span class="mw-headline" id=".E7.BB.99.E5.B8.B8.E8.A7.81.E7.97.85.E8.87.AA.E6.B5.8B.E6.9D.A1.E7.9B.AE.E7.9A.84.E7.95.99.E8.A8.80_2"> 给常见病自测条目的留言 </span></h2>
<p>--<a href="/w/%E7%89%B9%E6%AE%8A:%E7%94%A8%E6%88%B7%E8%B4%A1%E7%8C%AE/58.20.241.74" title="特殊:用户贡献/58.20.241.74">58.20.241.74</a> 2016年5月11日 (三) 16:11 (CST)
</p><p>留言：
内容丰富，感谢！
</p>
</td></tr>
<tr>
<td colspan="2"><a href="http://www.a-hospital.com/index.php?title=%E8%AE%A8%E8%AE%BA:%E5%B8%B8%E8%A7%81%E7%97%85%E8%87%AA%E6%B5%8B&amp;action=edit&amp;section=new&amp;preload=%E6%A8%A1%E6%9D%BF%3A%E7%AD%BE%E5%90%8D&amp;editintro=%E6%A8%A1%E6%9D%BF%3A%E7%AD%BE%E5%90%8D%E8%AF%B4%E6%98%8E&amp;preloadtitle=%E7%BB%99%E5%B8%B8%E8%A7%81%E7%97%85%E8%87%AA%E6%B5%8B%E6%9D%A1%E7%9B%AE%E7%9A%84%E7%95%99%E8%A8%80" class="external text" target="_blank">添加留言</a>
</td></tr></table>
<h2> <span class="mw-headline" id=".E6.9B.B4.E5.A4.9A.E5.8C.BB.E5.AD.A6.E7.99.BE.E7.A7.91.E6.9D.A1.E7.9B.AE">更多医学百科条目</span></h2>
				<!-- /bodytext -->
								<!-- catlinks -->
				<div id='catlinks' class='catlinks'><div id="mw-normal-catlinks"><a href="/w/%E7%89%B9%E6%AE%8A:%E9%A1%B5%E9%9D%A2%E5%88%86%E7%B1%BB" title="特殊:页面分类">1个分类</a>: <span dir='ltr'><a href="/w/%E5%88%86%E7%B1%BB:%E5%8C%BB%E5%AD%A6%E4%B9%A6%E7%B1%8D" title="分类:医学书籍">医学书籍</a></span></div></div>				<!-- /catlinks -->
												<div class="visualClear"></div>
			</div>
			<!-- /bodyContent -->
		</div>
		<!-- /content -->
		<!-- header -->
		<div id="mw-head" class="noprint">
			
<!-- 0 -->
<div id="p-personal" class="">
	<h5>个人工具</h5>
	<ul>
					<li  id="pt-login"><a href="/index.php?title=%E7%89%B9%E6%AE%8A:%E7%94%A8%E6%88%B7%E7%99%BB%E5%BD%95&amp;returnto=%E5%B8%B8%E8%A7%81%E7%97%85%E8%87%AA%E6%B5%8B" title="我们鼓励您登录，但这并不是必须的 [o]" accesskey="o" rel="nofollow">登录／创建账户</a></li>
			</ul>
</div>

<!-- /0 -->
			<div id="left-navigation">
				
<!-- 0 -->
<div id="p-namespaces" class="vectorTabs">
	<h5>名字空间</h5>
	<ul>
					<li  id="ca-nstab-main" class="selected"><a href="/w/%E5%B8%B8%E8%A7%81%E7%97%85%E8%87%AA%E6%B5%8B" rel="nofollow"  title="查看页面内容 [c]" accesskey="c"><span>页面</span></a></li>
					<li  id="ca-talk"><a href="/w/%E8%AE%A8%E8%AE%BA:%E5%B8%B8%E8%A7%81%E7%97%85%E8%87%AA%E6%B5%8B" rel="nofollow"  title="关于页面正文的讨论 [t]" accesskey="t"><span>讨论</span></a></li>
			</ul>
</div>

<!-- /0 -->

<!-- 1 -->

<!-- /1 -->
			</div>
			<div id="right-navigation">
				
<!-- 0 -->
<div id="p-views" class="vectorTabs">
	<h5>查看</h5>
	<ul>
					<li id="ca-view" class="selected"><a href="/w/%E5%B8%B8%E8%A7%81%E7%97%85%E8%87%AA%E6%B5%8B" rel="nofollow"><span>阅读</span></a></li>
					<li id="ca-trans"><a href="http://cht.a-hospital.com/w/%E5%B8%B8%E8%A7%81%E7%97%85%E8%87%AA%E6%B5%8B" rel="alternate" hreflang="zh-Hant"><span>繁体/正体</span></a></li>
					<li id="ca-viewsource"><a href="/index.php?title=%E5%B8%B8%E8%A7%81%E7%97%85%E8%87%AA%E6%B5%8B&amp;action=edit" rel="nofollow" title="修正、补充或整理本条目。 [e]" accesskey="e"><span>编辑修改</span></a></li>
					<li id="ca-history" class="collapsible "><a href="/index.php?title=%E5%B8%B8%E8%A7%81%E7%97%85%E8%87%AA%E6%B5%8B&amp;action=history" rel="nofollow" title="此页面的早前修订版本 [h]" accesskey="h"><span>修订历史</span></a></li>
			</ul>
</div>

<!-- /0 -->

<!-- 1 -->
<div id="p-cactions" class="vectorMenu emptyPortlet">
	<h5><span>动作</span><a href="#"></a></h5>
	<div class="menu">
		<ul>
					</ul>
	</div>
</div>

<!-- /1 -->

<!-- 2 -->
<div id="p-search">
	<h5><label for="searchInput">搜索</label></h5>
	<form action="/index.php" id="searchform">
		<input type='hidden' name="title" value="特殊:搜索"/>
		<div id="simpleSearch">
							<input id="searchInput"  onfocus="if (this.value == '搜索') {this.value = '';}" onblur="if (this.value == '') {this.value = '搜索';}" name="search" type="text"  title="搜索该网站 [f]" accesskey="f"  value="搜索"  />
						<button id="searchButton" type='submit' name='button'  title="搜索该文字的页面">&nbsp;</button>
		</div>
	</form>
</div>

<!-- /2 -->
			</div>
		</div>
		<!-- /header -->
		<!-- panel -->
			<div id="mw-panel" class="noprint">
				<!-- logo -->
					<div id="p-logo"><a style="background-image: url(http://s.ayxbk.com/common/images/logo.png);" href="/w/%E9%A6%96%E9%A1%B5"  title="访问首页"></a></div>
				<!-- /logo -->
				  
<div class="portal" id='p-navigation'>
	<h5>导航</h5>
	<div class="body">
				<ul>
					<li><a href="/w/%E9%A6%96%E9%A1%B5" title="访问首页 [z]" accesskey="z">首页</a></li>
					<li><a href="/w/%E5%A4%A7%E5%8C%BB%E7%B2%BE%E8%AF%9A">大医精诚</a></li>
					<li><a href="/w/%E4%BA%BA%E4%BD%93%E7%A9%B4%E4%BD%8D%E5%9B%BE">人体穴位图</a></li>
					<li><a href="/w/%E4%B8%AD%E8%8D%AF%E5%9B%BE%E5%85%B8">中药图典</a></li>
					<li><a href="/w/%E5%85%A8%E5%9B%BD%E5%8C%BB%E9%99%A2%E5%88%97%E8%A1%A8">全国医院列表</a></li>
					<li><a href="/w/%E5%8C%BB%E5%AD%A6%E7%94%B5%E5%AD%90%E4%B9%A6">医学电子书</a></li>
					<li><a href="/w/%E8%8D%AF%E5%93%81">药品百科</a></li>
					<li><a href="/w/%E4%B8%AD%E5%8C%BB">中医百科</a></li>
					<li><a href="/w/%E7%96%BE%E7%97%85%E8%AF%8A%E6%96%AD">疾病诊断</a></li>
					<li><a href="/w/%E6%80%A5%E6%95%91%E5%B8%B8%E8%AF%86">急救常识</a></li>
					<li><a href="/w/%E7%96%BE%E7%97%85">疾病查询</a></li>
					<li><a href="/w/%E4%B8%AD%E8%8D%AF">中药百科</a></li>
					<li><a href="/w/%E4%B8%AD%E8%8D%AF%E6%96%B9%E5%89%82">中医方剂大全</a></li>
					<li><a href="/w/%E6%80%8E%E6%A0%B7%E7%9C%8B%E5%8C%96%E9%AA%8C%E5%8D%95">怎样看化验单</a></li>
					<li><a href="/w/%E5%85%A8%E5%9B%BD%E5%88%B6%E8%8D%AF%E4%BC%81%E4%B8%9A%E5%88%97%E8%A1%A8">全国制药企业</a></li>
					<li><a href="/w/%E5%85%A8%E5%9B%BD%E5%8C%BB%E7%A7%91%E9%99%A2%E6%A0%A1%E5%88%97%E8%A1%A8">医科院校大全</a></li>
					<li><a href="/w/%E5%8C%BB%E4%BA%8B%E6%BC%AB%E8%B0%88">医事漫谈</a></li>
					<li><a href="/w/%E5%8C%BB%E5%AD%A6%E4%B8%8B%E8%BD%BD">医学下载</a></li>
					<li><a href="/w/%E5%8C%BB%E5%AD%A6%E8%A7%86%E9%A2%91">医学视频</a></li>
				</ul>
			</div>
</div>
  
<div class="portal" id='p-.E6.8E.A8.E8.8D.90.E5.B7.A5.E5.85.B7'>
	<h5>推荐工具</h5>
	<div class="body">
				<ul>
					<li><a href="http://www.adaohang.com/health.html">医学网站大全</a></li>
					<li><a href="http://www.mcd8.com/">医学词典</a></li>
					<li><a href="http://blog.a-hospital.com/">医学资讯博客</a></li>
				</ul>
			</div>
</div>
  
<div class="portal" id='p-.E5.8A.9F.E8.83.BD.E8.8F.9C.E5.8D.95'>
	<h5>功能菜单</h5>
	<div class="body">
				<ul>
					<li><a href="/w/A%2B%E5%8C%BB%E5%AD%A6%E7%99%BE%E7%A7%91:%E6%B7%BB%E5%8A%A0%E6%9D%A1%E7%9B%AE" rel="nofollow">添加页面</a></li>
					<li><a href="/w/A%2B%E5%8C%BB%E5%AD%A6%E7%99%BE%E7%A7%91:%E6%8B%9B%E5%8B%9F%E7%99%BE%E7%A7%91%E5%BF%97%E6%84%BF%E8%80%85" rel="nofollow">志愿者招募中</a></li>
					<li><a href="/w/%E7%89%B9%E6%AE%8A:ContributionScores" rel="nofollow">积分排名</a></li>
					<li><a href="/w/A%2B%E5%8C%BB%E5%AD%A6%E7%99%BE%E7%A7%91:%E5%85%B3%E4%BA%8E%E5%B9%BF%E5%91%8A" rel="nofollow">关于广告</a></li>
					<li><a href="/w/A%2B%E5%8C%BB%E5%AD%A6%E7%99%BE%E7%A7%91:%E7%BD%91%E7%AB%99%E4%BA%8B%E5%8A%A1">网站事务</a></li>
					<li><a href="/w/%E7%89%B9%E6%AE%8A:%E6%9C%80%E8%BF%91%E6%9B%B4%E6%94%B9" title="列出该网站的最近修改 [r]" accesskey="r">最近更改</a></li>
				</ul>
			</div>
</div>
<div class="portal" id="p-tb">
	<h5>工具箱</h5>
	<div class="body">
		<ul>
					<li id="t-whatlinkshere"><a href="/w/%E7%89%B9%E6%AE%8A:%E9%93%BE%E5%85%A5%E9%A1%B5%E9%9D%A2/%E5%B8%B8%E8%A7%81%E7%97%85%E8%87%AA%E6%B5%8B" title="列出所有与此页相链的页面 [j]" accesskey="j">链入页面</a></li>
						<li id="t-recentchangeslinked"><a href="/w/%E7%89%B9%E6%AE%8A:%E9%93%BE%E5%87%BA%E6%9B%B4%E6%94%B9/%E5%B8%B8%E8%A7%81%E7%97%85%E8%87%AA%E6%B5%8B" title="从此页链出的所有页面的更改 [k]" accesskey="k">链出更改</a></li>
																																												<li id="t-specialpages"><a href="/w/%E7%89%B9%E6%AE%8A:%E7%89%B9%E6%AE%8A%E9%A1%B5%E9%9D%A2" title="所有特殊页面列表 [q]" accesskey="q">所有特殊页面</a></li>
									<li id="t-print"><a href="/index.php?title=%E5%B8%B8%E8%A7%81%E7%97%85%E8%87%AA%E6%B5%8B&amp;printable=yes" rel="nofollow" title="这个页面的可打印版本 [p]" accesskey="p">可打印版</a></li>
						</ul>
	</div>
</div>
			</div>
		<!-- /panel -->
		<!-- footer -->
		<div id="footer">
											<ul id="footer-info">
																	<li id="footer-info-credits">此页由A+医学百科用户<a rel="nofollow" href="/w/%E7%94%A8%E6%88%B7:%E5%8C%BB%E8%80%85" title="用户:医者">医者</a>于2016年12月4日 (星期日) 11:21最后更改。 在<a rel="nofollow" href="/index.php?title=%E7%94%A8%E6%88%B7:%E5%93%88%E5%96%BD%E5%A4%A7%E9%87%8C&amp;action=edit&amp;redlink=1" class="new" title="用户:哈喽大里（尚未撰写）" rel="nofollow">呵呵</a>和A+医学百科用户<a rel="nofollow" href="/w/%E7%94%A8%E6%88%B7:Ewirqweirxuqwmruqw" title="用户:Ewirqweirxuqwmruqw">Ewirqweirxuqwmruqw</a>和<a rel="nofollow" href="/w/%E7%94%A8%E6%88%B7:%E8%A1%8C%E5%8C%BB" title="用户:行医">行医</a>的工作基础上。</li>
																							<li id="footer-info-copyright"><br />本站内容由网友添加和整理，仅供学习和参考。站内信息不一定准确、全面或最新。<br />
网站内容不应成为诊断或治疗疾病的最终依据。A+医学百科提醒网友，如有身体不适，请及时就医。<br />
本站的全部文本内容在<a rel="nofollow" href="/w/A%2B%E5%8C%BB%E5%AD%A6%E7%99%BE%E7%A7%91:%E7%89%88%E6%9D%83" title="A+医学百科:版权">知识共享 署名-相同方式共享 3.0协议</a>之条款下提供。<br /></li>
															</ul>
															<ul id="footer-places">
																	<li id="footer-places-privacy"><a rel="nofollow" href="/w/A%2B%E5%8C%BB%E5%AD%A6%E7%99%BE%E7%A7%91:%E9%9A%90%E7%A7%81%E6%94%BF%E7%AD%96" title="A+医学百科:隐私政策">隐私政策</a></li>
																							<li id="footer-places-about"><a rel="nofollow" href="/w/A%2B%E5%8C%BB%E5%AD%A6%E7%99%BE%E7%A7%91:%E5%85%B3%E4%BA%8E" title="A+医学百科:关于">关于A+医学百科</a></li>
																							<li id="footer-places-disclaimer"><a rel="nofollow" href="/w/A%2B%E5%8C%BB%E5%AD%A6%E7%99%BE%E7%A7%91:%E5%85%8D%E8%B4%A3%E5%A3%B0%E6%98%8E" title="A+医学百科:免责声明">免责声明</a></li>
															</ul>
										<div style="clear:both"></div>
		</div>
		<!-- /footer -->
						<script>window._bd_share_config={"common":{"bdSign":"off","bdSnsKey":{},"bdText":"","bdMini":"2","bdMiniList":false,"bdPic":"","bdStyle":"0","bdSize":"32"},"share":{},"image":{"viewList":["qzone","weixin","tqq","tsina","fbook"],"viewText":"分享到：","viewSize":"16"},"selectShare":{"bdContainerClass":null,"bdSelectMiniList":["qzone","weixin","tqq","tsina","fbook"]}};with(document)0[(getElementsByTagName('head')[0]||body).appendChild(createElement('script')).src='http://bdimg.share.baidu.com/static/api/js/share.js?v=89860593.js?cdnversion='+~(-new Date()/36e5)];</script>
				
<script>
var skin="vector",
stylepath="http://s.ayxbk.com",
wgUrlProtocols="http\\:\\/\\/|https\\:\\/\\/|ftp\\:\\/\\/|irc\\:\\/\\/|mailto\\:",
wgArticlePath="/w/$1",
wgScriptPath="",
wgScriptExtension=".php",
wgScript="/index.php",
wgVariantArticlePath=false,
wgActionPaths={},
wgServer="http://www.a-hospital.com",
wgCanonicalNamespace="",
wgCanonicalSpecialPageName=false,
wgNamespaceNumber=0,
wgPageName="常见病自测",
wgTitle="常见病自测",
wgAction="view",
wgArticleId=82286,
wgIsArticle=true,
wgUserName=null,
wgUserGroups=null,
wgUserLanguage="zh-hans",
wgContentLanguage="zh-hans",
wgBreakFrames=true,
wgCurRevisionId=539425,
wgVersion="1.16.0",
wgEnableAPI=true,
wgEnableWriteAPI=true,
wgSeparatorTransformTable=["", ""],
wgDigitTransformTable=["", ""],
wgMainPageTitle="首页",
wgFormattedNamespaces={"-2": "媒体", "-1": "特殊", "0": "", "1": "讨论", "2": "用户", "3": "用户讨论", "4": "A+医学百科", "5": "A+医学百科讨论", "6": "文件", "7": "文件讨论", "8": "MediaWiki", "9": "MediaWiki讨论", "10": "模板", "11": "模板讨论", "12": "帮助", "13": "帮助讨论", "14": "分类", "15": "分类讨论", "420": "Layer", "421": "Layer talk"},
wgSiteName="A+医学百科",
wgCategories=["医学书籍"],
wgMWSuggestTemplate="http://www.a-hospital.com/api.php?action=opensearch\x26search={searchTerms}\x26namespace={namespaces}\x26suggest",
wgDBname="ahospital",
wgSearchNamespaces=[0],
wgMWSuggestMessages=["有建议", "无建议"],
wgRestrictionEdit=[],
wgRestrictionMove=[];
</script><script src="http://s.ayxbk.com/common/main-mini.js?278"></script>
<!--[if lt IE 7]><style type="text/css">body{behavior:url("http://s.ayxbk.com/vector/csshover.htc")}</style><![endif]-->
<script type="text/javascript">
window.google_analytics_uacct = "UA-1856547-6";
</script>
<script>if (window.runOnloadHook) runOnloadHook();</script>
<script type="text/javascript">
var gaJsHost = (("https:" == document.location.protocol) ? "https://ssl." : "http://www.");
document.write(unescape("%3Cscript src='" + gaJsHost + "google-analytics.com/ga.js' type='text/javascript'%3E%3C/script%3E"));
</script>
<script type="text/javascript">
var pageTracker = _gat._getTracker("UA-1856547-6");
pageTracker._initData();
pageTracker._trackPageview();
</script>		<script type="text/javascript"> if ( window.isMSIE55 ) fixalpha(); </script>
		<!-- Served in 0.221 secs. -->			</body>
<!-- Cached/compressed 20181018200336 -->
</html>
"""
    response = HtmlResponse(url='http://www.a-hospital.com/w/DC',
                            body=body, encoding='utf8')
    ppl = AhospitalPipeline()
    spider = HospitalSpider() 
    ppl.open_spider(spider)
    resp_iter = spider.parse(response)
    page = next(resp_iter)
    assert page is not None
    assert not isinstance(page, AhospitalItem)

    next_url = next(resp_iter)
    assert isinstance(next_url, Request)

def test_spider_company_info_page():
    body = """

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html lang="zh-hans" dir="ltr">
<head>
<title>重庆药友制药有限责任公司_联系方式_电话_网站_邮箱_生产的药品列表_A+医学百科</title>
<meta name="keywords" content="重庆药友制药有限责任公司,重庆药友制药有限责任公司联系方式,重庆药友制药有限责任公司联系电话,重庆药友制药有限责任公司电子邮箱,重庆药友制药有限责任公司药品列表,药品生产企业,药品公司,公司信息" />
<meta name="description" content="重庆药友制药有限责任公司相关信息介绍，包含重庆药友制药有限责任公司的联系方式，地址，生产药品列表等信息。重庆药友制药有限责任公司位于重庆市渝北区人和镇（北部新区高新园区）星光大道 100号，联系..." />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<meta name="applicable-device" content="pc,mobile" />
<meta http-equiv="Cache-Control" content="no-transform" />
<meta http-equiv="Cache-Control" content="no-siteapp" />
<meta name="generator" content="MediaWiki 1.16.0" />
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<link rel="apple-touch-icon" href="http://s.ayxbk.com/common/images/apple-touch-icon.png" />
<link rel="shortcut icon" href="http://s.ayxbk.com/favicon.ico" />
<link rel="search" type="application/opensearchdescription+xml" href="/opensearch_desc.php" title="A+医学百科 (zh-hans)" />
<link rel="copyright" href="/w/A%2B%E5%8C%BB%E5%AD%A6%E7%99%BE%E7%A7%91:%E7%89%88%E6%9D%83" />
<link rel="stylesheet" href="http://s.ayxbk.com/vector/main-mini.css?278" media="screen" />

</head>
<body class="mediawiki ltr ns-0 ns-subject page-重庆药友制药有限责任公司 skin-vector">
		<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
		<script>
		     (adsbygoogle = window.adsbygoogle || []).push({
		          google_ad_client: "ca-pub-4174070858627065",
		          enable_page_level_ads: true
		     });
		</script>
		<div id="mw-page-base" class="noprint"></div>
		<div id="mw-head-base" class="noprint"></div>
		<!-- content -->
		<div id="content" >
			<a id="top"></a>
			<div id="mw-js-message" style="display:none;"></div>
						<!-- firstHeading -->
			<h1 id="firstHeading" class="firstHeading">重庆药友制药有限责任公司</h1>
			<!-- /firstHeading -->
			<!-- bodyContent -->
			<div id="bodyContent">
				<!-- subtitle -->
				<div id="contentSub"></div>
				<!-- /subtitle -->
																<!-- jumpto -->
				<div id="jump-to-nav">
					跳转到： <a href="#mw-head">导航</a>,
					<a href="#p-search">搜索</a>
				</div>
				<!-- /jumpto -->
								<!-- bodytext -->
				<table class="nav">
<tr>
<td><a href="/w/%E9%A6%96%E9%A1%B5" title="首页">A+医学百科</a> &gt;&gt; <a href="/w/%E5%85%A8%E5%9B%BD%E5%88%B6%E8%8D%AF%E4%BC%81%E4%B8%9A%E5%88%97%E8%A1%A8" title="全国制药企业列表">全国制药企业列表</a> &gt;&gt; <a href="/w/%E9%87%8D%E5%BA%86%E5%B8%82%E5%88%B6%E8%8D%AF%E4%BC%81%E4%B8%9A%E5%88%97%E8%A1%A8" title="重庆市制药企业列表">重庆市制药企业列表</a> &gt;&gt; 重庆药友制药有限责任公司</td>
</tr>
</table>
<p></p>
<table class="infobox hproduct" cellspacing="5" style="width:22em; width:23em; font-size:88%;float:none;">
<tr>
<th colspan="2" class="" style="text-align:center; font-size:125%; font-weight:bold; font-size: 110%;"><span class="fn">重庆药友制药有限责任公司</span></th>
</tr>
<tr class="">
<th scope="row" style="text-align:left; text-align:left; white-space: nowrap">公司地址</th>
<td class="" style="">重庆市渝北区人和镇（北部新区高新园区）星光大道 100号</td>
</tr>
<tr class="">
<th scope="row" style="text-align:left; text-align:left; white-space: nowrap">联系电话</th>
<td class="" style="">023-67527818</td>
</tr>
<tr class="">
<th scope="row" style="text-align:left; text-align:left; white-space: nowrap">传真号码</th>
<td class="" style="">023-67527018</td>
</tr>
<tr class="">
<th scope="row" style="text-align:left; text-align:left; white-space: nowrap">电子邮箱</th>
<td class="" style="">&#160;</td>
</tr>
<tr class="">
<th scope="row" style="text-align:left; text-align:left; white-space: nowrap">邮政编码</th>
<td class="" style="">401121</td>
</tr>
<tr class="">
<th scope="row" style="text-align:left; text-align:left; white-space: nowrap">公司网址</th>
<td class="" style=""><a href="http://www.yaoyou.cn" class="external free" rel="nofollow" target="_blank">http://www.yaoyou.cn</a></td>
</tr>
</table>
<p>重庆药友制药有限责任公司位于重庆市。查询更多位于重庆市的制药企业请参看<a href="/w/%E9%87%8D%E5%BA%86%E5%B8%82%E5%88%B6%E8%8D%AF%E4%BC%81%E4%B8%9A%E5%88%97%E8%A1%A8" title="重庆市制药企业列表">重庆市制药企业列表</a>。</p>
<div style="clear:both;"></div>
<p><br /></p>
<table id="toc" class="toc">
<tr>
<td>
<div id="toctitle">
<h2>目录</h2>
</div>
<ul>
<li class="toclevel-1 tocsection-1"><a href="#.E9.87.8D.E5.BA.86.E8.8D.AF.E5.8F.8B.E5.88.B6.E8.8D.AF.E6.9C.89.E9.99.90.E8.B4.A3.E4.BB.BB.E5.85.AC.E5.8F.B8.E7.AE.80.E4.BB.8B"><span class="tocnumber">1</span> <span class="toctext">重庆药友制药有限责任公司简介</span></a></li>
<li class="toclevel-1 tocsection-2"><a href="#.E9.87.8D.E5.BA.86.E8.8D.AF.E5.8F.8B.E5.88.B6.E8.8D.AF.E6.9C.89.E9.99.90.E8.B4.A3.E4.BB.BB.E5.85.AC.E5.8F.B8.E5.87.BA.E5.93.81.E7.9A.84.E8.8D.AF.E5.93.81.E5.88.97.E8.A1.A8"><span class="tocnumber">2</span> <span class="toctext">重庆药友制药有限责任公司出品的药品列表</span></a></li>
<li class="toclevel-1 tocsection-3"><a href="#.E9.87.8D.E5.BA.86.E8.8D.AF.E5.8F.8B.E5.88.B6.E8.8D.AF.E6.9C.89.E9.99.90.E8.B4.A3.E4.BB.BB.E5.85.AC.E5.8F.B8.E5.9C.B0.E5.9B.BE"><span class="tocnumber">3</span> <span class="toctext">重庆药友制药有限责任公司地图</span></a></li>
<li class="toclevel-1 tocsection-4"><a href="#.E9.87.8D.E5.BA.86.E8.8D.AF.E5.8F.8B.E5.88.B6.E8.8D.AF.E6.9C.89.E9.99.90.E8.B4.A3.E4.BB.BB.E5.85.AC.E5.8F.B8.E9.99.84.E8.BF.91.E7.9A.84.E5.88.B6.E8.8D.AF.E4.BC.81.E4.B8.9A"><span class="tocnumber">4</span> <span class="toctext">重庆药友制药有限责任公司附近的制药企业</span></a></li>
<li class="toclevel-1 tocsection-5"><a href="#.E5.8F.82.E7.9C.8B"><span class="tocnumber">5</span> <span class="toctext">参看</span></a></li>
<li class="toclevel-1"><a href="#.E5.88.B6.E8.8D.AF.E4.BC.81.E4.B8.9A.E5.88.86.E5.8C.BA.E5.9F.9F.E6.9F.A5.E8.AF.A2"><span class="tocnumber">6</span> <span class="toctext">制药企业分区域查询</span></a></li>
</ul>
</td>
</tr>
</table>
<script type="text/javascript">
//<![CDATA[
if (window.showTocToggle) { var tocShowText = "显示"; var tocHideText = "隐藏"; showTocToggle(); } 
//]]>
</script>
<h2><span class="mw-headline" id=".E9.87.8D.E5.BA.86.E8.8D.AF.E5.8F.8B.E5.88.B6.E8.8D.AF.E6.9C.89.E9.99.90.E8.B4.A3.E4.BB.BB.E5.85.AC.E5.8F.B8.E7.AE.80.E4.BB.8B">重庆药友制药有限责任公司简介</span></h2>
<p><strong class="selflink">重庆药友制药有限责任公司</strong>创建于1939年，是由上海复星实业控股的高科技制药企业，地处重庆北部新区高新技术科技园，占地 18 万平方米、员工1000余名、年销售收入4亿元，是一家符合GMP，以生产<a href="/w/%E5%8C%96%E5%AD%A6" title="化学">化学</a>药物制剂为主，兼产化学<a href="/w/%E5%8E%9F%E6%96%99%E8%8D%AF" title="原料药">原料药</a>和<a href="/w/%E4%B8%AD%E8%8D%AF" title="中药">中药</a>制剂的综合性制药企业。</p>
<p>公司以“药友”为注册商标的<a href="/w/%E6%8A%97%E7%94%9F%E7%B4%A0%E7%B1%BB" title="抗生素类" class="mw-redirect">抗生素类</a>、<a href="/w/%E4%BF%9D%E8%82%9D" title="保肝">保肝</a>类、<a href="/index.php?title=%E8%A7%A3%E7%83%AD%E6%AD%A2%E7%97%9B&amp;action=edit&amp;redlink=1" class="new" title="解热止痛（尚未撰写）" rel="nofollow">解热止痛</a>类、<a href="/w/%E7%BB%B4%E7%94%9F%E7%B4%A0%E7%B1%BB" title="维生素类" class="mw-redirect">维生素类</a>、<a href="/w/%E5%BF%83%E8%A1%80%E7%AE%A1" title="心血管">心血管</a>类等300多个品种及规格的药物,以确切的疗效，优良的品质深得广大用户信赖，国内市场覆盖率达90%以上，部分产品畅销海外。1998年以来，药友制药连续被评为重庆市“工业企业五十强”、“文明单位”，“技术创新工作先进集体”、“新的经济增长点重点企业”、“质量效益型企业”；荣获重庆市“劳动创新奖状”、“生产经营管理成效显著奖”，2001年被国家科技部评为“国家级重点高新技术企业”，2004年被全国总工会授予“全国五一劳动奖状”。</p>
<h2><span class="mw-headline" id=".E9.87.8D.E5.BA.86.E8.8D.AF.E5.8F.8B.E5.88.B6.E8.8D.AF.E6.9C.89.E9.99.90.E8.B4.A3.E4.BB.BB.E5.85.AC.E5.8F.B8.E5.87.BA.E5.93.81.E7.9A.84.E8.8D.AF.E5.93.81.E5.88.97.E8.A1.A8">重庆药友制药有限责任公司出品的药品列表</span></h2>
<ul>
<li><b><a href="/w/%E6%B3%A8%E5%B0%84%E7%94%A8%E8%BF%98%E5%8E%9F%E5%9E%8B%E8%B0%B7%E8%83%B1%E7%94%98%E8%82%BD" title="注射用还原型谷胱甘肽">注射用还原型谷胱甘肽</a>（阿拓莫兰）</b>
<ul>
<li>批准字号：国药准字H20051599、国药准字H19991067、国药准字H20090044、国药准字H19991068</li>
<li>包装规格：1.0g /支；0.6g；0.9g；300mg</li>
<li>作用功效：用于：①<a href="/w/%E5%8C%96%E7%96%97" title="化疗">化疗</a>患者：包括用顺氯铵铂、<a href="/w/%E7%8E%AF%E7%A3%B7%E9%85%B0%E8%83%BA" title="环磷酰胺">环磷酰胺</a>、<a href="/w/%E9%98%BF%E9%9C%89%E7%B4%A0" title="阿霉素">阿霉素</a>、<a href="/w/%E7%BA%A2%E6%AF%94%E9%9C%89%E7%B4%A0" title="红比霉素" class="mw-redirect">红比霉素</a>、<a href="/w/%E5%8D%9A%E6%9D%A5%E9%9C%89%E7%B4%A0" title="博来霉素">博来霉素</a>化疗，尤其是<a href="/index.php?title=%E5%A4%A7%E5%89%82%E9%87%8F%E5%8C%96%E7%96%97&amp;action=edit&amp;redlink=1" class="new" title="大剂量化疗（尚未撰写）" rel="nofollow">大剂量化疗</a>时；②<a href="/w/%E6%94%BE%E5%B0%84%E6%B2%BB%E7%96%97" title="放射治疗">放射治疗</a>患者；③各种<a href="/w/%E4%BD%8E%E6%B0%A7%E8%A1%80%E7%97%87" title="低氧血症">低氧血症</a>：如<a href="/w/%E6%80%A5%E6%80%A7%E8%B4%AB%E8%A1%80" title="急性贫血">急性贫血</a>，<a href="/w/%E6%88%90%E4%BA%BA%E5%91%BC%E5%90%B8%E7%AA%98%E8%BF%AB%E7%BB%BC%E5%90%88%E7%97%87" title="成人呼吸窘迫综合症" class="mw-redirect">成人呼吸窘迫综合症</a>，<a href="/w/%E8%B4%A5%E8%A1%80%E7%97%87" title="败血症">败血症</a>等；④<a href="/w/%E8%82%9D%E8%84%8F" title="肝脏">肝脏</a>疾病：包括<a href="/w/%E7%97%85%E6%AF%92%E6%80%A7" title="病毒性">病毒性</a>、药物<a href="/w/%E6%AF%92%E6%80%A7" title="毒性">毒性</a>、<a href="/w/%E9%85%92%E7%B2%BE" title="酒精">酒精</a>毒性及其它化学物质毒性引起的肝脏损害。⑤亦可用于<a href="/w/%E6%9C%89%E6%9C%BA%E7%A3%B7" title="有机磷">有机磷</a>、胺基或硝基<a href="/w/%E5%8C%96%E5%90%88%E7%89%A9" title="化合物">化合物</a><a href="/w/%E4%B8%AD%E6%AF%92" title="中毒" class="mw-redirect">中毒</a>的辅助治疗。</li>
</ul>
</li>
<li><b><a href="/w/%E7%A1%AB%E8%BE%9B%E9%85%B8%E6%B3%A8%E5%B0%84%E6%B6%B2" title="硫辛酸注射液">硫辛酸注射液</a></b>
<ul>
<li>批准字号：国药准字H20066706</li>
<li>包装规格：6ml:150mg</li>
<li>作用功效：用于治疗肝炎、<a href="/w/%E8%84%82%E8%82%AA%E8%82%9D" title="脂肪肝">脂肪肝</a>、<a href="/w/%E8%82%9D%E7%A1%AC%E5%8F%98" title="肝硬变">肝硬变</a>、<a href="/w/%E8%82%9D%E6%80%A7%E6%98%8F%E8%BF%B7" title="肝性昏迷" class="mw-redirect">肝性昏迷</a>、<a href="/w/%E5%A6%8A%E5%A8%A0%E5%91%95%E5%90%90" title="妊娠呕吐">妊娠呕吐</a>等。</li>
</ul>
</li>
<li><b><a href="/w/%E6%B3%A8%E5%B0%84%E7%94%A8%E5%A4%B4%E5%AD%A2%E5%94%91%E6%9E%97%E9%92%A0" title="注射用头孢唑林钠">注射用头孢唑林钠</a>（注射用头孢唑林钠）</b>
<ul>
<li>批准字号：国药准字H50021533</li>
<li>包装规格：0.5g(按C14H14N8O4S3计)</li>
<li>作用功效：适用于治疗<a href="/w/%E6%95%8F%E6%84%9F%E7%BB%86%E8%8F%8C" title="敏感细菌" class="mw-redirect">敏感细菌</a>所致的<a href="/w/%E4%B8%AD%E8%80%B3%E7%82%8E" title="中耳炎">中耳炎</a>、<a href="/w/%E6%94%AF%E6%B0%94%E7%AE%A1%E7%82%8E" title="支气管炎">支气管炎</a>、<a href="/w/%E8%82%BA%E7%82%8E" title="肺炎">肺炎</a>等<a href="/w/%E5%91%BC%E5%90%B8%E9%81%93%E6%84%9F%E6%9F%93" title="呼吸道感染">呼吸道感染</a>、<a href="/w/%E5%B0%BF%E8%B7%AF%E6%84%9F%E6%9F%93" title="尿路感染">尿路感染</a>、<a href="/w/%E7%9A%AE%E8%82%A4%E8%BD%AF%E7%BB%84%E7%BB%87%E6%84%9F%E6%9F%93" title="皮肤软组织感染">皮肤软组织感染</a>、骨和<a href="/w/%E5%85%B3%E8%8A%82" title="关节">关节</a><a href="/w/%E6%84%9F%E6%9F%93" title="感染">感染</a>、<a href="/w/%E8%B4%A5%E8%A1%80%E7%97%87" title="败血症">败血症</a>、<a href="/w/%E6%84%9F%E6%9F%93%E6%80%A7%E5%BF%83%E5%86%85%E8%86%9C%E7%82%8E" title="感染性心内膜炎">感染性心内膜炎</a>、肝胆系统感染及眼、耳、鼻、喉科等感染。本品也可作为<a href="/w/%E5%A4%96%E7%A7%91%E6%89%8B%E6%9C%AF" title="外科手术" class="mw-redirect">外科手术</a>前的预防用药。本品不宜用于<a href="/w/%E4%B8%AD%E6%9E%A2%E7%A5%9E%E7%BB%8F%E7%B3%BB%E7%BB%9F%E6%84%9F%E6%9F%93" title="中枢神经系统感染">中枢神经系统感染</a>。对慢性尿路感染，尤其伴有尿路<a href="/w/%E8%A7%A3%E5%89%96" title="解剖">解剖</a>异常者的疗效较差。本品不宜用于治疗<a href="/w/%E6%B7%8B%E7%97%85" title="淋病">淋病</a>和<a href="/w/%E6%A2%85%E6%AF%92" title="梅毒">梅毒</a>。</li>
</ul>
</li>
<li><b><a href="/w/%E7%94%98%E9%9C%B2%E8%81%9A%E7%B3%96%E8%82%BD%E5%8F%A3%E6%9C%8D%E6%BA%B6%E6%B6%B2" title="甘露聚糖肽口服溶液">甘露聚糖肽口服溶液</a></b>
<ul>
<li>批准字号：国药准字H20003304</li>
<li>包装规格：10ml:10mg</li>
<li>作用功效：用于<a href="/w/%E5%85%8D%E7%96%AB%E5%8A%9F%E8%83%BD%E4%BD%8E%E4%B8%8B" title="免疫功能低下" class="mw-redirect">免疫功能低下</a>、反复<a href="/w/%E5%91%BC%E5%90%B8%E9%81%93%E6%84%9F%E6%9F%93" title="呼吸道感染">呼吸道感染</a>、<a href="/w/%E7%99%BD%E7%BB%86%E8%83%9E%E5%87%8F%E5%B0%91%E7%97%87" title="白细胞减少症" class="mw-redirect">白细胞减少症</a>和<a href="/w/%E5%86%8D%E7%94%9F%E9%9A%9C%E7%A2%8D%E6%80%A7%E8%B4%AB%E8%A1%80" title="再生障碍性贫血">再生障碍性贫血</a>及<a href="/w/%E8%82%BF%E7%98%A4" title="肿瘤">肿瘤</a>的辅助治疗，减轻放、<a href="/w/%E5%8C%96%E7%96%97" title="化疗">化疗</a>对<a href="/w/%E9%80%A0%E8%A1%80%E7%B3%BB%E7%BB%9F" title="造血系统">造血系统</a>的不良反应和<a href="/w/%E8%83%83%E8%82%A0%E9%81%93" title="胃肠道">胃肠道</a>反应</li>
</ul>
</li>
<li><b><a href="/w/%E8%90%98%E6%99%AE%E7%94%9F%E9%A2%97%E7%B2%92" title="萘普生颗粒">萘普生颗粒</a></b>
<ul>
<li>批准字号：国药准字H50021326</li>
<li>包装规格：10g:0.25g</li>
<li>作用功效：用于治疗风湿性和<a href="/w/%E7%B1%BB%E9%A3%8E%E6%B9%BF%E6%80%A7%E5%85%B3%E8%8A%82%E7%82%8E" title="类风湿性关节炎">类风湿性关节炎</a>、<a href="/w/%E9%AA%A8%E5%85%B3%E8%8A%82%E7%82%8E" title="骨关节炎">骨关节炎</a>、<a href="/w/%E5%BC%BA%E7%9B%B4%E6%80%A7%E8%84%8A%E6%9F%B1%E7%82%8E" title="强直性脊柱炎">强直性脊柱炎</a>、<a href="/w/%E7%97%9B%E9%A3%8E" title="痛风">痛风</a>、<a href="/w/%E5%85%B3%E8%8A%82%E7%82%8E" title="关节炎">关节炎</a>、<a href="/w/%E8%85%B1%E9%9E%98%E7%82%8E" title="腱鞘炎">腱鞘炎</a>。亦可用于缓解<a href="/w/%E8%82%8C%E8%82%89" title="肌肉">肌肉</a>骨骼<a href="/w/%E6%89%AD%E4%BC%A4" title="扭伤">扭伤</a>、<a href="/w/%E6%8C%AB%E4%BC%A4" title="挫伤">挫伤</a>、损伤以及<a href="/w/%E7%97%9B%E7%BB%8F" title="痛经">痛经</a>等所致的疼痛。</li>
</ul>
</li>
<li><b><a href="/w/%E9%85%AE%E6%B4%9B%E8%8A%AC%E6%A0%93" title="酮洛芬栓">酮洛芬栓</a></b>
<ul>
<li>批准字号：国药准字H50021956</li>
<li>包装规格：0.2g</li>
<li>作用功效：用于减轻中度疼痛如关<a href="/w/%E7%97%9B%E7%BB%8F" title="痛经">痛经</a>、<a href="/w/%E7%89%99%E7%97%9B" title="牙痛">牙痛</a>。</li>
</ul>
</li>
<li><b><a href="/w/%E7%BE%8E%E6%89%91%E4%BC%AA%E9%BA%BB%E7%89%87" title="美扑伪麻片">美扑伪麻片</a>（立林）</b>
<ul>
<li>批准字号：国药准字H10960213</li>
<li>包装规格：12粒/盒。</li>
<li>作用功效：适用于缓解<a href="/w/%E6%99%AE%E9%80%9A%E6%84%9F%E5%86%92" title="普通感冒" class="mw-redirect">普通感冒</a>及<a href="/w/%E6%B5%81%E8%A1%8C%E6%80%A7%E6%84%9F%E5%86%92" title="流行性感冒">流行性感冒</a>引起的<a href="/w/%E5%8F%91%E7%83%AD" title="发热">发热</a>、<a href="/w/%E5%A4%B4%E7%97%9B" title="头痛">头痛</a>、四肢酸痛、<a href="/w/%E6%89%93%E5%96%B7%E5%9A%8F" title="打喷嚏">打喷嚏</a>、<a href="/w/%E6%B5%81%E9%BC%BB%E6%B6%95" title="流鼻涕" class="mw-redirect">流鼻涕</a>、<a href="/w/%E9%BC%BB%E5%A1%9E" title="鼻塞">鼻塞</a>、<a href="/w/%E5%92%B3%E5%97%BD" title="咳嗽">咳嗽</a>、<a href="/w/%E5%92%BD%E7%97%9B" title="咽痛">咽痛</a>等症状。</li>
</ul>
</li>
<li><b><a href="/w/%E7%89%9B%E7%A3%BA%E9%85%B8%E6%95%A3" title="牛磺酸散">牛磺酸散</a></b>
<ul>
<li>批准字号：国药准字H50021241</li>
<li>包装规格：0.4g</li>
<li>作用功效：用于缓解<a href="/w/%E6%84%9F%E5%86%92" title="感冒">感冒</a>初期的<a href="/w/%E5%8F%91%E7%83%AD" title="发热">发热</a>.</li>
</ul>
</li>
<li><b><a href="/w/%E8%B0%B7%E6%B0%A8%E9%85%B0%E8%83%BA%E9%A2%97%E7%B2%92" title="谷氨酰胺颗粒">谷氨酰胺颗粒</a>（安凯舒）</b>
<ul>
<li>批准字号：国药准字H20020054</li>
<li>包装规格：2.5g</li>
<li>作用功效：主要适用于<a href="/w/%E7%83%A7%E4%BC%A4" title="烧伤">烧伤</a>、<a href="/w/%E5%88%9B%E4%BC%A4" title="创伤">创伤</a>、手术、<a href="/w/%E8%82%BF%E7%98%A4" title="肿瘤">肿瘤</a>放<a href="/w/%E5%8C%96%E7%96%97" title="化疗">化疗</a>等引起的<a href="/w/%E8%82%A0%E9%81%93" title="肠道">肠道</a>损伤、<a href="/w/%E5%85%8D%E7%96%AB%E5%8A%9F%E8%83%BD%E4%BD%8E%E4%B8%8B" title="免疫功能低下" class="mw-redirect">免疫功能低下</a>以及处于<a href="/w/%E5%88%86%E8%A7%A3%E4%BB%A3%E8%B0%A2" title="分解代谢">分解代谢</a>和<a href="/index.php?title=%E9%AB%98%E4%BB%A3%E8%B0%A2&amp;action=edit&amp;redlink=1" class="new" title="高代谢（尚未撰写）" rel="nofollow">高代谢</a>状况的病人的辅助治疗。</li>
</ul>
</li>
<li><b><a href="/w/%E9%86%8B%E9%85%B8%E5%8F%AF%E7%9A%84%E6%9D%BE%E6%B3%A8%E5%B0%84%E6%B6%B2" title="醋酸可的松注射液">醋酸可的松注射液</a></b>
<ul>
<li>批准字号：国药准字H50021603</li>
<li>包装规格：125mg/5ml/瓶</li>
<li>作用功效：用于治疗<a href="/w/%E5%8E%9F%E5%8F%91%E6%80%A7" title="原发性">原发性</a>或<a href="/w/%E7%BB%A7%E5%8F%91%E6%80%A7" title="继发性">继发性</a>肾上腺<a href="/w/%E7%9A%AE%E8%B4%A8%E5%8A%9F%E8%83%BD%E5%87%8F%E9%80%80" title="皮质功能减退">皮质功能减退</a>症，合成<a href="/w/%E7%B3%96%E7%9A%AE%E8%B4%A8%E6%BF%80%E7%B4%A0" title="糖皮质激素">糖皮质激素</a>所需酶系缺陷所致的各型<a href="/index.php?title=%E5%85%88%E5%A4%A9%E6%80%A7%E8%82%BE%E4%B8%8A%E8%85%BA%E5%A2%9E%E7%94%9F&amp;action=edit&amp;redlink=1" class="new" title="先天性肾上腺增生（尚未撰写）" rel="nofollow">先天性肾上腺增生</a>症，以及利用其药理作用治疗多种疾病，包括：1.<a href="/w/%E8%87%AA%E8%BA%AB%E5%85%8D%E7%96%AB%E6%80%A7%E7%96%BE%E7%97%85" title="自身免疫性疾病">自身免疫性疾病</a>：如<a href="/w/%E7%B3%BB%E7%BB%9F%E6%80%A7%E7%BA%A2%E6%96%91%E7%8B%BC%E7%96%AE" title="系统性红斑狼疮">系统性红斑狼疮</a>、<a href="/w/%E8%A1%80%E7%AE%A1%E7%82%8E" title="血管炎" class="mw-redirect">血管炎</a>、<a href="/w/%E5%A4%9A%E8%82%8C%E7%82%8E" title="多肌炎">多肌炎</a>、<a href="/w/%E7%9A%AE%E8%82%8C%E7%82%8E" title="皮肌炎">皮肌炎</a>、Still病、Graves’眼病、<a href="/w/%E8%87%AA%E8%BA%AB%E5%85%8D%E7%96%AB" title="自身免疫" class="mw-redirect">自身免疫</a>性溶血、<a href="/w/%E8%A1%80%E5%B0%8F%E6%9D%BF%E5%87%8F%E5%B0%91%E6%80%A7%E7%B4%AB%E7%99%9C" title="血小板减少性紫癜">血小板减少性紫癜</a>、<a href="/w/%E9%87%8D%E7%97%87%E8%82%8C%E6%97%A0%E5%8A%9B" title="重症肌无力" class="mw-redirect">重症肌无力</a>。2.<a href="/w/%E8%BF%87%E6%95%8F%E6%80%A7%E7%96%BE%E7%97%85" title="过敏性疾病">过敏性疾病</a>，如严重<a href="/w/%E6%94%AF%E6%B0%94%E7%AE%A1%E5%93%AE%E5%96%98" title="支气管哮喘">支气管哮喘</a>、<a href="/w/%E8%BF%87%E6%95%8F%E6%80%A7%E4%BC%91%E5%85%8B" title="过敏性休克">过敏性休克</a>、<a href="/w/%E8%A1%80%E6%B8%85%E7%97%85" title="血清病">血清病</a>、特异反应性<a href="/w/%E7%9A%AE%E7%82%8E" title="皮炎">皮炎</a>。3.<a href="/w/%E5%99%A8%E5%AE%98%E7%A7%BB%E6%A4%8D" title="器官移植">器官移植</a>排异反应，如肾、肝、心、等<a href="/w/%E7%BB%84%E7%BB%87%E7%A7%BB%E6%A4%8D" title="组织移植">组织移植</a>。4.<a href="/w/%E7%82%8E%E7%97%87" title="炎症">炎症</a>性疾患，如<a href="/w/%E8%8A%82%E6%AE%B5%E6%80%A7%E5%9B%9E%E8%82%A0%E7%82%8E" title="节段性回肠炎" class="mw-redirect">节段性回肠炎</a>、<a href="/w/%E6%BA%83%E7%96%A1%E6%80%A7%E7%BB%93%E8%82%A0%E7%82%8E" title="溃疡性结肠炎">溃疡性结肠炎</a>、非感染性炎性眼病。5.血液病，如<a href="/w/%E6%80%A5%E6%80%A7%E7%99%BD%E8%A1%80%E7%97%85" title="急性白血病">急性白血病</a>、<a href="/w/%E6%B7%8B%E5%B7%B4%E7%98%A4" title="淋巴瘤" class="mw-redirect">淋巴瘤</a>。6.其他：<a href="/w/%E7%BB%93%E8%8A%82%E7%97%85" title="结节病">结节病</a>、<a href="/w/%E7%94%B2%E7%8A%B6%E8%85%BA%E5%8D%B1%E8%B1%A1" title="甲状腺危象">甲状腺危象</a>、<a href="/w/%E4%BA%9A%E6%80%A5%E6%80%A7" title="亚急性">亚急性</a><a href="/index.php?title=%E9%9D%9E%E5%8C%96%E8%84%93%E6%80%A7%E7%94%B2%E7%8A%B6%E8%85%BA%E7%82%8E&amp;action=edit&amp;redlink=1" class="new" title="非化脓性甲状腺炎（尚未撰写）" rel="nofollow">非化脓性甲状腺炎</a>、败血性<a href="/w/%E4%BC%91%E5%85%8B" title="休克">休克</a>、<a href="/w/%E8%84%91%E6%B0%B4%E8%82%BF" title="脑水肿">脑水肿</a>、<a href="/w/%E8%82%BE%E7%97%85%E7%BB%BC%E5%90%88%E5%BE%81" title="肾病综合征">肾病综合征</a>、<a href="/w/%E9%AB%98%E9%92%99%E8%A1%80%E7%97%87" title="高钙血症">高钙血症</a>。</li>
</ul>
</li>
<li><b><a href="/w/%E6%B3%A8%E5%B0%84%E7%94%A8%E7%A1%AB%E9%85%B8%E9%93%BE%E9%9C%89%E7%B4%A0" title="注射用硫酸链霉素">注射用硫酸链霉素</a></b>
<ul>
<li>批准字号：国药准字H50020693</li>
<li>包装规格：1.0g(100万单位)</li>
<li>作用功效：本品主要与其他抗结核药联合用于<a href="/w/%E7%BB%93%E6%A0%B8%E5%88%86%E6%9E%9D%E6%9D%86%E8%8F%8C" title="结核分枝杆菌">结核分枝杆菌</a>所致各种<a href="/w/%E7%BB%93%E6%A0%B8%E7%97%85" title="结核病" class="mw-redirect">结核病</a>的初治病例，或其他敏感<a href="/w/%E5%88%86%E6%9E%9D%E6%9D%86%E8%8F%8C" title="分枝杆菌" class="mw-redirect">分枝杆菌</a><a href="/w/%E6%84%9F%E6%9F%93" title="感染">感染</a>。2．本品可单用于治疗<a href="/w/%E5%9C%9F%E6%8B%89%E8%8F%8C%E7%97%85" title="土拉菌病" class="mw-redirect">土拉菌病</a>，或与其他<a href="/w/%E6%8A%97%E8%8F%8C%E8%8D%AF%E7%89%A9" title="抗菌药物">抗菌药物</a>联合用于<a href="/w/%E9%BC%A0%E7%96%AB" title="鼠疫">鼠疫</a>、<a href="/w/%E8%85%B9%E8%82%A1%E6%B2%9F%E8%82%89%E8%8A%BD%E8%82%BF" title="腹股沟肉芽肿">腹股沟肉芽肿</a>、<a href="/w/%E5%B8%83%E9%B2%81%E8%8F%8C%E7%97%85" title="布鲁菌病" class="mw-redirect">布鲁菌病</a>、<a href="/w/%E9%BC%A0%E5%92%AC%E7%83%AD" title="鼠咬热">鼠咬热</a>等的治疗。3．亦可与<a href="/w/%E9%9D%92%E9%9C%89%E7%B4%A0" title="青霉素">青霉素</a>或<a href="/w/%E6%B0%A8%E8%8B%84%E8%A5%BF%E6%9E%97" title="氨苄西林">氨苄西林</a>联合治疗草绿色<a href="/w/%E9%93%BE%E7%90%83%E8%8F%8C" title="链球菌">链球菌</a>或肠球菌所致的<a href="/w/%E5%BF%83%E5%86%85%E8%86%9C%E7%82%8E" title="心内膜炎">心内膜炎</a>。</li>
</ul>
</li>
<li><b><a href="/w/%E9%98%BF%E8%8E%AB%E8%A5%BF%E6%9E%97%E8%83%B6%E5%9B%8A" title="阿莫西林胶囊">阿莫西林胶囊</a></b>
<ul>
<li>批准字号：国药准字H50020504</li>
<li>包装规格：0.25g(按C16H19N3O5S计)</li>
<li>作用功效：<a href="/w/%E9%98%BF%E8%8E%AB%E8%A5%BF%E6%9E%97" title="阿莫西林">阿莫西林</a>适用于敏感菌（不产β内酰胺酶<a href="/w/%E8%8F%8C%E6%A0%AA" title="菌株">菌株</a>）所致的下列<a href="/w/%E6%84%9F%E6%9F%93" title="感染">感染</a>：1．<a href="/index.php?title=%E6%BA%B6%E8%A1%80%E9%93%BE%E7%90%83%E8%8F%8C&amp;action=edit&amp;redlink=1" class="new" title="溶血链球菌（尚未撰写）" rel="nofollow">溶血链球菌</a>、<a href="/w/%E8%82%BA%E7%82%8E" title="肺炎">肺炎</a>链球菌、<a href="/w/%E8%91%A1%E8%90%84%E7%90%83%E8%8F%8C" title="葡萄球菌" class="mw-redirect">葡萄球菌</a>或<a href="/w/%E6%B5%81%E6%84%9F%E5%97%9C%E8%A1%80%E6%9D%86%E8%8F%8C" title="流感嗜血杆菌">流感嗜血杆菌</a>所致<a href="/w/%E4%B8%AD%E8%80%B3%E7%82%8E" title="中耳炎">中耳炎</a>、<a href="/w/%E9%BC%BB%E7%AA%A6%E7%82%8E" title="鼻窦炎">鼻窦炎</a>、<a href="/w/%E5%92%BD%E7%82%8E" title="咽炎">咽炎</a>、<a href="/w/%E6%89%81%E6%A1%83%E4%BD%93%E7%82%8E" title="扁桃体炎">扁桃体炎</a>等<a href="/w/%E4%B8%8A%E5%91%BC%E5%90%B8%E9%81%93%E6%84%9F%E6%9F%93" title="上呼吸道感染" class="mw-redirect">上呼吸道感染</a>。2．<a href="/w/%E5%A4%A7%E8%82%A0%E5%9F%83%E5%B8%8C%E8%8F%8C" title="大肠埃希菌" class="mw-redirect">大肠埃希菌</a>、奇异<a href="/w/%E5%8F%98%E5%BD%A2%E6%9D%86%E8%8F%8C" title="变形杆菌">变形杆菌</a>或粪肠球菌所致的泌尿生殖道感染。3．溶血链球菌、葡萄球菌或大肠埃希菌所致的<a href="/w/%E7%9A%AE%E8%82%A4%E8%BD%AF%E7%BB%84%E7%BB%87%E6%84%9F%E6%9F%93" title="皮肤软组织感染">皮肤软组织感染</a>。4．溶血链球菌、肺炎链球菌、葡萄球菌或流感嗜血杆菌所致<a href="/w/%E6%80%A5%E6%80%A7%E6%94%AF%E6%B0%94%E7%AE%A1%E7%82%8E" title="急性支气管炎">急性支气管炎</a>、肺炎等下<a href="/w/%E5%91%BC%E5%90%B8%E9%81%93%E6%84%9F%E6%9F%93" title="呼吸道感染">呼吸道感染</a>。5．急性单纯性<a href="/w/%E6%B7%8B%E7%97%85" title="淋病">淋病</a>。6．本品尚可用于治疗<a href="/w/%E4%BC%A4%E5%AF%92" title="伤寒">伤寒</a>、伤寒<a href="/w/%E5%B8%A6%E8%8F%8C%E8%80%85" title="带菌者" class="mw-redirect">带菌者</a>及<a href="/w/%E9%92%A9%E7%AB%AF%E8%9E%BA%E6%97%8B%E4%BD%93%E7%97%85" title="钩端螺旋体病">钩端螺旋体病</a>；阿莫西林亦可与<a href="/w/%E5%85%8B%E6%8B%89%E9%9C%89%E7%B4%A0" title="克拉霉素">克拉霉素</a>、<a href="/w/%E5%85%B0%E7%B4%A2%E6%8B%89%E5%94%91" title="兰索拉唑">兰索拉唑</a>三联用药根除胃、十二指肠<a href="/w/%E5%B9%BD%E9%97%A8%E8%9E%BA%E6%9D%86%E8%8F%8C" title="幽门螺杆菌">幽门螺杆菌</a>，降低<a href="/w/%E6%B6%88%E5%8C%96%E9%81%93" title="消化道">消化道</a><a href="/w/%E6%BA%83%E7%96%A1" title="溃疡">溃疡</a>复发率.</li>
</ul>
</li>
<li><b><a href="/w/%E6%B3%A8%E5%B0%84%E7%94%A8%E5%A4%B4%E5%AD%A2%E6%9B%B2%E6%9D%BE%E9%92%A0" title="注射用头孢曲松钠">注射用头孢曲松钠</a></b>
<ul>
<li>批准字号：国药准字H20053794</li>
<li>包装规格：1.5g。</li>
<li>作用功效：用于敏感<a href="/w/%E8%87%B4%E7%97%85%E8%8F%8C" title="致病菌">致病菌</a>所致的下<a href="/w/%E5%91%BC%E5%90%B8%E9%81%93%E6%84%9F%E6%9F%93" title="呼吸道感染">呼吸道感染</a>、尿路、<a href="/w/%E8%83%86%E9%81%93%E6%84%9F%E6%9F%93" title="胆道感染">胆道感染</a>，以及<a href="/w/%E8%85%B9%E8%85%94%E6%84%9F%E6%9F%93" title="腹腔感染">腹腔感染</a>、<a href="/w/%E7%9B%86%E8%85%94" title="盆腔">盆腔</a><a href="/w/%E6%84%9F%E6%9F%93" title="感染">感染</a>、<a href="/w/%E7%9A%AE%E8%82%A4%E8%BD%AF%E7%BB%84%E7%BB%87%E6%84%9F%E6%9F%93" title="皮肤软组织感染">皮肤软组织感染</a>、骨和<a href="/w/%E5%85%B3%E8%8A%82" title="关节">关节</a>感染、<a href="/w/%E8%B4%A5%E8%A1%80%E7%97%87" title="败血症">败血症</a>、<a href="/w/%E8%84%91%E8%86%9C%E7%82%8E" title="脑膜炎">脑膜炎</a>等及手术期感染预防。本品单剂可治疗单纯性<a href="/w/%E6%B7%8B%E7%97%85" title="淋病">淋病</a>。</li>
</ul>
</li>
<li><b><a href="/w/%E7%A3%BA%E8%83%BA%E4%BA%8C%E7%94%B2%E5%98%A7%E5%95%B6%E9%92%A0%E6%B3%A8%E5%B0%84%E6%B6%B2" title="磺胺二甲嘧啶钠注射液">磺胺二甲嘧啶钠注射液</a></b>
<ul>
<li>批准字号：国药准字H50021579</li>
<li>包装规格：2ml:0.2g</li>
<li>作用功效：用于<a href="/w/%E6%95%8F%E6%84%9F%E8%8F%8C" title="敏感菌">敏感菌</a>引起的下列<a href="/w/%E6%84%9F%E6%9F%93" title="感染">感染</a>，当患者不能口服时，如急性单纯性下<a href="/w/%E5%B0%BF%E8%B7%AF%E6%84%9F%E6%9F%93" title="尿路感染">尿路感染</a>、<a href="/w/%E6%80%A5%E6%80%A7%E4%B8%AD%E8%80%B3%E7%82%8E" title="急性中耳炎">急性中耳炎</a>和<a href="/w/%E7%9A%AE%E8%82%A4%E8%BD%AF%E7%BB%84%E7%BB%87%E6%84%9F%E6%9F%93" title="皮肤软组织感染">皮肤软组织感染</a>。</li>
</ul>
</li>
<li><b><a href="/w/%E5%A4%B4%E5%AD%A2%E6%B0%A8%E8%8B%84%E8%83%B6%E5%9B%8A" title="头孢氨苄胶囊">头孢氨苄胶囊</a></b>
<ul>
<li>批准字号：国药准字H50021314</li>
<li>包装规格：0.25g(按C16H17N3O4S计)</li>
<li>作用功效：适用于敏感菌所致的<a href="/w/%E6%80%A5%E6%80%A7%E6%89%81%E6%A1%83%E4%BD%93%E7%82%8E" title="急性扁桃体炎">急性扁桃体炎</a>、<a href="/w/%E5%92%BD%E5%B3%A1%E7%82%8E" title="咽峡炎">咽峡炎</a>、<a href="/w/%E4%B8%AD%E8%80%B3%E7%82%8E" title="中耳炎">中耳炎</a>、<a href="/w/%E9%BC%BB%E7%AA%A6%E7%82%8E" title="鼻窦炎">鼻窦炎</a>、<a href="/w/%E6%94%AF%E6%B0%94%E7%AE%A1%E7%82%8E" title="支气管炎">支气管炎</a>、<a href="/w/%E8%82%BA%E7%82%8E" title="肺炎">肺炎</a>等<a href="/w/%E5%91%BC%E5%90%B8%E9%81%93%E6%84%9F%E6%9F%93" title="呼吸道感染">呼吸道感染</a>、<a href="/w/%E5%B0%BF%E8%B7%AF%E6%84%9F%E6%9F%93" title="尿路感染">尿路感染</a>及<a href="/w/%E7%9A%AE%E8%82%A4%E8%BD%AF%E7%BB%84%E7%BB%87%E6%84%9F%E6%9F%93" title="皮肤软组织感染">皮肤软组织感染</a>等。本品为口服制剂，不宜用于重症<a href="/w/%E6%84%9F%E6%9F%93" title="感染">感染</a>。</li>
</ul>
</li>
<li><b><a href="/w/%E6%B3%A8%E5%B0%84%E7%94%A8%E6%B0%AF%E5%94%91%E8%A5%BF%E6%9E%97%E9%92%A0" title="注射用氯唑西林钠">注射用氯唑西林钠</a>（注射用氯唑西林钠）</b>
<ul>
<li>批准字号：国药准字H20033758</li>
<li>包装规格：0.5g</li>
<li>作用功效：本品仅适用于治疗产<a href="/w/%E9%9D%92%E9%9C%89%E7%B4%A0%E9%85%B6" title="青霉素酶">青霉素酶</a><a href="/w/%E8%91%A1%E8%90%84%E7%90%83%E8%8F%8C%E6%84%9F%E6%9F%93" title="葡萄球菌感染">葡萄球菌感染</a>，包括<a href="/w/%E8%B4%A5%E8%A1%80%E7%97%87" title="败血症">败血症</a>、<a href="/w/%E5%BF%83%E5%86%85%E8%86%9C%E7%82%8E" title="心内膜炎">心内膜炎</a>、<a href="/w/%E8%82%BA%E7%82%8E" title="肺炎">肺炎</a>和<a href="/w/%E7%9A%AE%E8%82%A4" title="皮肤">皮肤</a>、<a href="/w/%E8%BD%AF%E7%BB%84%E7%BB%87%E6%84%9F%E6%9F%93" title="软组织感染">软组织感染</a>等。也可用于化脓性<a href="/w/%E9%93%BE%E7%90%83%E8%8F%8C" title="链球菌">链球菌</a>或<a href="/w/%E8%82%BA%E7%82%8E%E7%90%83%E8%8F%8C" title="肺炎球菌" class="mw-redirect">肺炎球菌</a>与耐<a href="/w/%E9%9D%92%E9%9C%89%E7%B4%A0" title="青霉素">青霉素</a><a href="/w/%E8%91%A1%E8%90%84%E7%90%83%E8%8F%8C" title="葡萄球菌" class="mw-redirect">葡萄球菌</a>所致的<a href="/w/%E6%B7%B7%E5%90%88%E6%84%9F%E6%9F%93" title="混合感染">混合感染</a>。</li>
</ul>
</li>
<li><b><a href="/w/%E6%B3%A8%E5%B0%84%E7%94%A8%E7%A1%AB%E9%85%B8%E6%A0%B8%E7%B3%96%E9%9C%89%E7%B4%A0" title="注射用硫酸核糖霉素">注射用硫酸核糖霉素</a></b>
<ul>
<li>批准字号：国药准字H50020688</li>
<li>包装规格：1.0g（100万单位）。</li>
<li>作用功效：本品适用于敏感<a href="/w/%E8%82%A0%E6%9D%86%E8%8F%8C%E7%A7%91" title="肠杆菌科">肠杆菌科</a><a href="/w/%E7%BB%86%E8%8F%8C" title="细菌">细菌</a>如<a href="/w/%E5%A4%A7%E8%82%A0%E5%9F%83%E5%B8%8C%E8%8F%8C" title="大肠埃希菌" class="mw-redirect">大肠埃希菌</a>、克雷伯菌属、<a href="/w/%E5%8F%98%E5%BD%A2%E6%9D%86%E8%8F%8C%E5%B1%9E" title="变形杆菌属">变形杆菌属</a>、<a href="/w/%E5%BF%97%E8%B4%BA%E8%8F%8C%E5%B1%9E" title="志贺菌属" class="mw-redirect">志贺菌属</a>等引起的各种严重<a href="/w/%E6%84%9F%E6%9F%93" title="感染">感染</a>，如<a href="/w/%E8%82%BA%E7%82%8E" title="肺炎">肺炎</a>、<a href="/w/%E8%B4%A5%E8%A1%80%E7%97%87" title="败血症">败血症</a>、<a href="/w/%E8%83%86%E9%81%93%E6%84%9F%E6%9F%93" title="胆道感染">胆道感染</a>等。通常多与<a href="/w/%E5%B9%BF%E8%B0%B1" title="广谱">广谱</a><a href="/w/%E5%8D%8A%E5%90%88%E6%88%90" title="半合成">半合成</a><a href="/w/%E9%9D%92%E9%9C%89%E7%B4%A0%E7%B1%BB" title="青霉素类" class="mw-redirect">青霉素类</a>、<a href="/w/%E5%A4%B4%E5%AD%A2%E8%8F%8C%E7%B4%A0%E7%B1%BB" title="头孢菌素类" class="mw-redirect">头孢菌素类</a>或其他<a href="/w/%E6%8A%97%E8%8F%8C%E8%8D%AF%E7%89%A9" title="抗菌药物">抗菌药物</a>联合应用。</li>
</ul>
</li>
<li><b><a href="/w/%E6%B3%A8%E5%B0%84%E7%94%A8%E7%A1%AB%E9%85%B8%E9%98%BF%E7%B1%B3%E5%8D%A1%E6%98%9F" title="注射用硫酸阿米卡星">注射用硫酸阿米卡星</a></b>
<ul>
<li>批准字号：国药准字H50020687</li>
<li>包装规格：400mg/支</li>
<li>作用功效：本品适用于<a href="/w/%E9%93%9C%E7%BB%BF" title="铜绿" class="mw-redirect">铜绿</a>假单胞菌及部分其他<a href="/w/%E5%81%87%E5%8D%95%E8%83%9E%E8%8F%8C" title="假单胞菌">假单胞菌</a>、<a href="/w/%E5%A4%A7%E8%82%A0%E5%9F%83%E5%B8%8C%E8%8F%8C" title="大肠埃希菌" class="mw-redirect">大肠埃希菌</a>、<a href="/w/%E5%8F%98%E5%BD%A2%E6%9D%86%E8%8F%8C%E5%B1%9E" title="变形杆菌属">变形杆菌属</a>、克雷伯菌属、<a href="/w/%E8%82%A0%E6%9D%86%E8%8F%8C" title="肠杆菌" class="mw-redirect">肠杆菌</a>属、<a href="/index.php?title=%E6%B2%99%E9%9B%B7%E8%8F%8C%E5%B1%9E&amp;action=edit&amp;redlink=1" class="new" title="沙雷菌属（尚未撰写）" rel="nofollow">沙雷菌属</a>、不动杆菌属等敏感革兰阴性杆菌与<a href="/w/%E8%91%A1%E8%90%84%E7%90%83%E8%8F%8C%E5%B1%9E" title="葡萄球菌属">葡萄球菌属</a>(<a href="/w/%E7%94%B2%E6%B0%A7%E8%A5%BF%E6%9E%97" title="甲氧西林">甲氧西林</a>敏感株)所致严重<a href="/w/%E6%84%9F%E6%9F%93" title="感染">感染</a>，如<a href="/w/%E8%8F%8C%E8%A1%80%E7%97%87" title="菌血症">菌血症</a>或<a href="/w/%E8%B4%A5%E8%A1%80%E7%97%87" title="败血症">败血症</a>、<a href="/w/%E7%BB%86%E8%8F%8C%E6%80%A7%E5%BF%83%E5%86%85%E8%86%9C%E7%82%8E" title="细菌性心内膜炎">细菌性心内膜炎</a>、下<a href="/w/%E5%91%BC%E5%90%B8%E9%81%93%E6%84%9F%E6%9F%93" title="呼吸道感染">呼吸道感染</a>、骨关节感染、<a href="/w/%E8%83%86%E9%81%93%E6%84%9F%E6%9F%93" title="胆道感染">胆道感染</a>、<a href="/w/%E8%85%B9%E8%85%94%E6%84%9F%E6%9F%93" title="腹腔感染">腹腔感染</a>、<a href="/w/%E5%A4%8D%E6%9D%82%E6%80%A7%E5%B0%BF%E8%B7%AF%E6%84%9F%E6%9F%93" title="复杂性尿路感染">复杂性尿路感染</a>、<a href="/w/%E7%9A%AE%E8%82%A4%E8%BD%AF%E7%BB%84%E7%BB%87%E6%84%9F%E6%9F%93" title="皮肤软组织感染">皮肤软组织感染</a>等。由于本品对多数<a href="/w/%E6%B0%A8%E5%9F%BA%E7%B3%96%E8%8B%B7%E7%B1%BB" title="氨基糖苷类" class="mw-redirect">氨基糖苷类</a>钝化酶稳定，故尤其适用于治疗革兰阴性杆菌对<a href="/w/%E5%8D%A1%E9%82%A3%E9%9C%89%E7%B4%A0" title="卡那霉素">卡那霉素</a>、<a href="/w/%E5%BA%86%E5%A4%A7%E9%9C%89%E7%B4%A0" title="庆大霉素">庆大霉素</a>或<a href="/w/%E5%A6%A5%E5%B8%83%E9%9C%89%E7%B4%A0" title="妥布霉素">妥布霉素</a><a href="/w/%E8%80%90%E8%8D%AF%E8%8F%8C%E6%A0%AA" title="耐药菌株" class="mw-redirect">耐药菌株</a>所致的严重感染。</li>
</ul>
</li>
<li><b><a href="/w/%E6%B3%A8%E5%B0%84%E7%94%A8%E5%A4%B4%E5%AD%A2%E4%BB%96%E5%95%B6" title="注射用头孢他啶">注射用头孢他啶</a></b>
<ul>
<li>批准字号：国药准字H20054860、国药准字H20054861</li>
<li>包装规格：750mg(<a href="/w/%E5%A4%B4%E5%AD%A2%E4%BB%96%E5%95%B6" title="头孢他啶">头孢他啶</a>)。；1.5g(头孢他啶)</li>
<li>作用功效：用于敏感革兰阴性杆菌所致的<a href="/w/%E8%B4%A5%E8%A1%80%E7%97%87" title="败血症">败血症</a>、下<a href="/w/%E5%91%BC%E5%90%B8%E9%81%93%E6%84%9F%E6%9F%93" title="呼吸道感染">呼吸道感染</a>、腹腔和<a href="/w/%E8%83%86%E9%81%93%E6%84%9F%E6%9F%93" title="胆道感染">胆道感染</a>、<a href="/w/%E5%A4%8D%E6%9D%82%E6%80%A7%E5%B0%BF%E8%B7%AF%E6%84%9F%E6%9F%93" title="复杂性尿路感染">复杂性尿路感染</a>和严重<a href="/w/%E7%9A%AE%E8%82%A4%E8%BD%AF%E7%BB%84%E7%BB%87%E6%84%9F%E6%9F%93" title="皮肤软组织感染">皮肤软组织感染</a>等。对于由多种<a href="/w/%E8%80%90%E8%8D%AF" title="耐药" class="mw-redirect">耐药</a>革兰阴性杆菌引起的<a href="/w/%E5%85%8D%E7%96%AB%E7%BC%BA%E9%99%B7" title="免疫缺陷">免疫缺陷</a>者<a href="/w/%E6%84%9F%E6%9F%93" title="感染">感染</a>、<a href="/w/%E5%8C%BB%E9%99%A2%E5%86%85%E6%84%9F%E6%9F%93" title="医院内感染">医院内感染</a>以及革兰阴性杆菌或<a href="/w/%E9%93%9C%E7%BB%BF" title="铜绿" class="mw-redirect">铜绿</a>假单胞菌所致<a href="/w/%E4%B8%AD%E6%9E%A2%E7%A5%9E%E7%BB%8F%E7%B3%BB%E7%BB%9F%E6%84%9F%E6%9F%93" title="中枢神经系统感染">中枢神经系统感染</a>尤为适用。</li>
</ul>
</li>
<li><b><a href="/w/%E8%BF%98%E5%8E%9F%E5%9E%8B%E8%B0%B7%E8%83%B1%E7%94%98%E8%82%BD%E7%89%87" title="还原型谷胱甘肽片">还原型谷胱甘肽片</a>（阿拓莫兰）</b>
<ul>
<li>批准字号：国药准字H20050667</li>
<li>包装规格：0.1g；0.1g（<a href="/w/%E8%96%84%E8%86%9C%E8%A1%A3%E7%89%87" title="薄膜衣片">薄膜衣片</a>）</li>
<li>作用功效：解药物<a href="/w/%E6%AF%92%E6%80%A7" title="毒性">毒性</a>（<a href="/w/%E6%8A%97%E8%82%BF%E7%98%A4%E8%8D%AF" title="抗肿瘤药" class="mw-redirect">抗肿瘤药</a>、抗结核药、中枢神经药物、<a href="/w/%E5%AF%B9%E4%B9%99%E9%85%B0%E6%B0%A8%E5%9F%BA%E9%85%9A" title="对乙酰氨基酚">对乙酰氨基酚</a>等<a href="/w/%E4%B8%AD%E6%AF%92" title="中毒" class="mw-redirect">中毒</a>），防止<a href="/w/%E6%8A%97%E7%99%8C%E8%8D%AF%E7%89%A9" title="抗癌药物" class="mw-redirect">抗癌药物</a>的<a href="/w/%E5%89%AF%E4%BD%9C%E7%94%A8" title="副作用">副作用</a>，预防和治疗<a href="/w/%E6%94%BE%E5%B0%84%E7%BA%BF" title="放射线">放射线</a>损害；对抗<a href="/w/%E8%87%AA%E7%94%B1%E5%9F%BA" title="自由基">自由基</a>，抗氧化；提高机体免疫力……人体在许多状态下都可以使<a href="/w/%E7%BB%86%E8%83%9E" title="细胞">细胞</a>内<a href="/w/GSH" title="GSH" class="mw-redirect">GSH</a><a href="/w/%E7%94%9F%E7%89%A9%E5%90%88%E6%88%90" title="生物合成">生物合成</a>能力降低，含量下降，尤其是在<a href="/w/%E7%97%85%E7%90%86" title="病理">病理</a>状态下。外源性GSH的补充，可以预防、减轻、中止、组织细胞的损伤，改变病理生理过程。</li>
</ul>
</li>
<li><b><a href="/w/%E9%98%BF%E6%B3%95%E9%AA%A8%E5%8C%96%E9%86%87%E7%89%87" title="阿法骨化醇片">阿法骨化醇片</a>（立庆）</b>
<ul>
<li>批准字号：国药准字H10950135、国药准字H10950134</li>
<li>包装规格：0.25μg；0.5ug</li>
<li>作用功效：预防和治疗<a href="/w/%E9%AA%A8%E8%B4%A8%E7%96%8F%E6%9D%BE" title="骨质疏松">骨质疏松</a>，<a href="/w/%E8%82%BE%E6%80%A7%E9%AA%A8%E7%97%85" title="肾性骨病">肾性骨病</a>，肾性甲旁亢，<a href="/w/%E7%94%B2%E7%8A%B6%E6%97%81%E8%85%BA" title="甲状旁腺">甲状旁腺</a>功能低下以及其他<a href="/w/%E7%BB%B4%E7%94%9F%E7%B4%A0D" title="维生素D">维生素D</a><a href="/index.php?title=%E4%BB%A3%E8%B0%A2%E5%BC%82%E5%B8%B8&amp;action=edit&amp;redlink=1" class="new" title="代谢异常（尚未撰写）" rel="nofollow">代谢异常</a>疾病。</li>
</ul>
</li>
<li><b><a href="/w/%E8%86%A6%E7%94%B2%E9%85%B8%E9%92%A0%E6%B0%AF%E5%8C%96%E9%92%A0%E6%B3%A8%E5%B0%84%E6%B6%B2" title="膦甲酸钠氯化钠注射液">膦甲酸钠氯化钠注射液</a>（易可亚）</b>
<ul>
<li>批准字号：国药准字H20030125</li>
<li>包装规格：100ml:2.4g</li>
</ul>
</li>
<li><b><a href="/w/%E7%9B%90%E9%85%B8%E6%99%AE%E8%90%98%E6%B4%9B%E5%B0%94%E6%B3%A8%E5%B0%84%E6%B6%B2" title="盐酸普萘洛尔注射液">盐酸普萘洛尔注射液</a></b>
<ul>
<li>批准字号：国药准字H50021242</li>
<li>包装规格：5ml:5mg</li>
<li>作用功效：<a href="/w/%E9%AB%98%E8%A1%80%E5%8E%8B" title="高血压">高血压</a>、心率失常、减轻<a href="/w/%E5%BF%83%E7%BB%9E%E7%97%9B" title="心绞痛">心绞痛</a>、<a href="/w/%E5%BF%83%E6%82%B8" title="心悸">心悸</a>与<a href="/w/%E6%98%8F%E5%8E%A5" title="昏厥">昏厥</a>等症状等。</li>
</ul>
</li>
<li><b><a href="/w/%E6%B3%A8%E5%B0%84%E7%94%A8%E8%85%BA%E8%8B%B7%E9%92%B4%E8%83%BA" title="注射用腺苷钴胺">注射用腺苷钴胺</a>（米乐卡）</b>
<ul>
<li>批准字号：国药准字H20066850、国药准字H20066456、国药准字H20066849</li>
<li>包装规格：1.5mg；0.5mg；1.0mg</li>
<li>作用功效：主要用巨幼红细胞<a href="/w/%E8%B4%AB%E8%A1%80" title="贫血">贫血</a>，<a href="/w/%E8%90%A5%E5%85%BB%E4%B8%8D%E8%89%AF" title="营养不良">营养不良</a>性贫血，<a href="/w/%E5%A6%8A%E5%A8%A0%E6%9C%9F" title="妊娠期">妊娠期</a>贫血，<a href="/w/%E5%A4%9A%E5%8F%91%E6%80%A7%E7%A5%9E%E7%BB%8F%E7%82%8E" title="多发性神经炎">多发性神经炎</a>，<a href="/index.php?title=%E7%A5%9E%E7%BB%8F%E6%A0%B9%E7%82%8E&amp;action=edit&amp;redlink=1" class="new" title="神经根炎（尚未撰写）" rel="nofollow">神经根炎</a>，<a href="/w/%E4%B8%89%E5%8F%89%E7%A5%9E%E7%BB%8F%E7%97%9B" title="三叉神经痛">三叉神经痛</a>，<a href="/w/%E5%9D%90%E9%AA%A8%E7%A5%9E%E7%BB%8F%E7%97%9B" title="坐骨神经痛">坐骨神经痛</a>，<a href="/index.php?title=%E7%A5%9E%E7%BB%8F%E9%BA%BB%E7%97%B9&amp;action=edit&amp;redlink=1" class="new" title="神经麻痹（尚未撰写）" rel="nofollow">神经麻痹</a>，也可用于营养不良性产品以及<a href="/w/%E6%94%BE%E5%B0%84%E7%BA%BF" title="放射线">放射线</a>与药物引起的<a href="/w/%E7%99%BD%E7%BB%86%E8%83%9E%E5%87%8F%E5%B0%91%E7%97%87" title="白细胞减少症" class="mw-redirect">白细胞减少症</a>。</li>
</ul>
</li>
<li><b><a href="/w/%E6%B0%AF%E5%8C%96%E9%92%BE%E9%A2%97%E7%B2%92" title="氯化钾颗粒">氯化钾颗粒</a></b>
<ul>
<li>批准字号：国药准字H50020683</li>
<li>包装规格：10g:1.5g</li>
<li>作用功效：治疗<a href="/w/%E4%BD%8E%E9%92%BE%E8%A1%80%E7%97%87" title="低钾血症">低钾血症</a>。</li>
</ul>
</li>
<li><b><a href="/w/%E6%B3%A8%E5%B0%84%E7%94%A8%E6%B0%B4%E6%BA%B6%E6%80%A7%E7%BB%B4%E7%94%9F%E7%B4%A0" title="注射用水溶性维生素">注射用水溶性维生素</a></b>
<ul>
<li>批准字号：国药准字H50020795</li>
<li>包装规格：<a href="/w/%E5%A4%8D%E6%96%B9" title="复方">复方</a></li>
<li>作用功效：本品系<a href="/w/%E8%82%A0%E5%A4%96%E8%90%A5%E5%85%BB" title="肠外营养">肠外营养</a>不可少组成部分之一，用以满足成人和儿童每日对<a href="/w/%E6%B0%B4%E6%BA%B6%E6%80%A7%E7%BB%B4%E7%94%9F%E7%B4%A0" title="水溶性维生素">水溶性维生素</a>的<a href="/w/%E7%94%9F%E7%90%86" title="生理" class="mw-redirect">生理</a>需要。</li>
</ul>
</li>
<li><b><a href="/w/%E5%A4%8D%E6%96%B9%E6%B0%A8%E5%9F%BA%E9%85%B8%E6%B3%A8%E5%B0%84%E6%B6%B2(18AA)" title="复方氨基酸注射液(18AA)">复方氨基酸注射液(18AA)</a></b>
<ul>
<li>批准字号：国药准字H50020790、国药准字H50021600、国药准字H50020906</li>
<li>包装规格：500ml:25g(总<a href="/w/%E6%B0%A8%E5%9F%BA%E9%85%B8" title="氨基酸">氨基酸</a>)；200ml:10g(总氨基酸)；250ml:30g(总氨基酸)</li>
<li>作用功效：<a href="/index.php?title=%E6%B0%A8%E5%9F%BA%E9%85%B8%E7%B1%BB&amp;action=edit&amp;redlink=1" class="new" title="氨基酸类（尚未撰写）" rel="nofollow">氨基酸类</a>药。用于<a href="/w/%E8%9B%8B%E7%99%BD%E8%B4%A8" title="蛋白质">蛋白质</a>摄入不足、<a href="/w/%E5%90%B8%E6%94%B6%E9%9A%9C%E7%A2%8D" title="吸收障碍" class="mw-redirect">吸收障碍</a>等<a href="/w/%E6%B0%A8%E5%9F%BA%E9%85%B8" title="氨基酸">氨基酸</a>不能满足机体<a href="/w/%E4%BB%A3%E8%B0%A2" title="代谢">代谢</a>需要的患者。亦用于改善手术后病人的营养状况。</li>
</ul>
</li>
<li><b><a href="/w/%E7%BB%B4%E7%94%9F%E7%B4%A0B6%E6%B3%A8%E5%B0%84%E6%B6%B2" title="维生素B6注射液">维生素B6注射液</a></b>
<ul>
<li>批准字号：国药准字H50021582、国药准字H50021580、国药准字H50021583、国药准字H50021581</li>
<li>包装规格：2ml:50mg；1ml:50mg；2ml:100mg；1ml:25mg</li>
<li>作用功效：1、适用于维生素B6缺乏的预防和治疗，防治<a href="/w/%E5%BC%82%E7%83%9F%E8%82%BC%E4%B8%AD%E6%AF%92" title="异烟肼中毒">异烟肼中毒</a>；也可用于<a href="/w/%E5%A6%8A%E5%A8%A0" title="妊娠">妊娠</a>、<a href="/w/%E6%94%BE%E5%B0%84%E7%97%85" title="放射病">放射病</a>及抗癌药所致的 <a href="/w/%E5%91%95%E5%90%90" title="呕吐">呕吐</a>，脂溢性 <a href="/w/%E7%9A%AE%E7%82%8E" title="皮炎">皮炎</a>等。2、全<a href="/w/%E8%83%83%E8%82%A0%E9%81%93" title="胃肠道">胃肠道</a>外营养及因摄入不足所致<a href="/w/%E8%90%A5%E5%85%BB%E4%B8%8D%E8%89%AF" title="营养不良">营养不良</a>、进行性体重下降 时维生素 B6的补充。3、下列情况对<a href="/w/%E7%BB%B4%E7%94%9F%E7%B4%A0B6" title="维生素B6">维生素B6</a>需要量增加：妊娠及<a href="/w/%E5%93%BA%E4%B9%B3%E6%9C%9F" title="哺乳期">哺乳期</a>、<a href="/w/%E7%94%B2%E7%8A%B6%E8%85%BA%E5%8A%9F%E8%83%BD%E4%BA%A2%E8%BF%9B" title="甲状腺功能亢进" class="mw-redirect">甲状腺功能亢进</a>、<a href="/w/%E7%83%A7%E4%BC%A4" title="烧伤">烧伤</a>、长 期慢性<a href="/w/%E6%84%9F%E6%9F%93" title="感染">感染</a>、 <a href="/w/%E5%8F%91%E7%83%AD" title="发热">发热</a>、先天性代谢障碍病（<a href="/index.php?title=%E8%83%B1%E7%A1%AB%E9%86%9A%E5%B0%BF%E7%97%87&amp;action=edit&amp;redlink=1" class="new" title="胱硫醚尿症（尚未撰写）" rel="nofollow">胱硫醚尿症</a>、高草酸盐症、<a href="/w/%E9%AB%98%E8%83%B1%E6%B0%A8%E9%85%B8%E5%B0%BF%E7%97%87" title="高胱氨酸尿症">高胱氨酸尿症</a>、黄 嘌呤<a href="/index.php?title=%E9%85%B8%E5%B0%BF&amp;action=edit&amp;redlink=1" class="new" title="酸尿（尚未撰写）" rel="nofollow">酸尿</a>症）、<a href="/w/%E5%85%85%E8%A1%80%E6%80%A7%E5%BF%83%E5%8A%9B%E8%A1%B0%E7%AB%AD" title="充血性心力衰竭">充血性心力衰竭</a>、长期<a href="/w/%E8%A1%80%E6%B6%B2%E9%80%8F%E6%9E%90" title="血液透析">血液透析</a>、吸收不良综合症伴肝胆系统疾病（如<a href="/w/%E9%85%92%E7%B2%BE%E4%B8%AD%E6%AF%92" title="酒精中毒">酒精中毒</a>伴 肝硬 化）、<a href="/w/%E8%82%A0%E9%81%93" title="肠道">肠道</a>疾病（<a href="/w/%E4%B9%B3%E7%B3%9C%E6%B3%BB" title="乳糜泻" class="mw-redirect">乳糜泻</a>、热带口炎性<a href="/w/%E8%82%A0%E7%82%8E" title="肠炎">肠炎</a> 、<a href="/w/%E5%B1%80%E9%99%90%E6%80%A7%E8%82%A0%E7%82%8E" title="局限性肠炎" class="mw-redirect">局限性肠炎</a>、持续<a href="/w/%E8%85%B9%E6%B3%BB" title="腹泻">腹泻</a>）、<a href="/w/%E8%83%83%E5%88%87%E9%99%A4%E6%9C%AF" title="胃切除术">胃切除术</a>后。4、<a href="/w/%E6%96%B0%E7%94%9F%E5%84%BF" title="新生儿">新生儿</a>遗传性<a href="/w/%E7%BB%B4%E7%94%9F%E7%B4%A0B6%E4%BE%9D%E8%B5%96%E7%BB%BC%E5%90%88%E5%BE%81" title="维生素B6依赖综合征">维生素B6依赖综合征</a>。</li>
</ul>
</li>
<li><b><a href="/w/%E4%BA%9A%E5%8F%B6%E9%85%B8%E9%92%99%E6%B3%A8%E5%B0%84%E6%B6%B2" title="亚叶酸钙注射液">亚叶酸钙注射液</a></b>
<ul>
<li>批准字号：国药准字H20010615</li>
<li>包装规格：10ml：0.1g（以<a href="/w/%E4%BA%9A%E5%8F%B6%E9%85%B8" title="亚叶酸">亚叶酸</a>计）</li>
<li>作用功效：1．<a href="/w/%E5%B0%BF%E5%98%A7%E5%95%B6" title="尿嘧啶">尿嘧啶</a>合用，可提高<a href="/w/%E6%B0%9F%E5%B0%BF%E5%98%A7%E5%95%B6" title="氟尿嘧啶" class="mw-redirect">氟尿嘧啶</a>的疗效，临床上常用于<a href="/w/%E7%BB%93%E7%9B%B4%E8%82%A0%E7%99%8C" title="结直肠癌" class="mw-redirect">结直肠癌</a>与<a href="/w/%E8%83%83%E7%99%8C" title="胃癌">胃癌</a>的治疗。2．作<a href="/w/%E5%8F%B6%E9%85%B8" title="叶酸">叶酸</a><a href="/w/%E6%8B%AE%E6%8A%97%E5%89%82" title="拮抗剂">拮抗剂</a>（如<a href="/w/%E7%94%B2%E6%B0%A8%E5%96%8B%E5%91%A4" title="甲氨喋呤" class="mw-redirect">甲氨喋呤</a>、<a href="/w/%E4%B9%99%E8%83%BA%E5%98%A7%E5%95%B6" title="乙胺嘧啶">乙胺嘧啶</a>或<a href="/w/%E7%94%B2%E6%B0%A7%E8%8B%84%E5%95%B6" title="甲氧苄啶">甲氧苄啶</a>等）的<a href="/w/%E8%A7%A3%E6%AF%92%E5%89%82" title="解毒剂" class="mw-redirect">解毒剂</a>。本品临床常用于预防甲氨喋呤过量等大剂量治疗后所引起的严重<a href="/w/%E6%AF%92%E6%80%A7" title="毒性">毒性</a>作用。3．于<a href="/w/%E5%8F%A3%E7%82%8E%E6%80%A7%E8%85%B9%E6%B3%BB" title="口炎性腹泻">口炎性腹泻</a>、<a href="/w/%E8%90%A5%E5%85%BB%E4%B8%8D%E8%89%AF" title="营养不良">营养不良</a>、<a href="/w/%E5%A6%8A%E5%A8%A0%E6%9C%9F" title="妊娠期">妊娠期</a>或<a href="/w/%E5%A9%B4%E5%84%BF%E6%9C%9F" title="婴儿期">婴儿期</a>引起的<a href="/w/%E5%B7%A8%E5%B9%BC%E7%BB%86%E8%83%9E%E6%80%A7%E8%B4%AB%E8%A1%80" title="巨幼细胞性贫血">巨幼细胞性贫血</a>，当口服叶酸疗效不佳时。对<a href="/index.php?title=%E7%BB%B4%E7%94%9F%E7%B4%A0B12%E7%BC%BA%E4%B9%8F%E6%80%A7%E8%B4%AB%E8%A1%80&amp;action=edit&amp;redlink=1" class="new" title="维生素B12缺乏性贫血（尚未撰写）" rel="nofollow">维生素B12缺乏性贫血</a>并不适用。</li>
</ul>
</li>
<li><b><a href="/w/%E5%90%B2%E8%BE%BE%E5%B8%95%E8%83%BA%E7%89%87" title="吲达帕胺片">吲达帕胺片</a></b>
<ul>
<li>批准字号：国药准字H50021320</li>
<li>包装规格：2.5mg</li>
<li>作用功效：用于治疗高血压。 主要用于治疗轻度、中度高<a href="/w/%E8%A1%80%E5%8E%8B" title="血压">血压</a>，对<a href="/w/%E8%82%BE%E6%80%A7%E9%AB%98%E8%A1%80%E5%8E%8B" title="肾性高血压">肾性高血压</a>、<a href="/w/%E7%B3%96%E5%B0%BF%E7%97%85" title="糖尿病">糖尿病</a>性<a href="/w/%E9%AB%98%E8%A1%80%E5%8E%8B" title="高血压">高血压</a>有较好的疗效。</li>
</ul>
</li>
<li><b><a href="/w/%E6%B3%A8%E5%B0%84%E7%94%A8%E5%89%8D%E5%88%97%E5%9C%B0%E5%B0%94" title="注射用前列地尔">注射用前列地尔</a>（快乐斯）</b>
<ul>
<li>批准字号：国药准字H50021597、国药准字H50021598、国药准字H20057824、国药准字H50021393</li>
<li>包装规格：30ug；200ug；40μg；20μg</li>
<li>作用功效：用于<a href="/w/%E5%BF%83%E8%82%8C%E6%A2%97%E6%AD%BB" title="心肌梗死" class="mw-redirect">心肌梗死</a>，<a href="/w/%E8%A1%80%E6%A0%93%E6%80%A7%E8%84%89%E7%AE%A1%E7%82%8E" title="血栓性脉管炎">血栓性脉管炎</a>、<a href="/w/%E9%97%AD%E5%A1%9E%E6%80%A7%E5%8A%A8%E8%84%89%E7%A1%AC%E5%8C%96" title="闭塞性动脉硬化" class="mw-redirect">闭塞性动脉硬化</a>等症。</li>
</ul>
</li>
<li><b><a href="/w/%E9%AB%98%E4%B8%89%E5%B0%96%E6%9D%89%E9%85%AF%E7%A2%B1%E6%B3%A8%E5%B0%84%E6%B6%B2" title="高三尖杉酯碱注射液">高三尖杉酯碱注射液</a></b>
<ul>
<li>批准字号：国药准字H50021101、国药准字H50021102</li>
<li>包装规格：1ml:1mg；2ml:2mg</li>
<li>作用功效：适用于各型急性非淋巴细胞<a href="/w/%E7%99%BD%E8%A1%80%E7%97%85" title="白血病">白血病</a>，对<a href="/w/%E9%AA%A8%E9%AB%93%E5%A2%9E%E7%94%9F%E5%BC%82%E5%B8%B8%E7%BB%BC%E5%90%88%E5%BE%81" title="骨髓增生异常综合征">骨髓增生异常综合征</a>（MDS）、<a href="/w/%E6%85%A2%E6%80%A7%E7%B2%92%E7%BB%86%E8%83%9E%E6%80%A7%E7%99%BD%E8%A1%80%E7%97%85" title="慢性粒细胞性白血病">慢性粒细胞性白血病</a>及<a href="/w/%E7%9C%9F%E6%80%A7%E7%BA%A2%E7%BB%86%E8%83%9E%E5%A2%9E%E5%A4%9A%E7%97%87" title="真性红细胞增多症">真性红细胞增多症</a>等亦有一定疗效。</li>
</ul>
</li>
<li><b><a href="/w/%E9%85%9A%E7%A3%BA%E4%B9%99%E8%83%BA%E6%B3%A8%E5%B0%84%E6%B6%B2" title="酚磺乙胺注射液">酚磺乙胺注射液</a></b>
<ul>
<li>批准字号：国药准字H50020580、国药准字H50020579、国药准字H50020581</li>
<li>包装规格：5ml:1g；2ml:0.25g；2ml:0.5g</li>
<li>作用功效：1.用于防治多种手术前、后的<a href="/w/%E5%87%BA%E8%A1%80" title="出血">出血</a>。 2.也可用于<a href="/w/%E8%A1%80%E5%B0%8F%E6%9D%BF" title="血小板">血小板</a>功能不良、<a href="/w/%E8%A1%80%E7%AE%A1" title="血管">血管</a>脆性增加而引起的出血，如<a href="/w/%E8%A1%80%E5%B0%8F%E6%9D%BF%E5%87%8F%E5%B0%91%E6%80%A7%E7%B4%AB%E7%99%9C" title="血小板减少性紫癜">血小板减少性紫癜</a>、<a href="/w/%E8%BF%87%E6%95%8F%E6%80%A7%E7%B4%AB%E7%99%9C" title="过敏性紫癜">过敏性紫癜</a>。 3.还可用于其它原因引起的出血，如<a href="/w/%E8%84%91%E5%87%BA%E8%A1%80" title="脑出血">脑出血</a>、<a href="/w/%E8%83%83%E8%82%A0%E9%81%93%E5%87%BA%E8%A1%80" title="胃肠道出血">胃肠道出血</a>、<a href="/index.php?title=%E6%B3%8C%E5%B0%BF%E9%81%93%E5%87%BA%E8%A1%80&amp;action=edit&amp;redlink=1" class="new" title="泌尿道出血（尚未撰写）" rel="nofollow">泌尿道出血</a>、<a href="/w/%E7%9C%BC%E5%BA%95%E5%87%BA%E8%A1%80" title="眼底出血">眼底出血</a>、<a href="/w/%E9%BD%BF%E9%BE%88%E5%87%BA%E8%A1%80" title="齿龈出血">齿龈出血</a>、<a href="/w/%E9%BC%BB%E5%87%BA%E8%A1%80" title="鼻出血">鼻出血</a>和<a href="/index.php?title=%E7%9A%AE%E8%82%A4%E5%87%BA%E8%A1%80&amp;action=edit&amp;redlink=1" class="new" title="皮肤出血（尚未撰写）" rel="nofollow">皮肤出血</a>等。</li>
</ul>
</li>
<li><b><a href="/w/%E5%8F%8C%E5%98%A7%E8%BE%BE%E8%8E%AB%E6%B3%A8%E5%B0%84%E6%B6%B2" title="双嘧达莫注射液">双嘧达莫注射液</a></b>
<ul>
<li>批准字号：国药准字H50020900</li>
<li>包装规格：2ml:10mg</li>
<li>作用功效：诊断<a href="/w/%E5%BF%83%E8%82%8C%E7%BC%BA%E8%A1%80" title="心肌缺血">心肌缺血</a>的药物实验。</li>
</ul>
</li>
<li><b><a href="/w/%E7%BB%B4%E7%94%9F%E7%B4%A0C%E6%B3%A8%E5%B0%84%E6%B6%B2" title="维生素C注射液">维生素C注射液</a></b>
<ul>
<li>批准字号：国药准字H50021541、国药准字H50021543、国药准字H50021539、国药准字H50021542、国药准字H50021540</li>
<li>包装规格：2ml:0.5g；20ml:2.5g；2ml:0.1g；5ml:0.5g；2ml:0.25g</li>
<li>作用功效：1、用于治疗<a href="/w/%E5%9D%8F%E8%A1%80%E7%97%85" title="坏血病">坏血病</a>，也可用于各种急慢性传染性疾病及<a href="/w/%E7%B4%AB%E7%99%9C" title="紫癜">紫癜</a>等辅助治疗。 2、慢性<a href="/w/%E9%93%81%E4%B8%AD%E6%AF%92" title="铁中毒">铁中毒</a>的治疗：<a href="/w/%E7%BB%B4%E7%94%9F%E7%B4%A0C" title="维生素C">维生素C</a>促进<a href="/w/%E5%8E%BB%E9%93%81%E8%83%BA" title="去铁胺">去铁胺</a>对铁的螯合，使铁排出加速。 3、特发性<a href="/w/%E9%AB%98%E9%93%81%E8%A1%80%E7%BA%A2%E8%9B%8B%E7%99%BD" title="高铁血红蛋白">高铁血红蛋白</a>症的治疗。 4、下列情况对维生素C的需要量增加：(1)病人接受慢性<a href="/w/%E8%A1%80%E6%B6%B2%E9%80%8F%E6%9E%90" title="血液透析">血液透析</a>、<a href="/w/%E8%83%83%E8%82%A0%E9%81%93" title="胃肠道">胃肠道</a>疾病(长期<a href="/w/%E8%85%B9%E6%B3%BB" title="腹泻">腹泻</a>、胃或<a href="/index.php?title=%E5%9B%9E%E8%82%A0%E5%88%87%E9%99%A4%E6%9C%AF&amp;action=edit&amp;redlink=1" class="new" title="回肠切除术（尚未撰写）" rel="nofollow">回肠切除术</a>后)、<a href="/w/%E7%BB%93%E6%A0%B8%E7%97%85" title="结核病" class="mw-redirect">结核病</a>、<a href="/w/%E7%99%8C%E7%97%87" title="癌症">癌症</a>、<a href="/w/%E6%BA%83%E7%96%A1%E7%97%85" title="溃疡病" class="mw-redirect">溃疡病</a>、<a href="/w/%E7%94%B2%E7%8A%B6%E8%85%BA%E5%8A%9F%E8%83%BD%E4%BA%A2%E8%BF%9B" title="甲状腺功能亢进" class="mw-redirect">甲状腺功能亢进</a>、<a href="/w/%E5%8F%91%E7%83%AD" title="发热">发热</a>、<a href="/w/%E6%84%9F%E6%9F%93" title="感染">感染</a>、<a href="/w/%E5%88%9B%E4%BC%A4" title="创伤">创伤</a>、<a href="/w/%E7%83%A7%E4%BC%A4" title="烧伤">烧伤</a>、手术等；(2)因严格控制或选择饮食，接受<a href="/w/%E8%82%A0%E9%81%93" title="肠道">肠道</a>外营养的病人，因<a href="/w/%E8%90%A5%E5%85%BB%E4%B8%8D%E8%89%AF" title="营养不良">营养不良</a>，体重骤降，以及在<a href="/w/%E5%A6%8A%E5%A8%A0%E6%9C%9F" title="妊娠期">妊娠期</a>和<a href="/w/%E5%93%BA%E4%B9%B3%E6%9C%9F" title="哺乳期">哺乳期</a>；(3)应用巴比妥类、<a href="/w/%E5%9B%9B%E7%8E%AF%E7%B4%A0%E7%B1%BB" title="四环素类" class="mw-redirect">四环素类</a>、<a href="/w/%E6%B0%B4%E6%9D%A8%E9%85%B8" title="水杨酸">水杨酸</a>类，或以维生素C作为<a href="/w/%E6%B3%8C%E5%B0%BF%E7%B3%BB%E7%BB%9F" title="泌尿系统">泌尿系统</a>酸<a href="/w/%E5%8C%96%E8%8D%AF" title="化药">化药</a>时。</li>
</ul>
</li>
</ul>
<h2><span class="mw-headline" id=".E9.87.8D.E5.BA.86.E8.8D.AF.E5.8F.8B.E5.88.B6.E8.8D.AF.E6.9C.89.E9.99.90.E8.B4.A3.E4.BB.BB.E5.85.AC.E5.8F.B8.E5.9C.B0.E5.9B.BE">重庆药友制药有限责任公司地图</span></h2>
<p>重庆药友制药有限责任公司地图信息由第三方公司提供。由于技术原因，部分企业位置可能不精确，本地图仅供参考。 本地图显示的位置为重庆市渝北区。</p>
<div id="map_google3_1" style="width: auto; height: 350px; background-color: #cccccc; overflow: hidden;"></div>
<h2><span class="mw-headline" id=".E9.87.8D.E5.BA.86.E8.8D.AF.E5.8F.8B.E5.88.B6.E8.8D.AF.E6.9C.89.E9.99.90.E8.B4.A3.E4.BB.BB.E5.85.AC.E5.8F.B8.E9.99.84.E8.BF.91.E7.9A.84.E5.88.B6.E8.8D.AF.E4.BC.81.E4.B8.9A">重庆药友制药有限责任公司附近的制药企业</span></h2>
<ul>
<li><b><a href="/w/%E9%87%8D%E5%BA%86%E5%8D%8E%E9%82%A6%E5%88%B6%E8%8D%AF%E8%82%A1%E4%BB%BD%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8" title="重庆华邦制药股份有限公司">重庆华邦制药股份有限公司</a></b>
<ul>
<li>企业地址：重庆市渝北区人和星光大道69号</li>
<li>联系电话：023-67889222</li>
<li>电子邮箱：huapont@huapont.cn</li>
</ul>
</li>
<li><b><a href="/w/%E9%87%8D%E5%BA%86%E5%8D%8E%E9%82%A6%E5%88%B6%E8%8D%AF%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8" title="重庆华邦制药有限公司">重庆华邦制药有限公司</a></b>
<ul>
<li>企业地址：重庆市渝北区人和星光大道69号</li>
<li>联系电话：023-67889222</li>
<li>电子邮箱：hr@huapont.cn</li>
</ul>
</li>
<li><b><a href="/w/%E9%87%8D%E5%BA%86%E6%96%B0%E5%8E%9F%E5%85%B4%E8%8D%AF%E4%B8%9A%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8" title="重庆新原兴药业有限公司">重庆新原兴药业有限公司</a></b>
<ul>
<li>企业地址：重庆市江北区兴隆路26号数码大厦B1座7楼</li>
<li>联系电话：023-67727551</li>
<li>电子邮箱：webmaster@cqpharm.cn</li>
</ul>
</li>
<li><b><a href="/w/%E9%87%8D%E5%BA%86%E9%9D%92%E9%98%B3%E8%8D%AF%E4%B8%9A%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8" title="重庆青阳药业有限公司">重庆青阳药业有限公司</a></b>
<ul>
<li>企业地址：重庆市江北区寸滩水口兴药村426号4-2号</li>
<li>联系电话：023-67092651</li>
</ul>
</li>
<li><b><a href="/w/%E8%A5%BF%E5%8D%97%E5%88%B6%E8%8D%AF%E4%B8%80%E5%8E%82" title="西南制药一厂">西南制药一厂</a></b>
<ul>
<li>企业地址：重庆市江北区寸滩水口</li>
<li>联系电话：023-67093051</li>
</ul>
</li>
<li><b><a href="/w/%E9%87%8D%E5%BA%86%E5%B8%82%E5%8C%96%E5%B7%A5%E7%A0%94%E7%A9%B6%E9%99%A2" title="重庆市化工研究院">重庆市化工研究院</a></b>
<ul>
<li>企业地址：重庆市江北区玉带山化工村</li>
<li>联系电话：023-86852598</li>
<li>电子邮箱：chyfzb@ccqci.com</li>
</ul>
</li>
<li><b><a href="/w/%E8%A5%BF%E5%8D%97%E5%90%88%E6%88%90%E6%88%90%E5%88%B6%E8%8D%AF%E8%82%A1%E4%BB%BD%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8" title="西南合成成制药股份有限公司">西南合成成制药股份有限公司</a></b>
<ul>
<li>企业地址：重庆市江北区寸滩水口</li>
</ul>
</li>
<li><b><a href="/w/%E9%87%8D%E5%BA%86%E7%BE%8E%E8%81%94%E5%88%B6%E8%8D%AF%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8" title="重庆美联制药有限公司">重庆美联制药有限公司</a></b>
<ul>
<li>企业地址：重庆市江北区大石坝南桥寺</li>
<li>联系电话：023-67654576</li>
</ul>
</li>
<li><b><a href="/w/%E9%87%8D%E5%BA%86%E5%90%8C%E5%BF%83%E5%88%B6%E8%8D%AF%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8" title="重庆同心制药有限公司">重庆同心制药有限公司</a></b>
<ul>
<li>企业地址：重庆市江北区建东一村69号</li>
<li>联系电话：023-67522673</li>
</ul>
</li>
<li><b><a href="/w/%E9%87%8D%E5%BA%86%E9%99%AA%E9%83%BD%E8%8D%AF%E4%B8%9A%E8%82%A1%E4%BB%BD%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8" title="重庆陪都药业股份有限公司">重庆陪都药业股份有限公司</a></b>
<ul>
<li>企业地址：重庆南坪东路6号南坪商务大厦6楼</li>
<li>联系电话：023-62940362，62940570，62940282</li>
<li>电子邮箱：peidu@cqpeidu.com</li>
</ul>
</li>
</ul>
<h2><span class="mw-headline" id=".E5.8F.82.E7.9C.8B">参看</span></h2>
<ul>
<li><a href="/w/%E9%87%8D%E5%BA%86%E5%B8%82%E5%88%B6%E8%8D%AF%E4%BC%81%E4%B8%9A%E5%88%97%E8%A1%A8" title="重庆市制药企业列表">重庆市制药企业列表</a></li>
</ul>
<h2><span class="mw-headline" id=".E5.88.B6.E8.8D.AF.E4.BC.81.E4.B8.9A.E5.88.86.E5.8C.BA.E5.9F.9F.E6.9F.A5.E8.AF.A2">制药企业分区域查询</span></h2>
<table>
<tr>
<td>
<div style="height: 264px; width: 325px; "><map name="ImageMap_71_616662420" id="ImageMap_71_616662420">
<area href="/w/%E5%8F%B0%E6%B9%BE%E7%9C%81%E5%88%B6%E8%8D%AF%E4%BC%81%E4%B8%9A%E5%88%97%E8%A1%A8" shape="rect" coords="287,214,319,228" alt="台湾省" title="台湾省" />
<area href="/w/%E4%B8%8A%E6%B5%B7%E5%B8%82%E5%88%B6%E8%8D%AF%E4%BC%81%E4%B8%9A%E5%88%97%E8%A1%A8" shape="rect" coords="279,158,311,174" alt="上海市" title="上海市" />
<area href="/w/%E5%90%89%E6%9E%97%E7%9C%81%E5%88%B6%E8%8D%AF%E4%BC%81%E4%B8%9A%E5%88%97%E8%A1%A8" shape="rect" coords="280,61,311,74" alt="吉林省" title="吉林省" />
<area href="/w/%E5%AE%89%E5%BE%BD%E7%9C%81%E5%88%B6%E8%8D%AF%E4%BC%81%E4%B8%9A%E5%88%97%E8%A1%A8" shape="rect" coords="242,158,275,173" alt="安徽省" title="安徽省" />
<area href="/w/%E5%A4%A9%E6%B4%A5%E5%B8%82%E5%88%B6%E8%8D%AF%E4%BC%81%E4%B8%9A%E5%88%97%E8%A1%A8" shape="rect" coords="260,106,292,119" alt="天津市" title="天津市" />
<area href="/w/%E9%9D%92%E6%B5%B7%E7%9C%81%E5%88%B6%E8%8D%AF%E4%BC%81%E4%B8%9A%E5%88%97%E8%A1%A8" shape="rect" coords="107,124,138,139" alt="青海省" title="青海省" />
<area href="/w/%E7%A6%8F%E5%BB%BA%E7%9C%81%E5%88%B6%E8%8D%AF%E4%BC%81%E4%B8%9A%E5%88%97%E8%A1%A8" shape="rect" coords="249,196,282,210" alt="福建省" title="福建省" />
<area href="/w/%E4%BA%91%E5%8D%97%E7%9C%81%E5%88%B6%E8%8D%AF%E4%BC%81%E4%B8%9A%E5%88%97%E8%A1%A8" shape="rect" coords="140,212,173,227" alt="云南省" title="云南省" />
<area href="/w/%E5%B1%B1%E4%B8%9C%E7%9C%81%E5%88%B6%E8%8D%AF%E4%BC%81%E4%B8%9A%E5%88%97%E8%A1%A8" shape="rect" coords="240,121,273,135" alt="山东省" title="山东省" />
<area href="/w/%E5%8C%97%E4%BA%AC%E5%B8%82%E5%88%B6%E8%8D%AF%E4%BC%81%E4%B8%9A%E5%88%97%E8%A1%A8" shape="rect" coords="226,89,260,102" alt="北京市" title="北京市" />
<area href="/w/%E6%B2%B3%E5%8C%97%E7%9C%81%E5%88%B6%E8%8D%AF%E4%BC%81%E4%B8%9A%E5%88%97%E8%A1%A8" shape="rect" coords="222,105,255,118" alt="河北省" title="河北省" />
<area href="/w/%E7%94%98%E8%82%83%E7%9C%81%E5%88%B6%E8%8D%AF%E4%BC%81%E4%B8%9A%E5%88%97%E8%A1%A8" shape="rect" coords="118,97,150,111" alt="甘肃省" title="甘肃省" />
<area href="/w/%E5%B1%B1%E8%A5%BF%E7%9C%81%E5%88%B6%E8%8D%AF%E4%BC%81%E4%B8%9A%E5%88%97%E8%A1%A8" shape="rect" coords="203,120,235,134" alt="山西省" title="山西省" />
<area href="/w/%E5%86%85%E8%92%99%E5%8F%A4%E8%87%AA%E6%B2%BB%E5%8C%BA%E5%88%B6%E8%8D%AF%E4%BC%81%E4%B8%9A%E5%88%97%E8%A1%A8" shape="rect" coords="159,93,209,106" alt="内蒙古自治区" title="内蒙古自治区" />
<area href="/w/%E6%B9%96%E5%8D%97%E7%9C%81%E5%88%B6%E8%8D%AF%E4%BC%81%E4%B8%9A%E5%88%97%E8%A1%A8" shape="rect" coords="206,195,240,208" alt="湖南省" title="湖南省" />
<area href="/w/%E6%B2%B3%E5%8D%97%E7%9C%81%E5%88%B6%E8%8D%AF%E4%BC%81%E4%B8%9A%E5%88%97%E8%A1%A8" shape="rect" coords="215,139,246,154" alt="河南省" title="河南省" />
<area href="/w/%E5%B9%BF%E4%B8%9C%E7%9C%81%E5%88%B6%E8%8D%AF%E4%BC%81%E4%B8%9A%E5%88%97%E8%A1%A8" shape="rect" coords="219,216,250,232" alt="广东省" title="广东省" />
<area href="/w/%E5%AE%81%E5%A4%8F%E5%9B%9E%E6%97%8F%E8%87%AA%E6%B2%BB%E5%8C%BA%E5%88%B6%E8%8D%AF%E4%BC%81%E4%B8%9A%E5%88%97%E8%A1%A8" shape="rect" coords="152,125,185,141" alt="宁夏回族自治区" title="宁夏回族自治区" />
<area href="/w/%E6%96%B0%E7%96%86%E7%BB%B4%E5%90%BE%E5%B0%94%E8%87%AA%E6%B2%BB%E5%8C%BA%E5%88%B6%E8%8D%AF%E4%BC%81%E4%B8%9A%E5%88%97%E8%A1%A8" shape="rect" coords="42,84,77,99" alt="新疆维吾尔自治区" title="新疆维吾尔自治区" />
<area href="/w/%E9%87%8D%E5%BA%86%E5%B8%82%E5%88%B6%E8%8D%AF%E4%BC%81%E4%B8%9A%E5%88%97%E8%A1%A8" shape="rect" coords="166,177,198,191" alt="重庆市" title="重庆市" />
<area href="/w/%E6%B5%99%E6%B1%9F%E7%9C%81%E5%88%B6%E8%8D%AF%E4%BC%81%E4%B8%9A%E5%88%97%E8%A1%A8" shape="rect" coords="269,178,303,192" alt="浙江省" title="浙江省" />
<area href="/w/%E5%9B%9B%E5%B7%9D%E7%9C%81%E5%88%B6%E8%8D%AF%E4%BC%81%E4%B8%9A%E5%88%97%E8%A1%A8" shape="rect" coords="138,159,172,173" alt="四川省" title="四川省" />
<area href="/w/%E9%BB%91%E9%BE%99%E6%B1%9F%E7%9C%81%E5%88%B6%E8%8D%AF%E4%BC%81%E4%B8%9A%E5%88%97%E8%A1%A8" shape="rect" coords="272,28,322,43" alt="黑龙江省" title="黑龙江省" />
<area href="/w/%E9%99%95%E8%A5%BF%E7%9C%81%E5%88%B6%E8%8D%AF%E4%BC%81%E4%B8%9A%E5%88%97%E8%A1%A8" shape="rect" coords="183,140,215,154" alt="陕西省" title="陕西省" />
<area href="/w/%E6%B1%9F%E8%A5%BF%E7%9C%81%E5%88%B6%E8%8D%AF%E4%BC%81%E4%B8%9A%E5%88%97%E8%A1%A8" shape="rect" coords="235,179,266,192" alt="江西省" title="江西省" />
<area href="/w/%E6%B5%B7%E5%8D%97%E7%9C%81%E5%88%B6%E8%8D%AF%E4%BC%81%E4%B8%9A%E5%88%97%E8%A1%A8" shape="rect" coords="172,243,207,257" alt="海南省" title="海南省" />
<area href="/w/%E8%B4%B5%E5%B7%9E%E7%9C%81%E5%88%B6%E8%8D%AF%E4%BC%81%E4%B8%9A%E5%88%97%E8%A1%A8" shape="rect" coords="173,194,204,209" alt="贵州省" title="贵州省" />
<area href="/w/%E6%B1%9F%E8%8B%8F%E7%9C%81%E5%88%B6%E8%8D%AF%E4%BC%81%E4%B8%9A%E5%88%97%E8%A1%A8" shape="rect" coords="253,140,284,154" alt="江苏省" title="江苏省" />
<area href="/w/%E8%BE%BD%E5%AE%81%E7%9C%81%E5%88%B6%E8%8D%AF%E4%BC%81%E4%B8%9A%E5%88%97%E8%A1%A8" shape="rect" coords="261,83,293,96" alt="辽宁省" title="辽宁省" />
<area href="/w/%E6%B9%96%E5%8C%97%E7%9C%81%E5%88%B6%E8%8D%AF%E4%BC%81%E4%B8%9A%E5%88%97%E8%A1%A8" shape="rect" coords="209,162,240,177" alt="湖北省" title="湖北省" />
<area href="/w/%E8%A5%BF%E8%97%8F%E8%87%AA%E6%B2%BB%E5%8C%BA%E5%88%B6%E8%8D%AF%E4%BC%81%E4%B8%9A%E5%88%97%E8%A1%A8" shape="rect" coords="51,156,82,171" alt="西藏自治区" title="西藏自治区" />
<area href="/w/%E5%B9%BF%E8%A5%BF%E5%A3%AE%E6%97%8F%E8%87%AA%E6%B2%BB%E5%8C%BA%E5%88%B6%E8%8D%AF%E4%BC%81%E4%B8%9A%E5%88%97%E8%A1%A8" shape="rect" coords="183,216,217,231" alt="广西壮族自治区" title="广西壮族自治区" />
<area href="/w/%E6%BE%B3%E9%97%A8%E7%89%B9%E5%88%AB%E8%A1%8C%E6%94%BF%E5%8C%BA%E5%88%B6%E8%8D%AF%E4%BC%81%E4%B8%9A%E5%88%97%E8%A1%A8" shape="rect" coords="219,234,250,247" alt="澳门特别行政区" title="澳门特别行政区" />
<area href="/w/%E9%A6%99%E6%B8%AF%E7%89%B9%E5%88%AB%E8%A1%8C%E6%94%BF%E5%8C%BA%E5%88%B6%E8%8D%AF%E4%BC%81%E4%B8%9A%E5%88%97%E8%A1%A8" shape="rect" coords="252,225,284,238" alt="香港特别行政区" title="香港特别行政区" /></map><img alt="按省份查询" src="http://p.ayxbk.com/images/2/21/China_map.gif" width="325" height="264" usemap="#ImageMap_71_616662420" />
<div style="margin-left: 305px; margin-top: -20px; text-align: left;"><a href="/w/%E6%96%87%E4%BB%B6:China_map.gif" title="关于这幅图像"><img alt="关于这幅图像" src="/extensions/ImageMap/desc-20.png" style="border: none;" /></a></div>
</div>
</td>
<td>
<p>制药企业名录列表可以按省份或城市分区域查看，详细参看<a href="/w/%E5%85%A8%E5%9B%BD%E5%88%B6%E8%8D%AF%E4%BC%81%E4%B8%9A%E5%88%97%E8%A1%A8" title="全国制药企业列表">全国制药企业列表</a>。</p>
<p><a href="/w/%E5%B9%BF%E4%B8%9C%E7%9C%81%E5%88%B6%E8%8D%AF%E4%BC%81%E4%B8%9A%E5%88%97%E8%A1%A8" title="广东省制药企业列表">广东省</a> | <a href="/w/%E6%B1%9F%E8%8B%8F%E7%9C%81%E5%88%B6%E8%8D%AF%E4%BC%81%E4%B8%9A%E5%88%97%E8%A1%A8" title="江苏省制药企业列表">江苏省</a> | <a href="/w/%E5%8C%97%E4%BA%AC%E5%B8%82%E5%88%B6%E8%8D%AF%E4%BC%81%E4%B8%9A%E5%88%97%E8%A1%A8" title="北京市制药企业列表">北京市</a> | <a href="/w/%E6%B5%99%E6%B1%9F%E7%9C%81%E5%88%B6%E8%8D%AF%E4%BC%81%E4%B8%9A%E5%88%97%E8%A1%A8" title="浙江省制药企业列表">浙江省</a> | <a href="/w/%E5%B1%B1%E4%B8%9C%E7%9C%81%E5%88%B6%E8%8D%AF%E4%BC%81%E4%B8%9A%E5%88%97%E8%A1%A8" title="山东省制药企业列表">山东省</a> | <a href="/w/%E5%90%89%E6%9E%97%E7%9C%81%E5%88%B6%E8%8D%AF%E4%BC%81%E4%B8%9A%E5%88%97%E8%A1%A8" title="吉林省制药企业列表">吉林省</a> | <a href="/w/%E6%B2%B3%E5%8C%97%E7%9C%81%E5%88%B6%E8%8D%AF%E4%BC%81%E4%B8%9A%E5%88%97%E8%A1%A8" title="河北省制药企业列表">河北省</a> | <a href="/w/%E5%9B%9B%E5%B7%9D%E7%9C%81%E5%88%B6%E8%8D%AF%E4%BC%81%E4%B8%9A%E5%88%97%E8%A1%A8" title="四川省制药企业列表">四川省</a> | <a href="/w/%E6%B2%B3%E5%8D%97%E7%9C%81%E5%88%B6%E8%8D%AF%E4%BC%81%E4%B8%9A%E5%88%97%E8%A1%A8" title="河南省制药企业列表">河南省</a> | <a href="/w/%E8%BE%BD%E5%AE%81%E7%9C%81%E5%88%B6%E8%8D%AF%E4%BC%81%E4%B8%9A%E5%88%97%E8%A1%A8" title="辽宁省制药企业列表">辽宁省</a> | <a href="/w/%E4%B8%8A%E6%B5%B7%E5%B8%82%E5%88%B6%E8%8D%AF%E4%BC%81%E4%B8%9A%E5%88%97%E8%A1%A8" title="上海市制药企业列表">上海市</a> | <a href="/w/%E6%B9%96%E5%8C%97%E7%9C%81%E5%88%B6%E8%8D%AF%E4%BC%81%E4%B8%9A%E5%88%97%E8%A1%A8" title="湖北省制药企业列表">湖北省</a> | <a href="/w/%E9%99%95%E8%A5%BF%E7%9C%81%E5%88%B6%E8%8D%AF%E4%BC%81%E4%B8%9A%E5%88%97%E8%A1%A8" title="陕西省制药企业列表">陕西省</a> | <a href="/w/%E9%BB%91%E9%BE%99%E6%B1%9F%E7%9C%81%E5%88%B6%E8%8D%AF%E4%BC%81%E4%B8%9A%E5%88%97%E8%A1%A8" title="黑龙江省制药企业列表">黑龙江省</a> | <a href="/w/%E5%B9%BF%E8%A5%BF%E5%A3%AE%E6%97%8F%E8%87%AA%E6%B2%BB%E5%8C%BA%E5%88%B6%E8%8D%AF%E4%BC%81%E4%B8%9A%E5%88%97%E8%A1%A8" title="广西壮族自治区制药企业列表">广西壮族自治区</a> | <a href="/w/%E6%B1%9F%E8%A5%BF%E7%9C%81%E5%88%B6%E8%8D%AF%E4%BC%81%E4%B8%9A%E5%88%97%E8%A1%A8" title="江西省制药企业列表">江西省</a> | <a href="/w/%E4%BA%91%E5%8D%97%E7%9C%81%E5%88%B6%E8%8D%AF%E4%BC%81%E4%B8%9A%E5%88%97%E8%A1%A8" title="云南省制药企业列表">云南省</a> | <a href="/w/%E5%B1%B1%E8%A5%BF%E7%9C%81%E5%88%B6%E8%8D%AF%E4%BC%81%E4%B8%9A%E5%88%97%E8%A1%A8" title="山西省制药企业列表">山西省</a> | <a href="/w/%E5%AE%89%E5%BE%BD%E7%9C%81%E5%88%B6%E8%8D%AF%E4%BC%81%E4%B8%9A%E5%88%97%E8%A1%A8" title="安徽省制药企业列表">安徽省</a> | <a href="/w/%E6%B9%96%E5%8D%97%E7%9C%81%E5%88%B6%E8%8D%AF%E4%BC%81%E4%B8%9A%E5%88%97%E8%A1%A8" title="湖南省制药企业列表">湖南省</a> | <a href="/w/%E8%B4%B5%E5%B7%9E%E7%9C%81%E5%88%B6%E8%8D%AF%E4%BC%81%E4%B8%9A%E5%88%97%E8%A1%A8" title="贵州省制药企业列表">贵州省</a> | <a href="/w/%E5%A4%A9%E6%B4%A5%E5%B8%82%E5%88%B6%E8%8D%AF%E4%BC%81%E4%B8%9A%E5%88%97%E8%A1%A8" title="天津市制药企业列表">天津市</a> | <a href="/w/%E9%87%8D%E5%BA%86%E5%B8%82%E5%88%B6%E8%8D%AF%E4%BC%81%E4%B8%9A%E5%88%97%E8%A1%A8" title="重庆市制药企业列表">重庆市</a> | <a href="/w/%E6%B5%B7%E5%8D%97%E7%9C%81%E5%88%B6%E8%8D%AF%E4%BC%81%E4%B8%9A%E5%88%97%E8%A1%A8" title="海南省制药企业列表">海南省</a> | <a href="/w/%E7%A6%8F%E5%BB%BA%E7%9C%81%E5%88%B6%E8%8D%AF%E4%BC%81%E4%B8%9A%E5%88%97%E8%A1%A8" title="福建省制药企业列表">福建省</a> | <a href="/w/%E5%86%85%E8%92%99%E5%8F%A4%E8%87%AA%E6%B2%BB%E5%8C%BA%E5%88%B6%E8%8D%AF%E4%BC%81%E4%B8%9A%E5%88%97%E8%A1%A8" title="内蒙古自治区制药企业列表">内蒙古自治区</a> | <a href="/w/%E7%94%98%E8%82%83%E7%9C%81%E5%88%B6%E8%8D%AF%E4%BC%81%E4%B8%9A%E5%88%97%E8%A1%A8" title="甘肃省制药企业列表">甘肃省</a> | <a href="/w/%E6%96%B0%E7%96%86%E7%BB%B4%E5%90%BE%E5%B0%94%E8%87%AA%E6%B2%BB%E5%8C%BA%E5%88%B6%E8%8D%AF%E4%BC%81%E4%B8%9A%E5%88%97%E8%A1%A8" title="新疆维吾尔自治区制药企业列表">新疆维吾尔自治区</a> | <a href="/w/%E9%9D%92%E6%B5%B7%E7%9C%81%E5%88%B6%E8%8D%AF%E4%BC%81%E4%B8%9A%E5%88%97%E8%A1%A8" title="青海省制药企业列表">青海省</a> | <a href="/w/%E8%A5%BF%E8%97%8F%E8%87%AA%E6%B2%BB%E5%8C%BA%E5%88%B6%E8%8D%AF%E4%BC%81%E4%B8%9A%E5%88%97%E8%A1%A8" title="西藏自治区制药企业列表">西藏自治区</a> | <a href="/w/%E5%AE%81%E5%A4%8F%E5%9B%9E%E6%97%8F%E8%87%AA%E6%B2%BB%E5%8C%BA%E5%88%B6%E8%8D%AF%E4%BC%81%E4%B8%9A%E5%88%97%E8%A1%A8" title="宁夏回族自治区制药企业列表">宁夏回族自治区</a> | <a href="/w/%E5%8F%B0%E6%B9%BE%E7%9C%81%E5%88%B6%E8%8D%AF%E4%BC%81%E4%B8%9A%E5%88%97%E8%A1%A8" title="台湾省制药企业列表">台湾省</a> | <a href="/w/%E9%A6%99%E6%B8%AF%E7%89%B9%E5%88%AB%E8%A1%8C%E6%94%BF%E5%8C%BA%E5%88%B6%E8%8D%AF%E4%BC%81%E4%B8%9A%E5%88%97%E8%A1%A8" title="香港特别行政区制药企业列表">香港特别行政区</a> | <a href="/w/%E6%BE%B3%E9%97%A8%E7%89%B9%E5%88%AB%E8%A1%8C%E6%94%BF%E5%8C%BA%E5%88%B6%E8%8D%AF%E4%BC%81%E4%B8%9A%E5%88%97%E8%A1%A8" title="澳门特别行政区制药企业列表">澳门特别行政区</a></p>
</td>
</tr>
</table>
<p></p>

<!-- 
NewPP limit report
Preprocessor node count: 1918/1000000
Post-expand include size: 9327/2097152 bytes
Template argument size: 1628/2097152 bytes
Expensive parser function count: 0/100
-->

<!-- Saved in parser cache with key ahospital:pcache:idhash:178470-0!1!0!!zh-hans!2!edit=0 and timestamp 20181019021154 -->
<div id="fromlink">出自A+医学百科 “重庆药友制药有限责任公司”条目 <a href="http://www.a-hospital.com/w/%E9%87%8D%E5%BA%86%E8%8D%AF%E5%8F%8B%E5%88%B6%E8%8D%AF%E6%9C%89%E9%99%90%E8%B4%A3%E4%BB%BB%E5%85%AC%E5%8F%B8" class="external free" target="_blank">http://www.a-hospital.com/w/%E9%87%8D%E5%BA%86%E8%8D%AF%E5%8F%8B%E5%88%B6%E8%8D%AF%E6%9C%89%E9%99%90%E8%B4%A3%E4%BB%BB%E5%85%AC%E5%8F%B8</a> 转载请保留此链接</div><div class="bdsharebuttonbox"><a href="#" class="bds_qzone" data-cmd="qzone" title="分享到QQ空间"></a><a href="#" class="bds_weixin" data-cmd="weixin" title="分享到微信"></a><a href="#" class="bds_tqq" data-cmd="tqq" title="分享到腾讯微博"></a><a href="#" class="bds_tsina" data-cmd="tsina" title="分享到新浪微博"></a><a href="#" class="bds_fbook" data-cmd="fbook" title="分享到Facebook"></a><a href="#" class="bds_copy" data-cmd="copy" title="分享到复制网址"></a><a href="#" class="bds_more" data-cmd="more"></a><a href="#" class="bds_count" data-cmd="count"></a></div>
<table class="msg-table">

<tr style="background-color:rgb(206, 223, 242);">
<td><b>关于“<strong class="selflink">重庆药友制药有限责任公司</strong>”的留言：</b>
</td><td align="right"><img alt="Feed-icon.png" src="http://p.ayxbk.com/images/f/f4/Feed-icon.png" width="12" height="12" /> <a href="http://www.a-hospital.com/index.php?title=%E8%AE%A8%E8%AE%BA:%E9%87%8D%E5%BA%86%E8%8D%AF%E5%8F%8B%E5%88%B6%E8%8D%AF%E6%9C%89%E9%99%90%E8%B4%A3%E4%BB%BB%E5%85%AC%E5%8F%B8&amp;feed=rss&amp;action=history" class="external text" target="_blank">订阅讨论RSS</a>
</td></tr>
<tr>
<td colspan="2" style="background-color:#ffffff;">
<p>目前暂无留言
</p>
</td></tr>
<tr>
<td colspan="2"><a href="http://www.a-hospital.com/index.php?title=%E8%AE%A8%E8%AE%BA:%E9%87%8D%E5%BA%86%E8%8D%AF%E5%8F%8B%E5%88%B6%E8%8D%AF%E6%9C%89%E9%99%90%E8%B4%A3%E4%BB%BB%E5%85%AC%E5%8F%B8&amp;action=edit&amp;section=new&amp;preload=%E6%A8%A1%E6%9D%BF%3A%E7%AD%BE%E5%90%8D&amp;editintro=%E6%A8%A1%E6%9D%BF%3A%E7%AD%BE%E5%90%8D%E8%AF%B4%E6%98%8E&amp;preloadtitle=%E7%BB%99%E9%87%8D%E5%BA%86%E8%8D%AF%E5%8F%8B%E5%88%B6%E8%8D%AF%E6%9C%89%E9%99%90%E8%B4%A3%E4%BB%BB%E5%85%AC%E5%8F%B8%E6%9D%A1%E7%9B%AE%E7%9A%84%E7%95%99%E8%A8%80" class="external text" target="_blank">添加留言</a>
</td></tr></table>
<h2> <span class="mw-headline" id=".E6.9B.B4.E5.A4.9A.E5.8C.BB.E5.AD.A6.E7.99.BE.E7.A7.91.E6.9D.A1.E7.9B.AE">更多医学百科条目</span></h2>
				<!-- /bodytext -->
								<!-- catlinks -->
				<div id='catlinks' class='catlinks'><div id="mw-normal-catlinks"><a href="/w/%E7%89%B9%E6%AE%8A:%E9%A1%B5%E9%9D%A2%E5%88%86%E7%B1%BB" title="特殊:页面分类">4个分类</a>: <span dir='ltr'><a href="/w/%E5%88%86%E7%B1%BB:%E5%88%B6%E8%8D%AF%E4%BC%81%E4%B8%9A" title="分类:制药企业">制药企业</a></span> | <span dir='ltr'><a href="/w/%E5%88%86%E7%B1%BB:%E4%BC%81%E4%B8%9A" title="分类:企业">企业</a></span> | <span dir='ltr'><a href="/w/%E5%88%86%E7%B1%BB:%E9%87%8D%E5%BA%86%E5%B8%82%E5%88%B6%E8%8D%AF%E4%BC%81%E4%B8%9A" title="分类:重庆市制药企业">重庆市制药企业</a></span> | <span dir='ltr'><a href="/w/%E5%88%86%E7%B1%BB:%E9%87%8D%E5%BA%86%E5%B8%82" title="分类:重庆市">重庆市</a></span></div></div>				<!-- /catlinks -->
												<div class="visualClear"></div>
			</div>
			<!-- /bodyContent -->
		</div>
		<!-- /content -->
		<!-- header -->
		<div id="mw-head" class="noprint">
			
<!-- 0 -->
<div id="p-personal" class="">
	<h5>个人工具</h5>
	<ul>
					<li  id="pt-login"><a href="/index.php?title=%E7%89%B9%E6%AE%8A:%E7%94%A8%E6%88%B7%E7%99%BB%E5%BD%95&amp;returnto=%E9%87%8D%E5%BA%86%E8%8D%AF%E5%8F%8B%E5%88%B6%E8%8D%AF%E6%9C%89%E9%99%90%E8%B4%A3%E4%BB%BB%E5%85%AC%E5%8F%B8" title="我们鼓励您登录，但这并不是必须的 [o]" accesskey="o" rel="nofollow">登录／创建账户</a></li>
			</ul>
</div>

<!-- /0 -->
			<div id="left-navigation">
				
<!-- 0 -->
<div id="p-namespaces" class="vectorTabs">
	<h5>名字空间</h5>
	<ul>
					<li  id="ca-nstab-main" class="selected"><a href="/w/%E9%87%8D%E5%BA%86%E8%8D%AF%E5%8F%8B%E5%88%B6%E8%8D%AF%E6%9C%89%E9%99%90%E8%B4%A3%E4%BB%BB%E5%85%AC%E5%8F%B8" rel="nofollow"  title="查看页面内容 [c]" accesskey="c"><span>页面</span></a></li>
					<li  id="ca-talk" class="new"><a href="/index.php?title=%E8%AE%A8%E8%AE%BA:%E9%87%8D%E5%BA%86%E8%8D%AF%E5%8F%8B%E5%88%B6%E8%8D%AF%E6%9C%89%E9%99%90%E8%B4%A3%E4%BB%BB%E5%85%AC%E5%8F%B8&amp;action=edit&amp;redlink=1" rel="nofollow"  title="关于页面正文的讨论 [t]" accesskey="t"><span>讨论</span></a></li>
			</ul>
</div>

<!-- /0 -->

<!-- 1 -->

<!-- /1 -->
			</div>
			<div id="right-navigation">
				
<!-- 0 -->
<div id="p-views" class="vectorTabs">
	<h5>查看</h5>
	<ul>
					<li id="ca-view" class="selected"><a href="/w/%E9%87%8D%E5%BA%86%E8%8D%AF%E5%8F%8B%E5%88%B6%E8%8D%AF%E6%9C%89%E9%99%90%E8%B4%A3%E4%BB%BB%E5%85%AC%E5%8F%B8" rel="nofollow"><span>阅读</span></a></li>
					<li id="ca-trans"><a href="http://cht.a-hospital.com/w/%E9%87%8D%E5%BA%86%E8%8D%AF%E5%8F%8B%E5%88%B6%E8%8D%AF%E6%9C%89%E9%99%90%E8%B4%A3%E4%BB%BB%E5%85%AC%E5%8F%B8" rel="alternate" hreflang="zh-Hant"><span>繁体/正体</span></a></li>
					<li id="ca-viewsource"><a href="/index.php?title=%E9%87%8D%E5%BA%86%E8%8D%AF%E5%8F%8B%E5%88%B6%E8%8D%AF%E6%9C%89%E9%99%90%E8%B4%A3%E4%BB%BB%E5%85%AC%E5%8F%B8&amp;action=edit" rel="nofollow" title="修正、补充或整理本条目。 [e]" accesskey="e"><span>编辑修改</span></a></li>
					<li id="ca-history" class="collapsible "><a href="/index.php?title=%E9%87%8D%E5%BA%86%E8%8D%AF%E5%8F%8B%E5%88%B6%E8%8D%AF%E6%9C%89%E9%99%90%E8%B4%A3%E4%BB%BB%E5%85%AC%E5%8F%B8&amp;action=history" rel="nofollow" title="此页面的早前修订版本 [h]" accesskey="h"><span>修订历史</span></a></li>
			</ul>
</div>

<!-- /0 -->

<!-- 1 -->
<div id="p-cactions" class="vectorMenu emptyPortlet">
	<h5><span>动作</span><a href="#"></a></h5>
	<div class="menu">
		<ul>
					</ul>
	</div>
</div>

<!-- /1 -->

<!-- 2 -->
<div id="p-search">
	<h5><label for="searchInput">搜索</label></h5>
	<form action="/index.php" id="searchform">
		<input type='hidden' name="title" value="特殊:搜索"/>
		<div id="simpleSearch">
							<input id="searchInput"  onfocus="if (this.value == '搜索') {this.value = '';}" onblur="if (this.value == '') {this.value = '搜索';}" name="search" type="text"  title="搜索该网站 [f]" accesskey="f"  value="搜索"  />
						<button id="searchButton" type='submit' name='button'  title="搜索该文字的页面">&nbsp;</button>
		</div>
	</form>
</div>

<!-- /2 -->
			</div>
		</div>
		<!-- /header -->
		<!-- panel -->
			<div id="mw-panel" class="noprint">
				<!-- logo -->
					<div id="p-logo"><a style="background-image: url(http://s.ayxbk.com/common/images/logo.png);" href="/w/%E9%A6%96%E9%A1%B5"  title="访问首页"></a></div>
				<!-- /logo -->
				  
<div class="portal" id='p-navigation'>
	<h5>导航</h5>
	<div class="body">
				<ul>
					<li><a href="/w/%E9%A6%96%E9%A1%B5" title="访问首页 [z]" accesskey="z">首页</a></li>
					<li><a href="/w/%E5%A4%A7%E5%8C%BB%E7%B2%BE%E8%AF%9A">大医精诚</a></li>
					<li><a href="/w/%E4%BA%BA%E4%BD%93%E7%A9%B4%E4%BD%8D%E5%9B%BE">人体穴位图</a></li>
					<li><a href="/w/%E4%B8%AD%E8%8D%AF%E5%9B%BE%E5%85%B8">中药图典</a></li>
					<li><a href="/w/%E5%85%A8%E5%9B%BD%E5%8C%BB%E9%99%A2%E5%88%97%E8%A1%A8">全国医院列表</a></li>
					<li><a href="/w/%E5%8C%BB%E5%AD%A6%E7%94%B5%E5%AD%90%E4%B9%A6">医学电子书</a></li>
					<li><a href="/w/%E8%8D%AF%E5%93%81">药品百科</a></li>
					<li><a href="/w/%E4%B8%AD%E5%8C%BB">中医百科</a></li>
					<li><a href="/w/%E7%96%BE%E7%97%85%E8%AF%8A%E6%96%AD">疾病诊断</a></li>
					<li><a href="/w/%E6%80%A5%E6%95%91%E5%B8%B8%E8%AF%86">急救常识</a></li>
					<li><a href="/w/%E7%96%BE%E7%97%85">疾病查询</a></li>
					<li><a href="/w/%E4%B8%AD%E8%8D%AF">中药百科</a></li>
					<li><a href="/w/%E4%B8%AD%E8%8D%AF%E6%96%B9%E5%89%82">中医方剂大全</a></li>
					<li><a href="/w/%E6%80%8E%E6%A0%B7%E7%9C%8B%E5%8C%96%E9%AA%8C%E5%8D%95">怎样看化验单</a></li>
					<li><a href="/w/%E5%85%A8%E5%9B%BD%E5%88%B6%E8%8D%AF%E4%BC%81%E4%B8%9A%E5%88%97%E8%A1%A8">全国制药企业</a></li>
					<li><a href="/w/%E5%85%A8%E5%9B%BD%E5%8C%BB%E7%A7%91%E9%99%A2%E6%A0%A1%E5%88%97%E8%A1%A8">医科院校大全</a></li>
					<li><a href="/w/%E5%8C%BB%E4%BA%8B%E6%BC%AB%E8%B0%88">医事漫谈</a></li>
					<li><a href="/w/%E5%8C%BB%E5%AD%A6%E4%B8%8B%E8%BD%BD">医学下载</a></li>
					<li><a href="/w/%E5%8C%BB%E5%AD%A6%E8%A7%86%E9%A2%91">医学视频</a></li>
				</ul>
			</div>
</div>
  
<div class="portal" id='p-.E6.8E.A8.E8.8D.90.E5.B7.A5.E5.85.B7'>
	<h5>推荐工具</h5>
	<div class="body">
				<ul>
					<li><a href="http://www.adaohang.com/health.html">医学网站大全</a></li>
					<li><a href="http://www.mcd8.com/">医学词典</a></li>
					<li><a href="http://blog.a-hospital.com/">医学资讯博客</a></li>
				</ul>
			</div>
</div>
  
<div class="portal" id='p-.E5.8A.9F.E8.83.BD.E8.8F.9C.E5.8D.95'>
	<h5>功能菜单</h5>
	<div class="body">
				<ul>
					<li><a href="/w/A%2B%E5%8C%BB%E5%AD%A6%E7%99%BE%E7%A7%91:%E6%B7%BB%E5%8A%A0%E6%9D%A1%E7%9B%AE" rel="nofollow">添加页面</a></li>
					<li><a href="/w/A%2B%E5%8C%BB%E5%AD%A6%E7%99%BE%E7%A7%91:%E6%8B%9B%E5%8B%9F%E7%99%BE%E7%A7%91%E5%BF%97%E6%84%BF%E8%80%85" rel="nofollow">志愿者招募中</a></li>
					<li><a href="/w/%E7%89%B9%E6%AE%8A:ContributionScores" rel="nofollow">积分排名</a></li>
					<li><a href="/w/A%2B%E5%8C%BB%E5%AD%A6%E7%99%BE%E7%A7%91:%E5%85%B3%E4%BA%8E%E5%B9%BF%E5%91%8A" rel="nofollow">关于广告</a></li>
					<li><a href="/w/A%2B%E5%8C%BB%E5%AD%A6%E7%99%BE%E7%A7%91:%E7%BD%91%E7%AB%99%E4%BA%8B%E5%8A%A1">网站事务</a></li>
					<li><a href="/w/%E7%89%B9%E6%AE%8A:%E6%9C%80%E8%BF%91%E6%9B%B4%E6%94%B9" title="列出该网站的最近修改 [r]" accesskey="r">最近更改</a></li>
				</ul>
			</div>
</div>
<div class="portal" id="p-tb">
	<h5>工具箱</h5>
	<div class="body">
		<ul>
					<li id="t-whatlinkshere"><a href="/w/%E7%89%B9%E6%AE%8A:%E9%93%BE%E5%85%A5%E9%A1%B5%E9%9D%A2/%E9%87%8D%E5%BA%86%E8%8D%AF%E5%8F%8B%E5%88%B6%E8%8D%AF%E6%9C%89%E9%99%90%E8%B4%A3%E4%BB%BB%E5%85%AC%E5%8F%B8" title="列出所有与此页相链的页面 [j]" accesskey="j">链入页面</a></li>
						<li id="t-recentchangeslinked"><a href="/w/%E7%89%B9%E6%AE%8A:%E9%93%BE%E5%87%BA%E6%9B%B4%E6%94%B9/%E9%87%8D%E5%BA%86%E8%8D%AF%E5%8F%8B%E5%88%B6%E8%8D%AF%E6%9C%89%E9%99%90%E8%B4%A3%E4%BB%BB%E5%85%AC%E5%8F%B8" title="从此页链出的所有页面的更改 [k]" accesskey="k">链出更改</a></li>
																																												<li id="t-specialpages"><a href="/w/%E7%89%B9%E6%AE%8A:%E7%89%B9%E6%AE%8A%E9%A1%B5%E9%9D%A2" title="所有特殊页面列表 [q]" accesskey="q">所有特殊页面</a></li>
									<li id="t-print"><a href="/index.php?title=%E9%87%8D%E5%BA%86%E8%8D%AF%E5%8F%8B%E5%88%B6%E8%8D%AF%E6%9C%89%E9%99%90%E8%B4%A3%E4%BB%BB%E5%85%AC%E5%8F%B8&amp;printable=yes" rel="nofollow" title="这个页面的可打印版本 [p]" accesskey="p">可打印版</a></li>
						</ul>
	</div>
</div>
			</div>
		<!-- /panel -->
		<!-- footer -->
		<div id="footer">
											<ul id="footer-info">
																	<li id="footer-info-credits">此页由A+医学百科用户<a rel="nofollow" href="/w/%E7%94%A8%E6%88%B7:%E8%A1%8C%E5%8C%BB" title="用户:行医">行医</a>于2012年4月27日 (星期五) 06:57最后更改。 </li>
																							<li id="footer-info-copyright"><br />本站内容由网友添加和整理，仅供学习和参考。站内信息不一定准确、全面或最新。<br />
网站内容不应成为诊断或治疗疾病的最终依据。A+医学百科提醒网友，如有身体不适，请及时就医。<br />
本站的全部文本内容在<a rel="nofollow" href="/w/A%2B%E5%8C%BB%E5%AD%A6%E7%99%BE%E7%A7%91:%E7%89%88%E6%9D%83" title="A+医学百科:版权">知识共享 署名-相同方式共享 3.0协议</a>之条款下提供。<br /></li>
															</ul>
															<ul id="footer-places">
																	<li id="footer-places-privacy"><a rel="nofollow" href="/w/A%2B%E5%8C%BB%E5%AD%A6%E7%99%BE%E7%A7%91:%E9%9A%90%E7%A7%81%E6%94%BF%E7%AD%96" title="A+医学百科:隐私政策">隐私政策</a></li>
																							<li id="footer-places-about"><a rel="nofollow" href="/w/A%2B%E5%8C%BB%E5%AD%A6%E7%99%BE%E7%A7%91:%E5%85%B3%E4%BA%8E" title="A+医学百科:关于">关于A+医学百科</a></li>
																							<li id="footer-places-disclaimer"><a rel="nofollow" href="/w/A%2B%E5%8C%BB%E5%AD%A6%E7%99%BE%E7%A7%91:%E5%85%8D%E8%B4%A3%E5%A3%B0%E6%98%8E" title="A+医学百科:免责声明">免责声明</a></li>
															</ul>
										<div style="clear:both"></div>
		</div>
		<!-- /footer -->
						<script>window._bd_share_config={"common":{"bdSign":"off","bdSnsKey":{},"bdText":"","bdMini":"2","bdMiniList":false,"bdPic":"","bdStyle":"0","bdSize":"32"},"share":{},"image":{"viewList":["qzone","weixin","tqq","tsina","fbook"],"viewText":"分享到：","viewSize":"16"},"selectShare":{"bdContainerClass":null,"bdSelectMiniList":["qzone","weixin","tqq","tsina","fbook"]}};with(document)0[(getElementsByTagName('head')[0]||body).appendChild(createElement('script')).src='http://bdimg.share.baidu.com/static/api/js/share.js?v=89860593.js?cdnversion='+~(-new Date()/36e5)];</script>
				
<script>
var skin="vector",
stylepath="http://s.ayxbk.com",
wgUrlProtocols="http\\:\\/\\/|https\\:\\/\\/|ftp\\:\\/\\/|irc\\:\\/\\/|mailto\\:",
wgArticlePath="/w/$1",
wgScriptPath="",
wgScriptExtension=".php",
wgScript="/index.php",
wgVariantArticlePath=false,
wgActionPaths={},
wgServer="http://www.a-hospital.com",
wgCanonicalNamespace="",
wgCanonicalSpecialPageName=false,
wgNamespaceNumber=0,
wgPageName="重庆药友制药有限责任公司",
wgTitle="重庆药友制药有限责任公司",
wgAction="view",
wgArticleId=178470,
wgIsArticle=true,
wgUserName=null,
wgUserGroups=null,
wgUserLanguage="zh-hans",
wgContentLanguage="zh-hans",
wgBreakFrames=true,
wgCurRevisionId=399483,
wgVersion="1.16.0",
wgEnableAPI=true,
wgEnableWriteAPI=true,
wgSeparatorTransformTable=["", ""],
wgDigitTransformTable=["", ""],
wgMainPageTitle="首页",
wgFormattedNamespaces={"-2": "媒体", "-1": "特殊", "0": "", "1": "讨论", "2": "用户", "3": "用户讨论", "4": "A+医学百科", "5": "A+医学百科讨论", "6": "文件", "7": "文件讨论", "8": "MediaWiki", "9": "MediaWiki讨论", "10": "模板", "11": "模板讨论", "12": "帮助", "13": "帮助讨论", "14": "分类", "15": "分类讨论", "420": "Layer", "421": "Layer talk"},
wgSiteName="A+医学百科",
wgCategories=["制药企业", "企业", "重庆市制药企业", "重庆市"],
wgMWSuggestTemplate="http://www.a-hospital.com/api.php?action=opensearch\x26search={searchTerms}\x26namespace={namespaces}\x26suggest",
wgDBname="ahospital",
wgSearchNamespaces=[0],
wgMWSuggestMessages=["有建议", "无建议"],
wgRestrictionEdit=[],
wgRestrictionMove=[];
</script><script src="http://s.ayxbk.com/common/main-mini.js?278"></script>
<!--[if lt IE 7]><style type="text/css">body{behavior:url("http://s.ayxbk.com/vector/csshover.htc")}</style><![endif]-->
<script type="text/javascript">
window.google_analytics_uacct = "UA-1856547-6";
</script>
<script>if (window.runOnloadHook) runOnloadHook();</script>
<script type="text/javascript">
var gaJsHost = (("https:" == document.location.protocol) ? "https://ssl." : "http://www.");
document.write(unescape("%3Cscript src='" + gaJsHost + "google-analytics.com/ga.js' type='text/javascript'%3E%3C/script%3E"));
</script>
<script type="text/javascript">
var pageTracker = _gat._getTracker("UA-1856547-6");
pageTracker._initData();
pageTracker._trackPageview();
</script><script src="http://maps.google.com/maps/api/js?sensor=false&amp;language=zh-CN&amp;key=AIzaSyBqPw2BmgtcB6r_gYjzgqj2n9NaqibxHPE"></script><script src="/extensions/Maps/includes/services/GoogleMaps3/GoogleMap3Functions.js?270-0.7.8"></script><!-- 178470 --><script>addOnloadHook( function() { 		initGMap3(
			"map_google3_1",
			{	
				scrollwheel: false,
				zoom: 14,
				lat: 29.718137,
				lon: 106.631034,	
				types: [],
				mapTypeId: google.maps.MapTypeId.ROADMAP
			},
			[{"lat": "29.718137", "lon": "106.631034", "title": "\x3cp\x3e重庆药友制药有限责任公司\n\x3c/p\x3e", "label": "", "icon": ""}]
		); } );</script>		<script type="text/javascript"> if ( window.isMSIE55 ) fixalpha(); </script>
		<!-- Served in 0.914 secs. -->			</body>
<!-- Cached/compressed 20181019021154 -->
</html>

"""
    response = HtmlResponse(url='http://www.a-hospital.com/w/%E9%87%8D%E5%BA%86%E8%8D%AF%E5%8F%8B%E5%88%B6%E8%8D%AF%E6%9C%89%E9%99%90%E8%B4%A3%E4%BB%BB%E5%85%AC%E5%8F%B8',
                            body=body, encoding='utf8')
    ppl = AhospitalPipeline()
    spider = HospitalSpider() 
    ppl.open_spider(spider)
    resp_iter = spider.parse(response)
    try:
        page = next(resp_iter)
        assert False
    except StopIteration:
        print("pass")