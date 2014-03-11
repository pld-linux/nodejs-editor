%define		pkg	editor
Summary:	Launch $EDITOR in your program
Name:		nodejs-%{pkg}
Version:	0.0.5
Release:	1
License:	MIT
Group:		Development/Libraries
URL:		https://github.com/substack/node-editor
Source0:	http://registry.npmjs.org/%{pkg}/-/%{pkg}-%{version}.tgz
# Source0-md5:	69cde0a48685690052af4e2578ccf255
BuildRequires:	rpmbuild(macros) >= 1.634
Requires:	nodejs >= 0.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Launch $EDITOR in your program.

%prep
%setup -qc
mv package/* .

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}
cp -pr index.js package.json $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.markdown
%{nodejs_libdir}/%{pkg}
