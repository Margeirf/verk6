% rebase('base.tpl', title='Verkefni 6')

<h4>Items:</h4>
<a href="/items?vara=1"><img src="static/1.jpeg" height="100", width="100"></a>
<a href="/items?vara=2"><img src="static/2.jpeg" height="100", width="100"></a>
<a href="/items?vara=3"><img src="static/3.jpeg" height="100", width="100"></a>
<a href="/items?vara=4"><img src="static/4.jpeg" height="100", width="100"></a>
<a href="/items?vara=5"><img src="static/5.jpeg" height="100", width="100"></a>
<a href="/items?vara=6"><img src="static/6.jpeg" height="100", width="100"></a>
<hr>
% if nyvor != None:
    <h4>Nýlega skoðað:</h4>
    % for x in nyvor:
        <a href="/items?item={{x}}"><img src="static/{{x}}.jpeg" height="100", width="100"></a>
% end