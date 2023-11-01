Name: container-tools
Version: 1
Release: 12%{?dist}
Summary: A meta-package witch container tools such as podman, buildah, skopeo, etc.
License: MIT
BuildArch: noarch
Requires: aardvark-dns
Requires: buildah
Requires: conmon
Requires: (container-selinux >= 2:2.162.1 if selinux-policy)
Requires: containernetworking-plugins
Requires: containers-common
Requires: fuse-overlayfs
Requires: netavark
Requires: podman
Requires: podman-docker
Requires: podman-manpages
Requires: podman-remote
Requires: python3-podman
Requires: oci-runtime
%if 0%{?rhel} >= 9 || 0%{?fedora}
Requires: crun >= 0.19
%else
Requires: runc
%endif
Requires: skopeo
Requires: slirp4netns
Requires: cockpit-podman
Requires: toolbox
Requires: udica
Suggests: oci-seccomp-bpf-hook
Suggests: runc

%description
Latest versions of podman, buildah, skopeo, runc, conmon, CRIU, Udica, etc as
well as dependencies such as container-selinux built and tested together, and
updated.

%package tests
Summary: Test packages for container-tools
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: buildah-tests
Requires: podman-tests
Requires: skopeo-tests

%description tests
This package contains system tests for %{name}.

%prep

%build

%install

%files

%files tests

%changelog
* Thu Jun 30 2022 Jindrich Novy <jnovy@redhat.com> - 1-12
- remove direct podman/buildah/skopeo minimal verison dependencies
- Related: #2061316

* Mon May 16 2022 Jindrich Novy <jnovy@redhat.com> - 1-11
- rebuild for 9.1
- Related: #2061316

* Thu Feb 24 2022 Lokesh Mandvekar <lsm5@redhat.com> - 1-10
- Require netavark and aardvark
- Related: #2000051

* Thu Feb 10 2022 Jindrich Novy <jnovy@redhat.com> - 1-9
- put conditional require in the metapackage
- Related: #2000051

* Tue Feb 08 2022 Jindrich Novy <jnovy@redhat.com> - 1-8
- amend dependencies for container-tools metapackage
- Related: #2000051

* Mon Oct 04 2021 Jindrich Novy <jnovy@redhat.com> - 1-7
- rebuild for https://issues.redhat.com/browse/RHELBLD-7728
- Related: #2000051

* Thu Sep 30 2021 Jindrich Novy <jnovy@redhat.com> - 1-6
- perform only sanity/installability tests for metapackage
- Related: #2000051

* Thu Sep 30 2021 Jindrich Novy <jnovy@redhat.com> - 1-5
- modify gating.yaml according to the development guide
- Related: #2000051

* Wed Sep 29 2021 Jindrich Novy <jnovy@redhat.com> - 1-4
- add gating.yaml
- Related: #2000051

* Thu Sep 23 2021 Jindrich Novy <jnovy@redhat.com> - 1-3
- fix dependency on podman
- Related: #2000051

* Tue Sep 21 2021 Jindrich Novy <jnovy@redhat.com> - 1-2
- initial import
- Resolves: #2000871
