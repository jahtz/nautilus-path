SHELL=/bin/bash
nautilus_path=`which nautilus`
install:
	mkdir -p ~/.local/share/nautilus-python/extensions
	cp nautilus-path.py ~/.local/share/nautilus-python/extensions
	@echo 'Restarting nautilus'
	@${nautilus_path} -q||true # This is due to nautilus -q always returning 255 status which causes makefile to think it failed

uninstall:
	rm ~/.local/share/nautilus-python/extensions/nautilus-path.py
	@echo 'Restarting nautilus'
	@${nautilus_path} -q||true # This is due to nautilus -q always returning 255 status which causes makefile to think it failed