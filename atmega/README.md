# kagotos/atmega

# Components
- Pro Micro (Arduino Lernardo compatible)
- Motor Driver
- Gear motors and tires

# Requirement

platformIO

# Usage

## Build
```
pio run
```

## Write
```
pio run -t upload
```

## Test
Start communication.
```
pio board monitor -b 115200
```

Full speed.
```
motors 1023 1023
```

Stop.
```
motors 0 0
```

Back with middle speed.
```
motors -500 -500
```

Turn right.
```
motors 100 -100
```

Brake.
```
motors brake brake
```
or
```
motors b b
```

See status
```
status
```

# Setup memo

```
cd [kagotos dir]
mkdir arduino
cd arduino
pio init --board sparkfun_promicro16
```

# License
MIT
