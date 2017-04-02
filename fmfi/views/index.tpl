<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8" />
        <base href="{{base}}">
        <link rel="stylesheet" type="text/css" href="static/style.css" />
        <title>FMFI</title>
    </head>
    <body>
        <div class="navbar" id="navbar2">
            <a href="/c/bak"    class="bcmgr{{" active" if bcmgr=='bc' else ''}}">Bakalárske predmety</a>
            <a href="/c/mag"    class="bcmgr{{" active" if bcmgr=='mgr' else ''}}">Magisterské predmety</a>
            <br style="clear: both;" />
        </div>
        <div class="navbar" id="navbar1">
            % for abbrev, class_, title in predmety:
            <a href="/s/{{abbrev}}"     class="{{class_}}">{{title}}</a>
            % end
            <br style="clear: both;" />
        </div>
        <div id="content">
            <% 
            if include_page:
                include(include_page, **content)
            end 
            %>
        <p><em>updatované {{updated}}</em></p>
        </div>
        
    </body>
</html>