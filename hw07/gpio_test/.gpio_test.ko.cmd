cmd_/home/debian/ece497/hw07/gpio_test/gpio_test.ko := ld -EL -r  -T ./scripts/module-common.lds --build-id  -T ./arch/arm/kernel/module.lds -o /home/debian/ece497/hw07/gpio_test/gpio_test.ko /home/debian/ece497/hw07/gpio_test/gpio_test.o /home/debian/ece497/hw07/gpio_test/gpio_test.mod.o