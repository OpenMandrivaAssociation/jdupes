Summary:	A fast and powerful cross-platform duplicate file finder
Name:		jdupes
Version:	1.27.3
Release:	1
License:	MIT
Group:		File tools
URL:		https://codeberg.org/jbruchon/jdupes
Source0:	https://codeberg.org/jbruchon/jdupes/archive/v%{version}.tar.gz
Patch0:		0001-hashdb-backport-safety-fixes-from-master.patch

BuildRequires:	jodycode-devel

%description
jdupes is a program for identifying and taking actions upon duplicate
files such as deleting, hard linking, symlinking, and block-level
deduplication (also known as "dedupe" or "reflink"). It is faster than
most other duplicate scanners. It prioritizes data safety over
performance while also giving expert users access to advanced (and
sometimes dangerous) features.

%files
%license LICENSE.txt
%doc CHANGES.txt INSTALL.txt README.md README.stupid_dupes
%{_bindir}/jdupes
%{_mandir}/man1/jdupes.1.*

#-----------------------------------------------------------------------

%prep
%autosetup -p1 -n %{name}

%build
#configure
%setup_compile_flags
%make_build CFLAGS="%{optflags} -DENABLE_DEDUPE -DHARDEN" PREFIX="%{_prefix}" MAN_BASE_DIR="%{_mandir}"


%install
%make_install PREFIX="%{_prefix}" MAN_BASE_DIR="%{_mandir}"

