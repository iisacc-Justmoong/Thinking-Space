<a id="single-app-build-contract"></a>

# 단일 앱 빌드 계약

제품은 [워크스페이스 단일 앱 정책](../../build-policy/README.md)를 사용합니다. `build/` 아래에 오직 정통 애플리케이션 번들이 생성됩니다. 테스트와 헬퍼는 일반 실행 파일이며, 런타임 배포 및 패키징은 원위치로 작동합니다. 정통 경로, 플랫폼 전환 및 검증 명령에 대한 정책을 참조하십시오.

배포 보고서는 기본적으로 빌드 출력에 표시하며 별도의 로그 파일을 만들지 않습니다. 보고서 파일이 필요한 경우 배포 도구의 `--log`에 `resources/` 등의 빌드 디렉터리 바깥 경로를 명시합니다. `BUILD_TESTING=ON`이면 보고서 출력 계약을 자동 테스트합니다.

## Clean deployment layout

macOS deployment prints its report to the build console by default and stores
per-bundle locks under `resources/.state/deploy-locks/`. Framework copies retain
runtime binaries and resources without SDK headers or module maps. The
`tests/deploy_layout_test.py` contract checks these behaviors with disposable
resources and does not launch the application.

## QML debug symbols

Standard and compact macOS deployment keep QML `.dSYM` debug-symbol bundles
outside the application while preserving the QML runtime files.

