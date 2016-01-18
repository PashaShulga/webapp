<!DOCTYPE html>
<html lang="en" xmlns="http://www.w3.org/1999/html">
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>humble</title>

    <!-- Bootstrap -->
    <link href="../static/css/bootstrap.min.css" rel="stylesheet">
    <link href="../static/css/style.css" rel="stylesheet">

    <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
    <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
    <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
    <![endif]-->
</head>
<body>

<nav class="navbar navbar-default">
    <div class="container-fluid">
        <!-- Brand and toggle get grouped for better mobile display -->
        <div class="navbar-header">
            <a class="navbar-brand" href="/">
                <img alt="Brand" src="../static/img/logo.png" style="width: 35px; height: 35px;">
            </a>
        </div>

        <!-- Collect the nav links, forms, and other content for toggling -->
        <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
            <ul class="nav navbar-nav">
                <li class="active"><a href="#">Link <span class="sr-only">(current)</span></a></li>
                <li><a href="#">Link</a></li>
            </ul>
            <ul class="nav navbar-nav navbar-right">
                <!--?<li><a href="/login">Login</a></li>-->
                <li><a href="${link}">${login_status}</a></li>
            </ul>
        </div><!-- /.navbar-collapse -->
    </div><!-- /.container-fluid -->
</nav>

<div class="main-setting">
<div class="row">
    <div class="col-sm-6 col-md-3">
    <div class="thumbnail">
      <img src='${content.image}'>
      <div class="caption">
        <h3>${content.title}</h3>
        <pre>${content.description}</pre>
        <p><a href="#" class="btn btn-primary" role="button">Button</a> <a href="#" class="btn btn-default" role="button">Button</a></p>
      </div>
    </div>
  </div>

    <div class="col-sm-6 col-md-3">
    <div class="thumbnail">
      <img src="..." alt="...">
      <div class="caption">
        <h3>Thumbnail label</h3>
        <p>...</p>
        <p><a href="#" class="btn btn-primary" role="button">Button</a> <a href="#" class="btn btn-default" role="button">Button</a></p>
      </div>
    </div>
  </div>
    <div class="col-sm-6 col-md-3">
    <div class="thumbnail">
      <img src="..." alt="...">
      <div class="caption">
        <h3>Thumbnail label</h3>
        <p>...</p>
        <p><a href="#" class="btn btn-primary" role="button">Button</a> <a href="#" class="btn btn-default" role="button">Button</a></p>
      </div>
    </div>
  </div>
    <div class="col-sm-6 col-md-3">
    <div class="thumbnail">
      <img src="..." alt="...">
      <div class="caption">
        <h3>Thumbnail label</h3>
        <p>...</p>
        <p><a href="#" class="btn btn-primary" role="button">Button</a> <a href="#" class="btn btn-default" role="button">Button</a></p>
      </div>
    </div>
  </div>

</div>

<div class="row center-block">

    <div class="col-xs-6 col-md-3">
        <a href="#" class="thumbnail">
            <p>Bonus content 4</p>
        </a>
    </div>

    <div class="col-xs-6 col-md-3">
        <a href="#" class="thumbnail">
            <p>Bonus content 4</p>
        </a>
    </div>
</div>

<div class="row center-block">
    <div class="col-xs-5 col-md-3">
        <h3>SOLD: <strong>5000</strong></h3>
        <h2>Total sum: <strong>$ 9000</strong></h2>
    </div>
</div>
<br/>
<form action="/pay" method="post" class="form-group">

    <div class="center-block">
        <div class="btn-group" role="group">
            <button type="button" class="btn btn-default" id="" value="2">2$</button>
            <button type="button" class="btn btn-default" value="5">5$</button>
            <button type="button" class="btn btn-default" value="10">10$</button>
            <button type="button" class="btn btn-default" value="25">25$</button>
            <button type="button" class="btn btn-default" value="50">50$</button>
        </div>
        <div class="input-group center-block col-xs-6 col-md-3">
            <span class="input-group-addon" id="sizing-addon2">amount</span>
                ${form.amount(class_="form-control", placeholder="amount")}
        </div>
        <br/>
        <div class="input-group center-block col-xs-6 col-md-3">
            <span class="input-group-addon" id="sizing-addon2">email</span>
                ${form.email(class_='form-control', placeholder="email")}
        </div>
        <br/>

        <div class="center-block input-group col-md-2">
            <h2>Select ratio</h2>

            <input id="range1" type="range" min="0" max="100" value="0"/>
            <br/>
            <label>0</label>
            <input id="range2" type="range" min="0" max="100" value="100"/>
        </div>

        <div class="center-block btn-group btn-group-lg">
            <input type="submit" class="btn btn-default" value="Buy now">
        </div>
    </div>
</form>
</div>

<!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js"></script>
<script src="../static/js/slider.js" type="application/javascript"></script>
<!-- Include all compiled plugins (below), or include individual files as needed -->
<script src="../static/js/bootstrap.min.js"></script>
</body>
</html>