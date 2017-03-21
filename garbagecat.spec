Summary:	 Parses Java garbage collection logging and provides analysis to support JVM tuning and troubleshooting for OpenJDK and Sun/Oracle JDK.
Name:        garbagecat
Version:     2.0.5
Release:     1
License:     EPL
Group:       Development/Tools
Url:         http://mgm3746.github.io/garbagecat/

Source0:   https://github.com/mgm3746/garbagecat/archive/%{version}.tar.gz
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
cp target/garbagecat-%{version}.jar $RPM_BUILD_ROOT%{_libdir}/garbagecat/
install -p -D -m 0755 %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/garbagecat

%files
%defattr(-,root,root)
%{_libdir}/garbagecat/garbagecat-%{version}.jar
%{_bindir}/garbagecat
%doc README.md
