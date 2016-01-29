<%inherit file="base.html"/>
<%block name="bonus">
    <link href="../static/css/profile.css" rel="stylesheet">
        <script src="../static/js/profile.js"></script>
## <nav class="navbar navbar-default navbar-fixed-top" role="navigation">
##     <hr class="colorgraph colorgraph-header">
##     <div class="container">
##         <!-- Brand and toggle get grouped for better mobile display -->
##         <div class="navbar-header">
##             <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#main-navbar-collapse">
##                 <span class="sr-only">Toggle navigation</span>
##                 <span class="icon-bar"></span>
##                 <span class="icon-bar"></span>
##                 <span class="icon-bar"></span>
##             </button>
##             <a class="navbar-brand" href="#">Elementary</a>
##         </div>
##         <!-- Collect the nav links, forms, and other content for toggling -->
##         <div class="collapse navbar-collapse" id="main-navbar-collapse">
##             <ul class="nav navbar-nav navbar-right">
##                 <li>
##                     <a href="#"><i class="fa fa-search"></i> Search</a>
##                 </li>
##                 <li>
##                     <a href="#"><i class="fa fa-folder"></i> Browse Files</a>
##                 </li>
##                 <li>
##                     <a href="#"><i class="fa fa-bullhorn"></i> Notice Board</a>
##                 </li>
##                 <li class="dropdown active">
##                     <a href="#" class="dropdown-toggle" data-toggle="dropdown">
##                         <i class="fa fa-user"></i> My Profile
##                         <b class="caret"></b>
##                     </a>
##                     <ul class="dropdown-menu">
##                         <li class=""><a href="#"><i class="fa fa-cogs"></i> Settings</a></li>
##                         <li><a href="#"><i class="fa fa-power-off"></i> Logout</a></li>
##                     </ul>
##                 </li>
##             </ul>
##         </div>
##         <!-- /.navbar-collapse -->
##     </div>
##     <!-- /.container -->
## </nav>

<div class="container">
    <div class="row">
        <div class="col-md-9 col-sm-12">
            <div class="panel panel-default profile-panel">
                <div class="panel-body">
                    <div class="row">
                        <div class="col-sm-3 col-xs-12 text-center" >
                            <img src="https://graph.facebook.com/urmi.saha.754/picture?width=150&height=150" class="img-circle user-image">
                        </div>
                        <div class="col-sm-9 col-xs-12 user-info-box">
                            <a class="btn btn-info pull-right btn-edit" href="#" data-toggle="modal" data-target="#edit-profile">
                                <i class="fa fa-edit"></i>
                                Edit…
                            </a>
                            <h3 class="user-name">Urmi Saha</h3>
                            <p><strong>Dept. of <span class="user-dept">Computer Science & Engineering</span></strong></p>
                            <p><span class="user-year">3rd Year</span>, <span class="user-sem">5th Semester</span></p>
                            <p><a href="#more-info-panel" data-toggle="collapse" data-target="#more-info-panel" class="more-info-toggle">More ▼</a></p>
                            <div id="more-info-panel" class="collapse out">
                                <div class="row">
                                    <div class="col-md-6 col-sm-6 col-xs-12">
                                        <p><strong><i class="fa fa-envelope"></i> E-mail: </strong><span class="user-email">user@example.com</span></p>
                                        <p><strong><i class="fa fa-phone-square"></i> Phone: </strong><span class="user-phone">9434000000</span></p>
                                        <p><strong><i class="fa fa-users"></i> Admission Year: </strong><span class="user-admission-year">2016</span></p>
                                    </div>
                                    <div class="col-md-6 col-sm-6 col-xs-12">
                                        <p><strong><i class="fa fa-pencil"></i> Course: </strong><span class="user-course">B. Tech.</span></p>
                                        <p><strong><i class="fa fa-calendar"></i> Date of Birth: </strong><span class="user-dob">01-01-1994</span></p>
                                        <p><strong><i class="fa fa-bars"></i> Enrollment No: </strong><span class="user-enrollment-no">12012002004000</span></p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="panel panel-default academic-panel">
                <div class="panel-body">
                    <h3><i class="fa fa-book fa-lg"></i> My Academic Record</h3>
                    <hr class="colorgraph">
                    <table class="table table-hover table-responsive">
                        <thead>
                            <tr>
                                <th>#</th>
                                <th>First Name</th>
                                <th>Last Name</th>
                                <th>Semester</th>
                                <th>GPA</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>1</td>
                                <td>John</td>
                                <td>Carter</td>
                                <td>7th</td>
                                <td>9.2</td>
                            </tr>
                            <tr>
                                <td>2</td>
                                <td>Peter</td>
                                <td>Parker</td>
                                <td>4th</td>
                                <td>1.6</td>
                            </tr>
                            <tr>
                                <td>3</td>
                                <td>John</td>
                                <td>Rambo</td>
                                <td>200th</td>
                                <td>6.66</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>

            <div class="panel panel-default projects-panel">
                <div class="panel-body">
                    <h3><i class="fa fa-folder-open fa-lg"></i> My Projects</h3>
                    <hr class="colorgraph">
                    <table class="table table-hover table-responsive">
                        <thead>
                            <tr>
                                <th>#</th>
                                <th>First Name</th>
                                <th>Last Name</th>
                                <th>Semester</th>
                                <th>GPA</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>1</td>
                                <td>John</td>
                                <td>Carter</td>
                                <td>7th</td>
                                <td>9.2</td>
                            </tr>
                            <tr>
                                <td>2</td>
                                <td>Peter</td>
                                <td>Parker</td>
                                <td>4th</td>
                                <td>1.6</td>
                            </tr>
                            <tr>
                                <td>3</td>
                                <td>John</td>
                                <td>Rambo</td>
                                <td>200th</td>
                                <td>6.66</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>

            <div class="panel panel-default achievements-panel">
                <div class="panel-body">
                    <h3><i class="fa fa-trophy fa-lg"></i> My Achievements</h3>
                    <hr class="colorgraph">
                    <table class="table table-hover table-responsive">
                        <thead>
                            <tr>
                                <th>#</th>
                                <th>First Name</th>
                                <th>Last Name</th>
                                <th>Semester</th>
                                <th>GPA</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>1</td>
                                <td>John</td>
                                <td>Carter</td>
                                <td>7th</td>
                                <td>9.2</td>
                            </tr>
                            <tr>
                                <td>2</td>
                                <td>Peter</td>
                                <td>Parker</td>
                                <td>4th</td>
                                <td>1.6</td>
                            </tr>
                            <tr>
                                <td>3</td>
                                <td>John</td>
                                <td>Rambo</td>
                                <td>200th</td>
                                <td>6.66</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
        <div class="col-md-3 col-sm-12">
            <div class="row">
                <!-- Panel 2 -->
                <div class="col-md-12 col-sm-6 col-xs-12">
                    <div class="panel panel-default">
                        <div class="panel-heading">
                            <i class="fa fa-bullhorn fa-lg"></i> 
                            Recent Notices
                        </div>
                        <div class="panel-body">
                            <div id="notice-slider" class="carousel slide sidebar-slider" data-interval="10000" data-ride="carousel">
                                <!-- Carousel indicators -->
                                <ol class="carousel-indicators">
                                    <li data-target="#notice-slider" data-slide-to="0" class="active"></li>
                                    <li data-target="#notice-slider" data-slide-to="1"></li>
                                    <li data-target="#notice-slider" data-slide-to="2"></li>
                                </ol>
                               <!-- Carousel items -->
                                <div class="carousel-inner">
                                    <div class="active item">
                                        <h4>Notice 1</h4>
                            			<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quidem, veritatis nulla eum laudantium totam tempore optio doloremque laboriosam quas, quos eaque molestias odio aut eius animi. Impedit temporibus nisi accusamus.</p>
                                        <p>SSG</p>
                                    </div>
                                    <div class="item">
                                        <h4>Notice 2</h4>
                        				<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quidem, veritatis nulla eum laudantium totam tempore optio doloremque laboriosam quas, quos eaque molestias odio aut eius animi. Impedit temporibus nisi accusamus.</p>
                                        <p>SMU</p>
                                    </div>
                                    <div class="item">
                                        <h4>Notice 3</h4>
                                        <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quidem, veritatis nulla eum laudantium totam tempore optio doloremque laboriosam quas, quos eaque molestias odio aut eius animi. Impedit temporibus nisi accusamus.</p>
                                        <p>NDR</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Panel 2 -->
                <div class="col-md-12 col-sm-6 col-xs-12">
                    <div class="panel panel-default">
                        <div class="panel-heading">
                            <i class="fa fa-file fa-lg"></i> 
                            Recent Uploads
                        </div>
                        <div class="panel-body">
                            Ad leggings keytar, brunch id art party dolor labore. Pitchfork yr enim lo-fi before they sold out qui. Tumblr farm-to-table bicycle rights whatever. Anim keffiyeh carles cardigan.
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

<!-- Modal -->
<div class="modal fade" id="edit-profile" tabindex="-1" role="dialog" aria-labelledby="edit-profile-label" aria-hidden="true">
    <div class="modal-dialog">
        <div class="modal-content">
            <form class="form-horizontal" role="form">
                <div class="modal-header">
                    <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span class="sr-only">Close</span></button>
                    <h4 class="modal-title" id="edit-profile">Edit Profile</h4>
                </div>
                <div class="modal-body">
                    <div class="form-group">
                        <label class="col-sm-2 control-label" for="user-name">Name</label>
                        <div class="col-sm-10">
                            <input type="text" class="form-control" id="user-name" name="user-name" placeholder="Full Name" required>
                        </div>
                    </div>
                    <div class="form-group">
                        <label class="col-sm-2 control-label" for="user-dept">Department</label>
                        <div class="col-sm-10">
                            <input type="text" class="form-control" id="user-dept" name="user-dept" placeholder="Department" required>
                        </div>
                    </div>
                    <div class="form-group">
                        <label class="col-sm-2 control-label" for="user-year">Year</label>
                        <div class="col-sm-4">
                            <input type="text" class="form-control" id="user-year" name="user-year" placeholder="Year" required>
                        </div>
                        <p class="visible-xs help-block"></p><!-- Spacer -->
                        <label class="col-sm-2 control-label" for="user-sem">Semester</label>
                        <div class="col-sm-4">
                            <input type="text" class="form-control" id="user-sem" name="user-sem" placeholder="Semester" required>
                        </div>
                    </div>
                    <hr>
                    <div class="form-group">
                        <label class="col-sm-2 control-label" for="user-enrollment-no">Enrollment No.</label>
                        <div class="col-sm-10">
                            <input type="text" class="form-control" id="user-enrollment-no" name="user-enrollment-no" placeholder="Enrollment Number" required>
                        </div>
                    </div>
                    <div class="form-group">
                        <label class="col-sm-2 control-label" for="user-admission-year">Admission Year</label>
                        <div class="col-sm-4">
                            <input type="text" class="form-control" id="user-admission-year" name="user-admission-year" placeholder="Admission Year" required>
                        </div>
                        <p class="visible-xs help-block"></p><!-- Spacer -->
                        <label class="col-sm-2 control-label" for="user-dob">Date of Birth</label>
                        <div class="col-sm-4">
                            <input type="text" class="form-control" id="user-dob" name="user-dob" placeholder="Date of Birth" required>
                        </div>
                    </div>
                    <div class="form-group">
                        <label class="col-sm-2 control-label" for="user-course">Course</label>
                        <div class="col-sm-10">
                            <input type="text" class="form-control" id="user-course" name="user-course" placeholder="Course" required>
                        </div>
                    </div>
                    <hr>
                    <div class="form-group">
                        <label class="col-sm-2 control-label" for="user-email">E-mail Address</label>
                        <div class="col-sm-10">
                            <input type="email" class="form-control" id="user-email" name="user-email" placeholder="E-mail Address" required>
                        </div>
                    </div>
                    <div class="form-group">
                        <label class="col-sm-2 control-label" for="user-phone">Contact No.</label>
                        <div class="col-sm-10">
                            <input type="text" class="form-control" id="user-phone" name="user-phone" placeholder="Contact Number" required>
                        </div>
                    </div>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
                    <button type="submit" class="btn btn-primary">Save changes</button>
                </div>
            </form>
        </div>

    </div>
</div>

</%block>