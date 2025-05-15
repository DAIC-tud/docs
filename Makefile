check-links:
	npx --yes linkinator https://daic.tudelft.nl/ -r \
		--skip '(.*_print|change-me|login.daic|servicedesk.*|topdesk\.net|wiki\.tudelft\.nl)'\
		--markdown \
		--verbosity error

