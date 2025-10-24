document.addEventListener('DOMContentLoaded', () => {
  const rightSection = document.querySelector('.right-section');

  // 페이지 로드 시 슬라이드 인 효과
  rightSection.classList.add('slide-in');

  document.querySelectorAll('nav a').forEach(link => {
    // 새 탭, 외부 링크 제외
    if (link.target === '_blank' || !link.href.startsWith(window.location.origin)) return;

    link.addEventListener('click', e => {
      e.preventDefault();
      const href = link.href;
      if (href === window.location.href) return;

      // 오른쪽 섹션 슬라이드 아웃
      rightSection.classList.remove('slide-in');
      rightSection.classList.add('slide-out');

      // 500ms 뒤 페이지 이동
      setTimeout(() => {
        window.location.href = href;
      }, 500);
    });
  });
});
