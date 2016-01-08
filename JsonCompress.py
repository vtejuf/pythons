import json

import sublime, sublime_plugin

class jsoncompressCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        regionAll = sublime.Region( 0, self.view.size() )
        if( not regionAll.empty() ):
            text = self.view.substr(regionAll)
            if(text):
                try:
                    text = json.dumps(json.loads(text), ensure_ascii=False )
                    self.view.replace( edit, regionAll,  text);
                except Exception,e:
                    print Exception,":",e
        print "compress done"