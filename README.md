DashDoc provides integration of [Dash][1] into Sublime Text.

## Usage

You can look up the word under the cursor or selected text in Dash using `ctrl+h`.

## Installation
Use [Sublime Package Control][6].

## Options

As usual, you will find the associated settings under the *Preferences / Package Settings / DashDoc* menu.  Personal settings should be made in *Settings - User*.

### Syntax sensitivity

By default, DashDoc is sensitive to the syntax used in the current view. Dash will then consult the docset that matches the current syntax.  Example: a lookup for `map` in a Haskell buffer will instruct Dash to search in its `haskell` docset, a search for the same word in a Python buffer will consult the `python` docset instead.

Syntax-insensitive search may be invoked using the `ctrl+alt+h` hotkey. You have an option to switch the default method of searching with config option `syntax_sensitive_as_default`, which defaults to true. If you set it to false, then `ctrl+h` becomes syntax-insensitive, and `ctrl+alt+h` becomes the sensitive option.

### Choosing a Dash docset for a given syntax

For any Sublime Text syntax, DashDoc can search a number of docsets of your choosing. Use map entries of the form `{ <syntax> : [ <docset>, <docset>, ... ] }`. For `<docset>`, use the lowercase docset prefixes that Dash indicates in its *Preferences / Docsets* pane.  Dash searches the list of docsets in the given order.

For particular projects, you can override individual syntax-to-docsets mappings in the `settings` of the project's `.sublime-project` file, for example:

    "settings": {
      "syntax_docset_map": {
        "Objective-C": ["iphoneos", "cocos2d"]
      }
    }

Mappings that are not overridden this way default to what is found in the `DashDoc.sublime-settings` file.  The default mapping, derived from [Dash's suggestion][3], is:

    "syntax_docset_map":
    {
      "ActionScript"          : ["actionscript"],
      "Boo"                   : ["unity3d"],
      "C"                     : ["c", "glib", "gl2", "gl3", "gl4", "manpages"],
      "C99"                   : ["c", "glib", "gl2", "gl3", "gl4", "manpages"],
      "C++"                   : ["cpp", "net", "boost", "qt", "cvcpp", "cocos2dx", "c", "manpages"],
      "C++11"                 : ["cpp", "net", "boost", "qt", "cvcpp", "cocos2dx", "c", "manpages"],
      "Clojure"               : ["clojure"],
      "CoffeeScript"          : ["coffee"],
      "ColdFusion"            : ["cf"],
      "CSS"                   : ["css", "bootstrap", "foundation", "less", "cordova", "phonegap"],
      "Elixir"                : ["elixir"],
      "Erlang"                : ["erlang"],
      "Go"                    : ["go"],
      "GoSublime"             : ["go"],
      "GoSublime-Go"          : ["go"],
      "Groovy"                : ["groovy"],
      "Haskell"               : ["haskell"],
      "Haskell-SublimeHaskell": ["haskell"],
      "Literate Haskell"      : ["haskell"],
      "HTML"                  : ["html", "svg", "css", "bootstrap", "foundation", "javascript", "jquery", "jqueryui", "jquerym", "angularjs", "backbone", "marionette", "meteor", "moo", "prototype", "ember", "lodash", "underscore", "sencha", "extjs", "knockout", "zepto", "cordova", "phonegap", "yui"],
      "Jade"                  : ["jade"],
      "Java"                  : ["java", "javafx", "grails", "groovy", "playjava", "spring", "cvj", "processing"],
      "JavaScript"            : ["javascript", "jquery", "jqueryui", "jquerym", "backbone", "marionette", "meteor", "sproutcore", "moo", "prototype", "bootstrap", "foundation", "lodash", "underscore", "ember", "sencha", "extjs", "knockout", "zepto", "yui", "d3", "svg", "dojo", "coffee", "nodejs", "express", "chai", "html", "css", "cordova", "phonegap", "unity3d"],
      "Less"                  : ["less"],
      "Lisp"                  : ["lisp"],
      "Lua"                   : ["lua", "corona"],
      "Markdown"              : ["markdown"],
      "MultiMarkdown"         : ["markdown"],
      "Objective-C"           : ["iphoneos", "macosx", "appledoc", "cocos2d", "cocos3d", "kobold2d", "sparrow", "c", "manpages"],
      "Objective-C++"         : ["cpp", "iphoneos", "macosx", "appledoc", "cocos2d", "cocos2dx", "cocos3d", "kobold2d", "sparrow", "c", "manpages"],
      "Objective-J"           : ["cappucino"],
      "OCaml"                 : ["ocaml"],
      "Perl"                  : ["perl", "manpages"],
      "PHP"                   : ["php", "wordpress", "drupal", "zend", "laravel", "yii", "joomla", "ee", "codeigniter", "cakephp", "symfony", "typo3", "twig", "smarty", "html", "mysql", "sqlite", "mongodb", "psql", "redis"],
      "Processing"            : ["processing"],
      "Puppet"                : ["puppet"],
      "Python"                : ["python", "django", "twisted", "sphinx", "flask", "cvp"],
      "R"                     : ["r"],
      "Ruby"                  : ["ruby", "rubygems", "rails"],
      "Ruby on Rails"         : ["ruby", "rubygems", "rails"],
      "(HTML) Rails"          : ["ruby", "rubygems", "rails", "html", "svg", "css", "bootstrap", "foundation", "javascript", "jquery", "jqueryui", "jquerym", "angularjs", "backbone", "marionette", "meteor", "moo", "prototype", "ember", "lodash", "underscore", "sencha", "extjs", "knockout", "zepto", "cordova", "phonegap", "yui"],
      "(JavaScript) Rails"    : ["ruby", "rubygems", "rails", "javascript", "jquery", "jqueryui", "jquerym", "backbone", "marionette", "meteor", "sproutcore", "moo", "prototype", "bootstrap", "foundation", "lodash", "underscore", "ember", "sencha", "extjs", "knockout", "zepto", "yui", "d3", "svg", "dojo", "coffee", "nodejs", "express", "chai", "html", "css", "cordova", "phonegap", "unity3d"],
      "(SQL) Rails"           : ["ruby", "rubygems", "rails"],
      "Ruby Haml"             : ["haml"],
      "Sass"                  : ["sass", "compass", "bourbon", "neat", "css"],
      "Scala"                 : ["scala", "akka", "playscala"],
      "Shell-Unix-Generic"    : ["bash", "manpages"],
      "SQL"                   : ["mysql", "sqlite", "psql"],
      "TCL"                   : ["tcl"],
      "YAML"                  : ["yaml"]      
    }

More information on [Dash docsets][2].

## Credits

* Original idea and code by [Vladimir Pouzanov][4]
* Syntax sensitivity added by [Torsten Grust][5]

[1]: http://kapeli.com/dash
[2]: http://kapeli.com/docsets/
[3]: http://kapeli.com/dash_plugins
[4]: http://farcaller.net/
[5]: http://db.inf.uni-tuebingen.de/team/grust/
[6]: http://wbond.net/sublime_packages/package_control

