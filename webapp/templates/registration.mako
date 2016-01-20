<!-- All the files that are required -->
<link rel="stylesheet" href="../static/css/bootstrap.min.css">
<link rel="stylesheet" href="../static/css/login.css">
<link href='http://fonts.googleapis.com/css?family=Varela+Round' rel='stylesheet' type='text/css'>
<script src="../static/js/jquery.validate.min.js"></script>
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1" />


<!-- REGISTRATION FORM -->
<div class="text-center" style="padding:50px 0">
	<div class="logo">register</div>
	<!-- Main Form -->
	<div class="login-form-1">
		<form id="register-form" class="text-left" action="/registration" method="post">
			<div class="login-form-main-message"></div>
			<div class="main-login-form">
				<div class="login-group">
					<div class="form-group">
						<label for="reg_username" class="sr-only">Email address</label>
                        ${form.username(class_="form-control", placeholder="username")}
					</div>
					<div class="form-group">
						<label for="reg_password" class="sr-only">Password</label>
                        ${form.password(class_="form-control", placeholder="password")}
					</div>
					<div class="form-group">
						<label for="reg_password_confirm" class="sr-only">Password Confirm</label>
                        ${form.confirm_password(class_="form-control", placeholder="confirm password")}
					</div>
					<div class="form-group">
						<label for="reg_email" class="sr-only">Email</label>
                        ${form.email(class_="form-control", placeholder="email")}
					</div>
					<div class="form-group login-group-checkbox">

                        ${form.sex(class_="form-control")}
					</div>

					<div class="form-group login-group-checkbox">
						<input type="checkbox" class="" id="reg_agree" name="reg_agree">
						<label for="reg_agree">i agree with <a href="#">terms</a></label>
					</div>
				</div>
				<button type="submit" class="login-button"><i class="fa fa-chevron-right"></i></button>
			</div>
			<div class="etc-login-form">
				<p>already have an account? <a href="/login">login here</a></p>
			</div>
		</form>
	</div>
	<!-- end:Main Form -->
</div>