DashDoc provides integration of [Dash][1] into Sublime Text.

## Usage

You can look up the word under the cursor or selected text in Dash using `Ctrl+h`.

## Options

As usual, you will find the associated settings under the *Preferences / Package Settings / DashDoc* menu.  Personal settings should be made in *Settings - User*.

### Syntax sensitivity

DashDoc can be made sensitive to the syntax used in the current view. Dash will then consult the docset that matches the current syntax.  Example: a lookup for `map` in a Haskell buffer will instruct Dash to search in its `haskell` docset, a search for the same word in a Python buffer will consult the `python2` docset instead.  

Enable syntax sensitivity (default `False`):

    "syntax_sensitive": True

If you leave syntax sensitivity disabled, Dash will search all installed docsets.  Syntax sensitivity may then still be used in a one-off fashion: simply look up via `Ctrl-Alt-h`.

### Choosing a Dash docset for a given syntax

For any Sublime Text syntax, DashDoc can search a docset of your choosing. Map entries below are of the form `{ <syntax> : <docset> }`. For `<docset>`, use the lowercase docset prefixes that Dash indicates in its *Preferences / Docsets* pane.

    "syntax_docset_map":
    {
      "ActionScript": "actionscript",
      "C"           : "c",
      "C++"         : "cpp",
      "Clojure"     : "clojure",
      "CSS"         : "css",
      "Erlang"      : "erlang",
      "Groovy"      : "groovy",
      "Haskell"     : "haskell",
      "HTML"        : "html",
      "Java"        : "java7",
      "JavaScript"  : "javascript",
      "Lisp"        : "lisp",
      "Lua"         : "lua",
      "Perl"        : "perl",
      "PHP"         : "php",
      "Python"      : "python2",
      "Rails"       : "rails",
      "Ruby"        : "ruby",
      "Scala"       : "scala",
      "ShellScript" : "manpages",
      "SQL"         : "psql",
      "TCL"         : "tcl"
    }

More information on [Dash docsets][2].

## Credits

* Original idea and code by [Vladimir Pouzanov][3]
* Syntax sensitivity added by [Torsten Grust][4]

[1]: http://itunes.apple.com/us/app/dash-docs-snippets/id458034879?mt=12
[2]: http://kapeli.com/docsets/
[3]: http://farcaller.net/
[4]: http://db.inf.uni-tuebingen.de/team/grust/
