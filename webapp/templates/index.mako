<%inherit file="base.html"/>
<%block name="main">
<div class="main-setting">
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
                        </p>
                    </div>
                </div>
            </div>
        % endfor
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
            <ul class="nav-justified">
            <li>SOLD: <strong>${sold}</strong></li>
            <li>Total raised: <strong>$ ${total_raised}</strong></li>
                </ul>
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
</%block>