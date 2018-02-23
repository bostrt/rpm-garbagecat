Summary:	 Parses Java garbage collection logging and provides analysis to support JVM tuning and troubleshooting for OpenJDK and Sun/Oracle JDK.
Name:        garbagecat
Version:     2.0.12
Release:     1
License:     EPL
Group:       Development/Tools
Url:         http://mgm3746.github.io/garbagecat/

Source0:   https://github.com/mgm3746/garbagecat/archive/v%{version}.tar.gz
Source1:   garbagecat

BuildArch: noarch

BuildRequires: java-1.8.0-openjdk-devel
BuildRequires: maven

Requires: java-1.8.0-openjdk-headless

%description
Parses Java garbage collection logging and provides analysis to support JVM
tuning and troubleshooting for OpenJDK and Sun/Oracle JDK. It differs from
other tools in that it goes beyond the simple math of calculating statistics
such as maximum pause time and throughput. It adds context to these numbers by
identifying the associated collector or collector phase, which allows for much
deeper insight and analysis. This is especially relevant to collectors such as
the Concurrent Mark Sweep collector that have multiple concurrent and
stop-the-world phases.

%prep
%setup -q -n %{name}-%{version}

%build
mvn clean assembly:assembly -DskipTests=true

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_libdir}/garbagecat/
cp target/garbagecat-%{version}.jar $RPM_BUILD_ROOT%{_libdir}/garbagecat/garbagecat.jar
install -p -D -m 0755 %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/garbagecat

%files
%defattr(-,root,root)
%{_libdir}/garbagecat/garbagecat.jar
%{_bindir}/garbagecat
%doc README.md

%changelog
* Thu Feb 22 2018 Robert Bost <bostrt@gmail.com> 2.0.12-1
- Version bump. Source update (bostrt@gmail.com)

* Fri Jun 23 2017 Robert Bost <bostrt@gmail.com> 2.0.11-1
- Version bump. Source update. (bostrt@gmail.com)

* Wed Jun 07 2017 Robert Bost <bostrt@gmail.com> 2.0.10-1
- Version bump. Source update. (bostrt@gmail.com)

* Thu May 25 2017 Robert Bost <bostrt@gmail.com> 2.0.9-1
- Version bump. Source update. (bostrt@gmail.com)

* Thu Apr 20 2017 Robert Bost <bostrt@gmail.com> 2.0.8-1
- Version bump. Source update (bostrt@gmail.com)

* Wed Apr 05 2017 Robert Bost <bostrt@gmail.com> 2.0.7-2
- Removed version from .jar. Fixed garbagecat script. (bostrt@gmail.com)

* Wed Apr 05 2017 Robert Bost <bostrt@gmail.com> 2.0.7-1
- Version bump. Source update. (bostrt@gmail.com)
- Automatic commit of package [garbagecat] release [2.0.6-1].
  (bostrt@gmail.com)
- Add build status badge. (bostrt@gmail.com)

* Tue Apr 04 2017 Robert Bost 2.0.6-1
- Version bump. Source update. Slight change in upstream tagging.

* Fri Mar 24 2017 Robert Bost 2.0.5-2
- Add changelog section (bostrt@gmail.com)
