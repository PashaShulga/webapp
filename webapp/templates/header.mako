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
                <!--?<li class="active"><a href="#">Link <span class="sr-only">(current)</span></a></li>-->
                <li><a href="/about">About</a></li>
                <li><a href="/bundle_preview">bundles</a></li>
            </ul>
            <ul class="nav navbar-nav navbar-right">
                % if user is not None:
                    <li><a href='/logout'>logout</a></li>
                    <li><a href="/account/id=${user}">My Profile</a></li>
                %else:
                    <li><a href='/login'>login</a></li>
                % endif
            </ul>
        </div><!-- /.navbar-collapse -->
    </div><!-- /.container-fluid -->
</nav>