#!/usr/bin/env python

import gtk


def scrape_clipboard():
    clipboard = gtk.clipboard_get()
    targets = clipboard.wait_for_targets()

    for target in ["text/html", "UTF8_STRING", "text"]:
        if targets.count(target):
            paste = clipboard.wait_for_contents(target)
            print "found target type:", target
            return paste.data
            
    return None
    

if __name__ == "__main__":
    print scrape_clipboard()
