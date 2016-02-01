<%inherit file="base.html"/>
<%block name="preview_bundles">
    <div class="main-setting">
<div class="row">
            % for item in items:
                <div class="col-sm-6 col-md-3">
                    <div class="thumbnail">
                        <div class="caption">
                            <a href="/bundle/${item.id}"><h3>${item.title}</h3></a>
                            <pre>${item.description}</pre>
                                <p><strong>Start date:</strong> ${item.date_start.strftime("%Y-%m-%d")}</p>
                                <p><strong>End date:</strong> ${item.date_end.strftime("%Y-%m-%d")}</p>
                        </div>
                    </div>
                </div>
            % endfor
        </div>
    </div>
</%block>