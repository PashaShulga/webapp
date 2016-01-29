<%block name="login">
<!-- All the files that are required -->
<link rel="stylesheet" href="../static/css/bootstrap.min.css">
<link rel="stylesheet" href="../static/css/login.css">
<link href='http://fonts.googleapis.com/css?family=Varela+Round' rel='stylesheet' type='text/css'>
<script src="../static/js/jquery.validate.min.js"></script>
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1" />

<!-- Where all the magic happens -->
<!-- LOGIN FORM -->
<div class="text-center" style="padding:50px 0">
	<div class="logo"><span> ${message} </span></div>
	<!-- Main Form -->
	<div class="login-form-1">
		<form id="login-form" class="text-left" method="post" action=${url}>
			<div class="login-form-main-message"></div>
			<div class="main-login-form">
				<div class="login-group">
					<div class="form-group">
						<label for="lg_password" class="sr-only">username</label>
                        ${form.username(class_="form-control", placeholder="email")}
					</div>
                    <div class="form-group">
						<label for="lg_password" class="sr-only">Password</label>
                        ${form.password(class_="form-control", placeholder="password")}
					</div>
					<div class="form-group login-group-checkbox">
						<input type="checkbox" id="lg_remember" name="lg_remember">
						<label for="lg_remember">remember</label>
					</div>
				</div>
				<button type="submit" class="login-button"><i class="fa fa-chevron-right"></i></button>
			</div>
			<div class="etc-login-form">
				<p>forgot your password? <a href="#">click here</a></p>
				<p>New user? <a href="/registration">create an account</a></p>
			</div>
		</form>
	</div>
	<!-- end:Main Form -->
</div>
</%block>