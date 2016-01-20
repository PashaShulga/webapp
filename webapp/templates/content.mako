<%inherit file="base.html"/>
<%block name="content">
<div class="col-md-7">
<div class="media">
  <div class="media-left media-middle">
    <a href="#">
      <img class="media-object" src="${image}" style="width: 200px; height: 200px;">
    </a>
  </div>
  <div class="media-body">
    <h1 class="media-heading">${title}</h1>
    <h3 class="media-heading">${manufacture}</h3>
      <p style="word-wrap: break-word">${description}</p>
       % if link is not None:
           <a href="${link}">Link</a>
       % endif
  </div>
</div>
    </div>
</%block>