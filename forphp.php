<!DOCTYPE html>
<html lang="zh-cn">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>子亦.报名</title>
	<link rel="shortcut icon" href="head.ico" type="image/x-icon" />
    <!-- zui -->
    <link href="css/zui.min.css" rel="stylesheet">
  </head>
  <body >
	<header id="header" class="bg-primary">
      <div class="navbar navbar-inverse navbar-fixed-top" id="navbar" role="banner">
        <div class="container">
          <div class="navbar-header">
            <a href="##" class="navbar-brand"><span class="path-zui-36"><i class="path-1"></i><i class="path-2"></i></span> <span class="brand-title">紫丁香之翼-联谊特别活动</span> &nbsp;<small class="zui-version"></small> </a>
          </div>
          <nav class="collapse navbar-collapse zui-navbar-collapse">
            <ul class="nav navbar-nav navbar-right">
				</br>
				<li><i class="icon icon-hand-right"><font face="微软雅黑">By 肆Mars超</font></i></li>
            </ul>
          </nav>
        </div>
      </div>
      
        
      </div>
    </header>
	<div class="container">
		<article class="article">
		<section class="content">
		<h1>OK啦,您的序号是：</h1>
<?php
$con=mysql_connect("localhost","root","root");
mysql_query("set names 'utf8'");

if (! $con)
{
	die("something wrong with sql.sorry;");
}
mysql_select_db("lilacwing",$con);
$numwtd=mysql_num_rows(mysql_query("select * from boy")) + 1;
echo "<h1>" . $numwtd . "</h1>";
$string="";
for ($i=0;$i<32;$i++)
{
	$string .= $_POST["q" . $i];
}

$sentence="INSERT INTO boy VALUES('$_POST[qblank0]','$_POST[qblank1]','$_POST[qblank2]','$_POST[qblank3]','$_POST[qblank4]','$_POST[qblank5]','$_POST[qblank6]','$_POST[qblank7]','$_POST[qblank8]','$string','$_POST[ones_os]','0','0','0','0','0','0','$numwtd')";

if (!mysql_query($sentence,$con))
{
	die ("die");
}

mysql_close($con);


?>
</br>
<h3>快到群里改名片后愉快的玩耍等待消息吧~</h3>
</section>
		  <footer>
			<p class="pull-right text-muted">最终解释权归工大医大联谊策划组所有。</p>
			
		  </footer>
		</article>
	</div>


    <script src="jquery-3.1.1.min.js"></script>
    <script src="js/zui.min.js"></script>
  </body>
</html>