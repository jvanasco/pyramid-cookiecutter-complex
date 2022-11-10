This directory should not have anything tracked via version control.

Applications can write shared flags to this as needed.

All flags should be documented:

downtime
	- this instructs nginx that we are in downtime and to not serve files
	- managed by:
		* manual
	- checked by:
		* nginx


