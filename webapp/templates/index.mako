<%inherit file="base.html"/>
<%block name="main">
<div class="main-setting">
    % if bundle is not None:
        <h1 class="text-center">${bundle.title}</h1>
    %else:
        <h1 class="text-center">This bundle not active</h1>
    % endif

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
                <br />
            </div>
            <div class="input-group col-xs-6 col-md-3">
                <span class="input-group-addon" id="sizing-addon2">amount</span>
                    ${form.amount(class_="form-control", placeholder="amount")}
            </div>
            <br/>
            <div class="input-group col-xs-6 col-md-3">
                <span class="input-group-addon" id="sizing-addon2">email</span>
                    ${form.email(class_='form-control', placeholder="email")}
            </div>

            <div class="input-group col-md-2">
                <h2>Select ratio</h2>
                <label>charity</label>
                <input id="range1" type="range" min="0" max="100" value="0"/>
                <input type="text" id="charity" name="charity" value="0"/>
                <br/>
                <label>content</label>
                <input id="range2" type="range" min="0" max="100" value="100"/>
                <input type="text" id="content" name="content" value="100"/>
            </div>

            <div class="btn-group btn-group-lg">
                <input type="submit" class="btn btn-info" value="Buy now">
            </div>
        </div>
    </form>
</div>

<!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js"></script>
<script src="../static/js/slider.js" type="application/javascript"></script>
<!-- Include all compiled plugins (below), or include individual files as needed -->
<script src="../static/js/bootstrap.min.js"></script>
</%block>