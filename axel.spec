#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : axel
Version  : 2.16.1
Release  : 2
URL      : https://github.com/axel-download-accelerator/axel/releases/download/v2.16.1/axel-2.16.1.tar.xz
Source0  : https://github.com/axel-download-accelerator/axel/releases/download/v2.16.1/axel-2.16.1.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: axel-bin
Requires: axel-license
Requires: axel-locales
Requires: axel-man
BuildRequires : pkgconfig(openssl)

%description
# AXEL
#### Axel â Light command line download accelerator for Linux and Unix
* Help this project
* What is Axel?
* Building from source
* Install on macOS with Homebrew
* Building on macOS with Homebrew
* Related projects
* License

%package bin
Summary: bin components for the axel package.
Group: Binaries
Requires: axel-license
Requires: axel-man

%description bin
bin components for the axel package.


%package license
Summary: license components for the axel package.
Group: Default

%description license
license components for the axel package.


%package locales
Summary: locales components for the axel package.
Group: Default

%description locales
locales components for the axel package.


%package man
Summary: man components for the axel package.
Group: Default

%description man
man components for the axel package.


%prep
%setup -q -n axel-2.16.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1533091374
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1533091374
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/axel
cp COPYING %{buildroot}/usr/share/doc/axel/COPYING
%make_install
%find_lang axel

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/axel

%files license
%defattr(-,root,root,-)
/usr/share/doc/axel/COPYING

%files man
%defattr(-,root,root,-)
/usr/share/man/man1/axel.1

%files locales -f axel.lang
%defattr(-,root,root,-)

