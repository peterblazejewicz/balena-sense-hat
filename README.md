# balena-sense-hat

Template project for application image running RaspberryPi 4 64Bit with Sense Hat, Python 3.7.* on the Balena 64 bit OS

## Usage

- clone this repository:

```bash
https://github.com/peterblazejewicz/balena-sense-hat.git
```

- add Balena push git remote address of your application:

```bash
git remote add balena [endpoint]
```

- push that project

```bash
git push balena master
```

Initial build:

```bash
           ┌─────────┬────────────┬──────────────────────┐
[Info]     │ Service │ Image Size │ Build Time           │
[Info]     ├─────────┼────────────┼──────────────────────┤
[Info]     │ main    │ 189.68 MB  │ 6 minutes, 8 seconds │
[Info]     └─────────┴────────────┴──────────────────────┘
[Info]     Build finished in 7 minutes, 8 seconds
			    \
			     \
			      \\
			       \\
			        >\/7
			    _.-(6'  \
			   (=___._/` \
			        )  \ |
			       /   / |
			      /    > /
			     j    < _\
			 _.-' :      ``.
			 \ r=._\        `.
			<`\\_  \         .`-.
			 \ r-7  `-. ._  ' .  `\
			  \`,      `-.`7  7)   )
			   \/         \|  \'  / `-._
			              ||    .'
			               \\  (
			                >\  >
			            ,.-' >.'
			           <.'_.''
			             <'

```

Sample of outcome of subsequent builds:

```bash
[Info]     ┌─────────┬────────────┬────────────┐
[Info]     │ Service │ Image Size │ Build Time │
[Info]     ├─────────┼────────────┼────────────┤
[Info]     │ main    │ 189.68 MB  │ 6 seconds  │
[Info]     └─────────┴────────────┴────────────┘
[Info]     Build finished in 38 seconds
```

## Author

@peterblazejewicz
