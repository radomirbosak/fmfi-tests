<h1>{{title}}</h1>
% if files:
<ul>
	% for title, filename, ext in files:
    <li>{{title}} <a href="{{filename}}">{{ext}}</a></li>
    % end
</ul>
% end

% for subdir in dirs:
<h2>{{subdir['title']}}</h2>
<ul>
	% for title, filename, ext in subdir['files']:
    <li>{{title}} <a href="{{filename}}">{{ext}}</a></li>
    % end
</ul>
%	for ssdir in subdir['dirs']:
<h3>{{ssdir['title']}}</h3>
<ul>
	% for title, filename, ext in ssdir['files']:
    <li>{{title}} <a href="{{filename}}">{{ext}}</a></li>
    % end
</ul>
%	end
% end