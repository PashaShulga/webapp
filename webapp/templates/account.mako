<%inherit file="base.html"/>
<%block name="bonus">
    <link href="../static/css/profile.css" rel="stylesheet">
    <script src="../static/js/profile.js"></script>
    <div class="container">
        <div class="row">
            <div class="col-md-9 col-sm-12">
                <div class="panel panel-default profile-panel">
                    <div class="panel-body">
                        <div class="row">
                            <div class="col-sm-9 col-xs-12 user-info-box">
                                <h3 class="user-name">${user.mail}</h3>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="panel panel-default projects-panel">
                    <div class="panel-body">
                        <h3><i class="fa fa-folder-open fa-lg"></i> My Bundles</h3>
                        <hr class="colorgraph">
                        <table class="table table-hover table-responsive">
                            <thead>
                            <tr>
                                <th>Bundle</th>
                                <th>Charity $</th>
                                <th>Content $</th>
                                <th>Date</th>
                            </tr>
                            </thead>
                            <tbody>
                                % for orders, bundle in query:
                                    <tr>
                                    <td>${bundle.title}</td>
                                    <td>${orders.sum_charity}</td>
                                    <td>${orders.sum_content}</td>
                                    <td>${orders.timestamp.strftime("%Y-%m-%d")}</td>
                                    </tr>
                                % endfor
                            </tbody>
                        </table>
                    </div>
                </div>

##     <div class="modal fade" id="edit-profile" tabindex="-1" role="dialog" aria-labelledby="edit-profile-label"
##          aria-hidden="true">
##         <div class="modal-dialog">
##             <div class="modal-content">
##                 <form class="form-horizontal" role="form">
##                     <div class="modal-header">
##                         <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span
##                                 class="sr-only">Close</span></button>
##                         <h4 class="modal-title" id="edit-profile">Edit Profile</h4>
##                     </div>
##                     <div class="modal-body">
##                         <div class="form-group">
##                             <label class="col-sm-2 control-label" for="user-name">Name</label>
##                             <div class="col-sm-10">
##                                 <input type="text" class="form-control" id="user-name" name="user-name"
##                                        placeholder="Full Name" required>
##                             </div>
##                         </div>
##                         <div class="form-group">
##                             <label class="col-sm-2 control-label" for="user-dept">Department</label>
##                             <div class="col-sm-10">
##                                 <input type="text" class="form-control" id="user-dept" name="user-dept"
##                                        placeholder="Department" required>
##                             </div>
##                         </div>
##                         <div class="form-group">
##                             <label class="col-sm-2 control-label" for="user-year">Year</label>
##                             <div class="col-sm-4">
##                                 <input type="text" class="form-control" id="user-year" name="user-year"
##                                        placeholder="Year" required>
##                             </div>
##                             <p class="visible-xs help-block"></p><!-- Spacer -->
##                             <label class="col-sm-2 control-label" for="user-sem">Semester</label>
##                             <div class="col-sm-4">
##                                 <input type="text" class="form-control" id="user-sem" name="user-sem"
##                                        placeholder="Semester" required>
##                             </div>
##                         </div>
##                         <hr>
##                         <div class="form-group">
##                             <label class="col-sm-2 control-label" for="user-enrollment-no">Enrollment No.</label>
##                             <div class="col-sm-10">
##                                 <input type="text" class="form-control" id="user-enrollment-no"
##                                        name="user-enrollment-no" placeholder="Enrollment Number" required>
##                             </div>
##                         </div>
##                         <div class="form-group">
##                             <label class="col-sm-2 control-label" for="user-admission-year">Admission Year</label>
##                             <div class="col-sm-4">
##                                 <input type="text" class="form-control" id="user-admission-year"
##                                        name="user-admission-year" placeholder="Admission Year" required>
##                             </div>
##                             <p class="visible-xs help-block"></p><!-- Spacer -->
##                             <label class="col-sm-2 control-label" for="user-dob">Date of Birth</label>
##                             <div class="col-sm-4">
##                                 <input type="text" class="form-control" id="user-dob" name="user-dob"
##                                        placeholder="Date of Birth" required>
##                             </div>
##                         </div>
##                         <div class="form-group">
##                             <label class="col-sm-2 control-label" for="user-course">Course</label>
##                             <div class="col-sm-10">
##                                 <input type="text" class="form-control" id="user-course" name="user-course"
##                                        placeholder="Course" required>
##                             </div>
##                         </div>
##                         <hr>
##                         <div class="form-group">
##                             <label class="col-sm-2 control-label" for="user-email">E-mail Address</label>
##                             <div class="col-sm-10">
##                                 <input type="email" class="form-control" id="user-email" name="user-email"
##                                        placeholder="E-mail Address" required>
##                             </div>
##                         </div>
##                         <div class="form-group">
##                             <label class="col-sm-2 control-label" for="user-phone">Contact No.</label>
##                             <div class="col-sm-10">
##                                 <input type="text" class="form-control" id="user-phone" name="user-phone"
##                                        placeholder="Contact Number" required>
##                             </div>
##                         </div>
##                     </div>
##                     <div class="modal-footer">
##                         <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
##                         <button type="submit" class="btn btn-primary">Save changes</button>
##                     </div>
##                 </form>
##             </div>
##
        </div>
    </div>
    </div>

</%block>