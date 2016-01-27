<%inherit file="base.html"/>
<%block name="bundle">
    <div class="main-setting">
        % if bundle is not None:
            <h1 class="text-center">${_bundle.title}</h1>
        %else:
            <h1 class="text-center">This bundle not active</h1>
        % endif
        <div class="well" style="margin-left: auto; width: 30%">
            <img src="${charity.logo}">
            <h3>${charity.name}</h3>
            <p>${charity.description}</p>
        </div>


        <div class="row">

            % for item in items:
                <div class="col-sm-6 col-md-3">
                    <div class="thumbnail">
                        <img src=${item.image}>
                        <div class="caption">
                            <h3>${item.title}</h3>
                            <pre>${item.description}</pre>
                            <p>
                                <a href="/content/${item.id}" class="btn btn-primary" role="button">Open</a>
                                <label>${item.tier} $</label>
                            </p>
                        </div>
                    </div>
                </div>
            % endfor
        </div>

        <div class="row center-block">
            % for item in bonus:
                <div class="col-sm-6 col-md-3">
                    <div class="thumbnail">
                        <img src=${item.image}>
                        <div class="caption">
                            <h3>${item.title}</h3>
                            <pre>${item.description}</pre>
                            <p>
                                <a href="/content/${item.id}" class="btn btn-primary" role="button">Open</a>
                                <label>${item.tier} $</label>
                            </p>
                        </div>
                    </div>
                </div>
            % endfor

        </div>

        <div class="row center-block">
            <div class="col-xs-5 col-md-3">
                <ul class="nav-justified">
                    <li>SOLD: <strong>${sold}</strong></li>
                    <li>Total raised: <strong>$ ${total_raised}</strong></li>
                </ul>
            </div>
        </div>
        <br/>
        <form action="/pay" method="post" class="form-group">

            <div class="">
                <div class="btn-group" role="group">
                    <button type="button" class="btn btn-default" value="2">2$</button>
                    <button type="button" class="btn btn-default" value="5">5$</button>
                    <button type="button" class="btn btn-default" value="10">10$</button>
                    <button type="button" class="btn btn-default" value="25">25$</button>
                    <button type="button" class="btn btn-default" value="50">50$</button>
                    <br/>
                </div>
                <div class="input-group col-xs-6 col-md-3">
                    <span class="input-group-addon" id="sizing-addon2">amount</span>
                    ${form.amount(class_="form-control", placeholder="amount", value="25", required='')}
                </div>
                <br/>
                <div class="input-group col-xs-6 col-md-3">
                    <span class="input-group-addon" id="sizing-addon2">email</span>
                    ${form.email(class_='form-control', placeholder="email", required='')}
                </div>

                <div class="input-group col-md-2">
                    <h2>Select ratio</h2>
                    <label>charity</label>
                    <input id="range1" type="range" min="0" max="100" value="0"/>
                    <input type="text" id="charity" name="charity" value="0" required/>
                    <br/>
                    <label>content</label>
                    <input id="range2" type="range" min="0" max="100" value="100"/>
                    <input type="text" id="content" name="content" value="100" required/>
                </div>

                <div class="btn-group btn-group-lg">
                    <button type="button" class="btn btn-primary btn-lg" data-toggle="modal" data-target="#myModal">
                        Continue
                    </button>
                    <!-- Modal -->
                    <div class="modal fade" id="myModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">
                        <div class="modal-dialog" role="document">
                            <div class="modal-content">
                                <div class="modal-header">
                                    <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span
                                            aria-hidden="true">&times;</span></button>
                                    <h4 class="modal-title" id="myModalLabel">Credit cards</h4>
                                </div>
                                <div class="modal-body">
                                    <p>Please, enter the number of your payment card</p>
                                    ${form.card(class_='form-control', placeholder="card", required='')}
                                </div>
                                <div class="modal-footer">
                                    <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
                                    <input type="submit" class="btn btn-info" value="Buy now">
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </form>
    </div>
</%block>