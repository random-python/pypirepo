#!/usr/bin/env python

"""
Squash github commits starting from a point
"""

from devrepo import shell

point = "0458ce54553349ec02da82252956982097cdf9fc"
message = "Develop"

shell(f"git reset --soft {point}")
shell(f"git add --all")
shell(f"git commit --message='{message}'")
shell(f"git push --force --follow-tags")
