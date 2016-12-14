# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "webover"
app_title = "Webover"
app_publisher = "MN Technique"
app_description = "App for website makeover"
app_icon = "octicon octicon-file-directory"
app_color = "maroon"
app_email = "support@mntechnique.com"
app_license = "GPL v3"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/webover/css/webover.css"
# app_include_js = "/assets/webover/js/webover.js"

# include js, css files in header of web template
# web_include_css = "/assets/webover/css/webover.css"
# web_include_js = "/assets/webover/js/webover.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "webover.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "webover.install.before_install"
# after_install = "webover.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "webover.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"webover.tasks.all"
# 	],
# 	"daily": [
# 		"webover.tasks.daily"
# 	],
# 	"hourly": [
# 		"webover.tasks.hourly"
# 	],
# 	"weekly": [
# 		"webover.tasks.weekly"
# 	]
# 	"monthly": [
# 		"webover.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "webover.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "webover.event.get_events"
# }

