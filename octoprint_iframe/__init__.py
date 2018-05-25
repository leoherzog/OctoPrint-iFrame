# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin

class iFramePlugin(octoprint.plugin.StartupPlugin,
                       octoprint.plugin.TemplatePlugin,
                       octoprint.plugin.SettingsPlugin,
                       octoprint.plugin.AssetPlugin):
	def on_after_startup(self):
		self._logger.info("Set up and ready to go! (Default: %s)" % self._settings.get(["url"]))

	def get_settings_defaults(self):
		return dict(url="https://en.m.wikipedia.org/wiki/Hello_world")

	def get_template_configs(self):
		return [
			dict(type="settings", custom_bindings=False)
		]

	def get_assets(self):
		return dict(
			js=["js/iframe.js"],
			css=["css/iframe.css"],
			less=["less/iframe.less"]
		)

__plugin_name__ = "iFrame"
__plugin_implementation__ = iFramePlugin()
