import os

html_content = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>老马喵务局 · 荣耀 YOYO 智能体 | 发动机全景工程有机拆解大屏</title>
  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      theme: {
        extend: {
          colors: {
            blueprint: {
              50: '#F8FAFC',
              100: '#F1F5F9',
              200: '#E2E8F0',
              300: '#CBD5E1',
              400: '#94A3B8',
              500: '#64748B',
              600: '#475569',
              700: '#334155',
              800: '#1E293B',
              900: '#0F172A',
            }
          },
          fontFamily: {
            mono: ['JetBrains Mono', 'ui-monospace', 'SFMono-Regular', 'Menlo', 'Monaco', 'Consolas', 'monospace'],
            sans: ['-apple-system', 'BlinkMacSystemFont', '"PingFang SC"', '"Hiragino Sans GB"', '"Microsoft YaHei"', 'sans-serif']
          }
        }
      }
    }
  </script>
  <style>
    /* Blueprint dot grid background */
    .bg-blueprint-grid {
      background-color: #F8FAFC;
      background-image: radial-gradient(#CBD5E1 1.2px, transparent 1.2px);
      background-size: 28px 28px;
    }
    
    /* Hardware accelerated canvas */
    #canvas-stage {
      will-change: transform;
      transform-origin: 0 0;
    }

    /* Custom scrollbars */
    ::-webkit-scrollbar {
      width: 6px;
      height: 6px;
    }
    ::-webkit-scrollbar-track {
      background: #F1F5F9;
    }
    ::-webkit-scrollbar-thumb {
      background: #CBD5E1;
      border-radius: 9999px;
    }
    ::-webkit-scrollbar-thumb:hover {
      background: #94A3B8;
    }

    /* Exploded modules */
    .exploded-module {
      transition: box-shadow 0.3s ease, border-color 0.3s ease;
    }

    /* Glow highlights */
    .glow-cyan {
      box-shadow: 0 0 35px -5px rgba(6, 182, 212, 0.22);
    }
    .glow-amber {
      box-shadow: 0 0 35px -5px rgba(245, 158, 11, 0.22);
    }
    .glow-emerald {
      box-shadow: 0 0 35px -5px rgba(16, 185, 129, 0.22);
    }
    .glow-indigo {
      box-shadow: 0 0 35px -5px rgba(99, 102, 241, 0.22);
    }
    .glow-blue {
      box-shadow: 0 0 35px -5px rgba(59, 130, 246, 0.22);
    }
  </style>
</head>
<body class="bg-slate-100 text-slate-800 antialiased overflow-hidden font-sans h-screen w-screen flex flex-col select-none">

  <!-- ========================================================================= -->
  <!-- 顶部悬浮 HUD 控制中心 (Top Minimal Floating HUD) -->
  <!-- ========================================================================= -->
  <header class="fixed top-4 left-6 right-6 z-50 pointer-events-none flex items-center justify-between">
    <!-- Left: Project Brand & Verification Pill -->
    <div class="pointer-events-auto flex items-center gap-3 bg-white/90 backdrop-blur-xl px-4 py-2 rounded-2xl border border-slate-200/90 shadow-md">
      <div class="relative w-10 h-10 rounded-xl overflow-hidden shadow-sm ring-1 ring-blue-500/30 bg-slate-900 shrink-0">
        <img src="./assets/app_assets/app_icon_preview.png" alt="老马" class="w-full h-full object-cover">
      </div>
      <div>
        <div class="flex items-center gap-2">
          <h1 class="font-black text-slate-900 text-sm tracking-tight">老马喵务局</h1>
          <span class="text-[10px] px-2 py-0.5 rounded-md bg-blue-50 text-blue-600 font-bold border border-blue-200/60 font-mono">荣耀 YOYO 智能体</span>
          <span class="text-[10px] px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-700 font-bold border border-emerald-200/80">全景工程大屏</span>
        </div>
        <p class="text-[10.5px] text-slate-400 font-medium mt-0.5 font-mono">
          SINGLE MASTER CANVAS · 发动机有机拆解 · 100% 正版素材
        </p>
      </div>
    </div>

    <!-- Center: Exploded Rate Slider & Leader Lines Toggle -->
    <div class="pointer-events-auto flex items-center gap-3 bg-white/90 backdrop-blur-xl px-4 py-2 rounded-2xl border border-slate-200/90 shadow-md">
      <!-- Explosion Slider -->
      <div class="flex items-center gap-2">
        <span class="text-xs font-black text-slate-700 flex items-center gap-1">
          <span>⚙️ 拆解幅度:</span>
        </span>
        <input type="range" id="explode-slider" min="0" max="100" value="80" class="w-28 accent-blue-600 cursor-pointer" oninput="updateExplosion(this.value)">
        <span id="explode-val" class="font-mono text-xs font-black text-blue-600 w-8 text-right">80%</span>
      </div>

      <div class="w-px h-4 bg-slate-200"></div>

      <!-- State Switcher -->
      <div class="flex items-center gap-1 bg-slate-100 p-1 rounded-xl">
        <button onclick="setGlobalCatState('normal')" id="btn-state-normal" class="px-2.5 py-1 rounded-lg text-[11px] font-black transition-all bg-emerald-500 text-white shadow-2xs flex items-center gap-1">
          <span class="w-1.5 h-1.5 rounded-full bg-white animate-pulse"></span>
          <span>健康态</span>
        </button>
        <button onclick="setGlobalCatState('dirty')" id="btn-state-dirty" class="px-2.5 py-1 rounded-lg text-[11px] font-black transition-all text-slate-600 hover:bg-slate-200 flex items-center gap-1">
          <span class="w-1.5 h-1.5 rounded-full bg-amber-500"></span>
          <span>脏污态</span>
        </button>
        <button onclick="setGlobalCatState('touch')" id="btn-state-touch" class="px-2.5 py-1 rounded-lg text-[11px] font-black transition-all text-slate-600 hover:bg-slate-200 flex items-center gap-1">
          <span class="w-1.5 h-1.5 rounded-full bg-rose-500"></span>
          <span>抚摸态</span>
        </button>
      </div>

      <div class="w-px h-4 bg-slate-200"></div>

      <!-- Toggle Lines -->
      <button id="toggle-lines-btn" onclick="toggleLeaderLines()" class="px-2.5 py-1 rounded-xl bg-blue-50 text-blue-700 hover:bg-blue-100 text-[11px] font-bold border border-blue-200 transition-all flex items-center gap-1">
        <span>🔗</span> 导线开
      </button>
    </div>

    <!-- Right: Zoom & Reset Canvas -->
    <div class="pointer-events-auto flex items-center gap-2 bg-white/90 backdrop-blur-xl px-3 py-2 rounded-2xl border border-slate-200/90 shadow-md">
      <span class="text-xs font-mono font-black text-slate-700">ZOOM: <span id="hud-zoom" class="text-blue-600">85%</span></span>
      <button onclick="zoomStep(1.15)" class="w-6 h-6 rounded-lg bg-slate-100 hover:bg-slate-200 flex items-center justify-center font-mono font-bold text-xs">＋</button>
      <button onclick="zoomStep(0.85)" class="w-6 h-6 rounded-lg bg-slate-100 hover:bg-slate-200 flex items-center justify-center font-mono font-bold text-xs">－</button>
      <button onclick="resetCanvasTransform()" class="px-2 py-1 rounded-lg bg-slate-100 hover:bg-slate-200 text-xs font-bold text-slate-700 ml-1">复位</button>
    </div>
  </header>

  <!-- ========================================================================= -->
  <!-- 底部快速视窗锚点导航胶囊 (Bottom Zone Navigation Dock) -->
  <!-- ========================================================================= -->
  <nav class="fixed bottom-6 left-1/2 -translate-x-1/2 z-50 pointer-events-auto flex items-center gap-2 bg-white/90 backdrop-blur-2xl px-4 py-2 rounded-2xl border border-slate-200 shadow-xl">
    <span class="text-[11px] font-bold text-slate-400 mr-1 flex items-center gap-1">
      <span>🧭 视窗直达:</span>
    </span>
    <button onclick="focusZone('center')" class="px-3 py-1.5 rounded-xl text-xs font-black text-slate-700 hover:bg-blue-50 hover:text-blue-600 transition-all flex items-center gap-1.5 border border-transparent hover:border-blue-200">
      <span>⚙️ 发动机拆解核心</span>
    </button>
    <button onclick="focusZone('screens')" class="px-3 py-1.5 rounded-xl text-xs font-black text-slate-700 hover:bg-blue-50 hover:text-blue-600 transition-all flex items-center gap-1.5 border border-transparent hover:border-blue-200">
      <span>📱 真机8大运行截图</span>
    </button>
    <button onclick="focusZone('team')" class="px-3 py-1.5 rounded-xl text-xs font-black text-slate-700 hover:bg-blue-50 hover:text-blue-600 transition-all flex items-center gap-1.5 border border-transparent hover:border-blue-200">
      <span>👥 真实研创14人图谱</span>
    </button>
    <button onclick="focusZone('bom')" class="px-3 py-1.5 rounded-xl text-xs font-black text-slate-700 hover:bg-blue-50 hover:text-blue-600 transition-all flex items-center gap-1.5 border border-transparent hover:border-blue-200">
      <span>📦 全量物料清单墙</span>
    </button>
    <button onclick="focusZone('north')" class="px-3 py-1.5 rounded-xl text-xs font-black text-slate-700 hover:bg-blue-50 hover:text-blue-600 transition-all flex items-center gap-1.5 border border-transparent hover:border-blue-200">
      <span>📜 选题架构与状态机</span>
    </button>
  </nav>

  <!-- ========================================================================= -->
  <!-- 左下角触控板手势操作提示 (Trackpad Guide Badge) -->
  <!-- ========================================================================= -->
  <div class="fixed bottom-6 left-6 z-40 pointer-events-none bg-white/85 backdrop-blur-md px-3.5 py-2 rounded-xl border border-slate-200/80 shadow-sm flex items-center gap-2 text-[11px] text-slate-500 font-medium">
    <span class="w-2 h-2 rounded-full bg-emerald-500"></span>
    <span><b>Mac 触摸板原生支持</b>：双指任意方向滑动平移 · 双指捏合自由放大/缩小</span>
  </div>

  <!-- ========================================================================= -->
  <!-- 无限漫游主画布容器 (The Master Infinite Blueprint Canvas) -->
  <!-- ========================================================================= -->
  <main id="canvas-viewport" class="w-full h-full relative overflow-hidden bg-blueprint-grid cursor-grab active:cursor-grabbing">
    
    <!-- Giant Stage Layer: 5600px × 4200px (All Zones Arranged Organically) -->
    <div id="canvas-stage" class="absolute pointer-events-auto" style="width: 5600px; height: 4200px;">
      
      <!-- Dynamic SVG Leader Lines Layer -->
      <svg id="svg-leader-lines" class="absolute inset-0 w-full h-full pointer-events-none z-10" xmlns="http://www.w3.org/2000/svg">
        <!-- Connecting paths rendered via JS -->
      </svg>

      <!-- ===================================================================== -->
      <!-- ZONE NORTH (顶部总成 · Y: 350) · 选题背景、开发历程与 FSM 状态机拓扑 -->
      <!-- ===================================================================== -->
      <div id="zone-north" class="absolute z-20 bg-white/95 backdrop-blur-md p-8 rounded-3xl border border-slate-300/80 shadow-xl" style="left: 1700px; top: 380px; width: 2200px;">
        <!-- Header -->
        <div class="flex items-center justify-between border-b border-slate-200 pb-4 mb-6">
          <div class="flex items-center gap-3">
            <span class="w-10 h-10 rounded-2xl bg-blue-50 border border-blue-200 flex items-center justify-center text-xl">📜</span>
            <div>
              <h2 class="text-lg font-black text-slate-900 tracking-tight">荣耀 YOYO 智能体 · 选题开发历程与端侧双向感知通信拓扑</h2>
              <span class="text-xs font-mono text-blue-600 font-bold">[SYS-ARCH-000 · FINITE STATE MACHINE & HYBRID CONTAINER ARCHITECTURE]</span>
            </div>
          </div>
          <div class="flex items-center gap-2">
            <span class="text-xs font-mono text-slate-400">参赛作品权威开发档案</span>
            <span class="text-xs px-2.5 py-1 rounded-full bg-emerald-50 text-emerald-700 font-bold border border-emerald-200">已部署验证</span>
          </div>
        </div>

        <!-- 3 Milestone Cards & Architecture Pipeline -->
        <div class="grid grid-cols-4 gap-6 mb-6">
          <div class="p-5 rounded-2xl bg-slate-50 border border-slate-200">
            <span class="text-xs font-mono font-black text-blue-600">MILESTONE 01</span>
            <h4 class="text-sm font-black text-slate-800 mt-1 mb-2">团宠数字化立项</h4>
            <p class="text-xs text-slate-500 leading-relaxed">
              将真实蓝眼布偶猫“老马”数字化，深度融合荣耀 MagicOS 空间感知，让手机成为猫咪智能伴侣的端侧总舵。
            </p>
          </div>

          <div class="p-5 rounded-2xl bg-slate-50 border border-slate-200 border-l-4 border-l-amber-500">
            <span class="text-xs font-mono font-black text-amber-600">MILESTONE 02</span>
            <h4 class="text-sm font-black text-slate-800 mt-1 mb-2">架构统一 · 摒弃重构</h4>
            <p class="text-xs text-slate-500 leading-relaxed">
              团队在探索中摒弃失败的重构版本，将历经数万次真机验证的混合容器作为绝对生产基石，彻底保障手势物理平滑。
            </p>
          </div>

          <div class="p-5 rounded-2xl bg-slate-50 border border-slate-200 border-l-4 border-l-emerald-500">
            <span class="text-xs font-mono font-black text-emerald-600">MILESTONE 03</span>
            <h4 class="text-sm font-black text-slate-800 mt-1 mb-2">端云协同与飞书生态闭环</h4>
            <p class="text-xs text-slate-500 leading-relaxed">
              YOYO 端侧空间感知触发异常，实时调度高德地图生活服务，并由自动化 Bot 将交接清单同步至飞书老马群。
            </p>
          </div>

          <div class="p-5 rounded-2xl bg-slate-50 border border-slate-200 border-l-4 border-l-indigo-500">
            <span class="text-xs font-mono font-black text-indigo-600">MILESTONE 04</span>
            <h4 class="text-sm font-black text-slate-800 mt-1 mb-2">选题答辩与工程全景展开</h4>
            <p class="text-xs text-slate-500 leading-relaxed">
              向评审委员会以“发动机式有机爆炸图”全量展示 100% 真实资产、14 人研发名册与 8 大真机运行工况。
            </p>
          </div>
        </div>

        <!-- FSM Diagram Topology Strip -->
        <div class="p-4 rounded-2xl bg-slate-100/80 border border-slate-200 font-mono text-xs flex items-center justify-between">
          <div class="flex items-center gap-2">
            <span class="px-2 py-0.5 rounded bg-emerald-100 text-emerald-800 font-bold">STATE: NORMAL</span>
            <span class="text-slate-400">↔ (污垢传感器 / 8h未进食) ↔</span>
            <span class="px-2 py-0.5 rounded bg-amber-100 text-amber-800 font-bold">STATE: DIRTY</span>
            <span class="text-slate-400">↔ (屏幕手势轻抚 / 呼噜音频) ↔</span>
            <span class="px-2 py-0.5 rounded bg-rose-100 text-rose-800 font-bold">STATE: TOUCH</span>
          </div>
          <div class="text-slate-500 text-[11px]">
            <span>端侧心跳采样: 1000ms</span> | <span>混合手势惯性衰减率: 0.94</span>
          </div>
        </div>
      </div>

      <!-- ===================================================================== -->
      <!-- ZONE CENTER (中央整机装配体与发动机有机拆解核心 · Y: 1550) -->
      <!-- ===================================================================== -->

      <!-- 1. 中央整机装配体 (The Central Core: Honor Native Phone) -->
      <div id="core-device-frame" class="absolute z-30" style="left: 2605px; top: 1550px; width: 390px; height: 844px;">
        <div class="absolute -top-7 left-0 right-0 flex items-center justify-between font-mono text-[10px] text-blue-600 font-bold pointer-events-none px-1">
          <span>[CORE-ASM-000] 整机中央总成</span>
          <span>HONOR MAGIC NATIVE · 390 × 844</span>
        </div>

        <!-- Realistic Phone Outer Shell -->
        <div class="relative w-full h-full rounded-[48px] bg-slate-900 p-3 shadow-2xl ring-1 ring-slate-800 ring-offset-4 ring-offset-slate-200">
          <div class="relative w-full h-full rounded-[40px] overflow-hidden bg-white flex flex-col border border-slate-700 shadow-inner">
            
            <!-- Dynamic Pill / Camera Notch -->
            <div class="absolute top-2.5 left-1/2 -translate-x-1/2 w-28 h-6 bg-black rounded-full z-50 flex items-center justify-between px-2 text-[10px] text-white">
              <div class="flex items-center gap-1">
                <span class="w-2 h-2 rounded-full bg-blue-500 animate-pulse"></span>
                <span class="text-[8.5px] font-mono font-bold text-blue-300">YOYO</span>
              </div>
              <span class="w-2 h-2 rounded-full bg-slate-800 ring-1 ring-slate-700"></span>
            </div>

            <!-- Phone Screen Content -->
            <div class="relative w-full h-full flex flex-col bg-[#F8FAFC] overflow-hidden select-none">
              
              <!-- Top HUD -->
              <div class="pt-9 px-4 pb-2 flex items-center justify-between z-20 shrink-0">
                <div class="flex items-center gap-2">
                  <span class="font-black text-slate-900 text-sm tracking-tight">老马喵务局</span>
                  <div id="phone-state-badge" class="flex items-center gap-1 px-2 py-0.5 rounded-full bg-emerald-100 text-emerald-800 text-[10px] font-bold">
                    <span class="w-1.5 h-1.5 rounded-full bg-emerald-500"></span>
                    <span id="phone-state-text">精神不错</span>
                  </div>
                </div>
                <div class="flex items-center gap-1.5 font-mono text-xs font-bold text-slate-700">
                  <span>今日照护 <span id="phone-care-ratio" class="text-blue-600">3/5</span></span>
                </div>
              </div>

              <!-- Live Cat Video Player -->
              <div class="relative w-full h-[360px] overflow-hidden bg-slate-200 shrink-0">
                <img id="phone-bg-img" src="./assets/app_assets/home_bg_clean.png" class="absolute inset-0 w-full h-full object-cover" alt="背景">
                <video id="phone-cat-video" src="./assets/app_assets/home_cat_clean.mp4" autoplay loop muted playsinline class="absolute inset-0 w-full h-full object-contain z-10"></video>
                <div class="absolute bottom-3 right-3 z-20 bg-black/40 backdrop-blur-md px-2.5 py-1 rounded-full text-[10px] text-white font-bold flex items-center gap-1">
                  <span>🐾</span> 实时工况循环
                </div>
              </div>

              <!-- Docked Timeline Event Preview -->
              <div class="px-4 py-2 z-20">
                <div class="bg-white/90 backdrop-blur-md rounded-2xl p-3 border border-slate-200/80 shadow-xs flex items-center gap-3">
                  <div class="w-10 h-10 rounded-xl bg-blue-50 border border-blue-100 flex items-center justify-center p-1.5 shrink-0">
                    <img id="phone-active-icon" src="./assets/app_assets/ic_board_brush.png" class="w-full h-full object-contain" alt="事件">
                  </div>
                  <div class="flex-1 min-w-0">
                    <div class="flex items-center justify-between">
                      <span id="phone-active-title" class="text-xs font-black text-slate-800 truncate">全身梳毛</span>
                      <span id="phone-active-time" class="text-[10px] font-mono text-slate-400 font-bold">09:15</span>
                    </div>
                    <p id="phone-active-desc" class="text-[10.5px] text-slate-500 truncate mt-0.5">使用软针气垫梳整理背部浮毛，检查光泽...</p>
                  </div>
                </div>
              </div>

              <!-- Bottom Bento Buttons -->
              <div class="mt-auto px-4 pb-4 z-20">
                <div class="grid grid-cols-2 gap-2">
                  <div class="bg-white/90 backdrop-blur-md rounded-2xl p-3 border border-slate-200 shadow-xs flex items-center gap-2.5">
                    <img src="./assets/app_assets/ui_icons/ic_btn_trophy.png" class="w-7 h-7 object-contain" alt="榜单">
                    <div>
                      <div class="text-xs font-black text-slate-800">爱喵排行榜</div>
                      <div class="text-[9px] text-slate-400">守护贡献榜单</div>
                    </div>
                  </div>
                  <div class="bg-white/90 backdrop-blur-md rounded-2xl p-3 border border-slate-200 shadow-xs flex items-center gap-2.5">
                    <img src="./assets/app_assets/ic_tile_journal.png" class="w-7 h-7 object-contain" alt="档案">
                    <div>
                      <div class="text-xs font-black text-slate-800">老马档案馆</div>
                      <div class="text-[9px] text-slate-400">珍藏生活与回忆</div>
                    </div>
                  </div>
                </div>
              </div>

            </div>
          </div>
        </div>
      </div>

      <!-- 2. 发动机环绕总成 01 (左上) · 状态感知仪表组 -->
      <div id="module-gauges" class="exploded-module absolute z-20 bg-white/95 backdrop-blur-md p-5 rounded-3xl border border-cyan-200/80 shadow-xl glow-cyan cursor-pointer" style="left: 1980px; top: 1120px; width: 520px;" onclick="inspectComponent('gauges')">
        <div class="flex items-center justify-between border-b border-slate-100 pb-3 mb-4">
          <div class="flex items-center gap-2.5">
            <span class="w-8 h-8 rounded-xl bg-cyan-50 border border-cyan-200 flex items-center justify-center text-base">📊</span>
            <div>
              <h3 class="font-black text-slate-900 text-sm">状态感知与生命指标仪表总成</h3>
              <span class="text-[10px] font-mono text-cyan-600 font-bold">[ASM-01 · SENSORS & GAUGES CLUSTER]</span>
            </div>
          </div>
          <span class="text-[10px] px-2 py-0.5 rounded-full bg-cyan-50 text-cyan-700 font-mono font-bold">5 UNITS</span>
        </div>

        <div class="grid grid-cols-2 gap-3">
          <div class="p-3 rounded-2xl bg-slate-50 border border-slate-200/80 hover:border-cyan-400 transition-all cursor-pointer" onclick="event.stopPropagation(); inspectComponent('gauge_love')">
            <div class="flex items-center gap-2 mb-1.5">
              <img src="./assets/app_assets/ui_icons/ic_index_catlove.png" class="w-6 h-6 object-contain" alt="爱猫指数">
              <span class="text-xs font-bold text-slate-700">爱猫指数加权</span>
            </div>
            <div class="flex items-baseline justify-between">
              <span class="text-2xl font-black text-rose-500 font-mono">86<span class="text-xs font-normal text-slate-400 ml-1">分</span></span>
              <span class="text-[10px] text-emerald-600 font-bold bg-emerald-50 px-1.5 py-0.2 rounded">+4.2% 本周</span>
            </div>
          </div>

          <div class="p-3 rounded-2xl bg-slate-50 border border-slate-200/80 hover:border-cyan-400 transition-all cursor-pointer" onclick="event.stopPropagation(); inspectComponent('gauge_happiness')">
            <div class="flex items-center gap-2 mb-1.5">
              <img src="./assets/app_assets/ui_icons/ic_index_happiness.png" class="w-6 h-6 object-contain" alt="快乐值">
              <span class="text-xs font-bold text-slate-700">老马快乐指数</span>
            </div>
            <div class="flex items-baseline justify-between">
              <span class="text-2xl font-black text-amber-500 font-mono">98<span class="text-xs font-normal text-slate-400 ml-1">分</span></span>
              <span class="text-[10px] text-amber-600 font-bold bg-amber-50 px-1.5 py-0.2 rounded">极度愉悦</span>
            </div>
          </div>

          <div class="p-3 rounded-2xl bg-slate-50 border border-slate-200/80 hover:border-cyan-400 transition-all cursor-pointer" onclick="event.stopPropagation(); inspectComponent('gauge_green')">
            <div class="flex items-center gap-2 mb-1.5">
              <img src="./assets/app_assets/ui_icons/ic_index_happiness_green.png" class="w-6 h-6 object-contain" alt="健康状态">
              <span class="text-xs font-bold text-slate-700">精神活力态</span>
            </div>
            <div class="flex items-baseline justify-between">
              <span class="text-2xl font-black text-emerald-600 font-mono">100%</span>
              <span class="text-[10px] text-slate-400 font-mono">STABLE</span>
            </div>
          </div>

          <div class="p-3 rounded-2xl bg-slate-50 border border-slate-200/80 hover:border-cyan-400 transition-all cursor-pointer" onclick="event.stopPropagation(); inspectComponent('gauge_orange')">
            <div class="flex items-center gap-2 mb-1.5">
              <img src="./assets/app_assets/ui_icons/ic_index_happiness_orange.png" class="w-6 h-6 object-contain" alt="轻度预警">
              <span class="text-xs font-bold text-slate-700">饥饿脏污预警</span>
            </div>
            <div class="flex items-baseline justify-between">
              <span class="text-2xl font-black text-amber-500 font-mono">42<span class="text-xs font-normal text-slate-400 ml-1">分</span></span>
              <span class="text-[10px] text-amber-600 font-bold bg-amber-50 px-1.5 py-0.2 rounded">需要清洁</span>
            </div>
          </div>
        </div>

        <div class="mt-3 pt-2.5 border-t border-slate-100 flex items-center justify-between text-[10px] text-slate-500 font-mono">
          <span>端侧心跳采样: 1000ms</span>
          <span class="text-cyan-600 font-bold">直连中央整机 HUD</span>
        </div>
      </div>

      <!-- 3. 发动机环绕总成 02 (右上) · 视觉多媒体内核总成 -->
      <div id="module-media" class="exploded-module absolute z-20 bg-white/95 backdrop-blur-md p-5 rounded-3xl border border-emerald-200/80 shadow-xl glow-emerald cursor-pointer" style="left: 3120px; top: 1120px; width: 540px;" onclick="inspectComponent('media')">
        <div class="flex items-center justify-between border-b border-slate-100 pb-3 mb-4">
          <div class="flex items-center gap-2.5">
            <span class="w-8 h-8 rounded-xl bg-emerald-50 border border-emerald-200 flex items-center justify-center text-base">🎬</span>
            <div>
              <h3 class="font-black text-slate-900 text-sm">视觉多媒体内核与工况视频总成</h3>
              <span class="text-[10px] font-mono text-emerald-600 font-bold">[ASM-02 · MULTIMEDIA VIDEO & SPRITE ENGINE]</span>
            </div>
          </div>
          <span class="text-[10px] px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-700 font-mono font-bold">3 CLIPS + 5 SPRITES</span>
        </div>

        <div class="grid grid-cols-3 gap-2.5 mb-3">
          <div class="p-2 rounded-2xl bg-slate-50 border border-slate-200 hover:border-emerald-500 transition-all cursor-pointer flex flex-col" onclick="event.stopPropagation(); setGlobalCatState('normal')">
            <div class="relative w-full h-28 rounded-xl overflow-hidden bg-black mb-2">
              <video src="./assets/app_assets/home_cat_clean.mp4" autoplay loop muted playsinline class="w-full h-full object-cover"></video>
              <span class="absolute top-1 left-1 px-1.5 py-0.5 rounded bg-emerald-500/80 text-[8px] text-white font-mono font-bold">01 活力健康</span>
            </div>
            <span class="text-[11px] font-black text-slate-800 truncate">home_cat_clean</span>
            <span class="text-[9px] text-slate-400 font-mono">1080x1920 · 60fps</span>
          </div>

          <div class="p-2 rounded-2xl bg-slate-50 border border-slate-200 hover:border-amber-500 transition-all cursor-pointer flex flex-col" onclick="event.stopPropagation(); setGlobalCatState('dirty')">
            <div class="relative w-full h-28 rounded-xl overflow-hidden bg-black mb-2">
              <video src="./assets/app_assets/home_cat_dirty.mp4" autoplay loop muted playsinline class="w-full h-full object-cover"></video>
              <span class="absolute top-1 left-1 px-1.5 py-0.5 rounded bg-amber-500/80 text-[8px] text-white font-mono font-bold">02 饥饿脏污</span>
            </div>
            <span class="text-[11px] font-black text-slate-800 truncate">home_cat_dirty</span>
            <span class="text-[9px] text-slate-400 font-mono">1080x1920 · 60fps</span>
          </div>

          <div class="p-2 rounded-2xl bg-slate-50 border border-slate-200 hover:border-rose-500 transition-all cursor-pointer flex flex-col" onclick="event.stopPropagation(); setGlobalCatState('touch')">
            <div class="relative w-full h-28 rounded-xl overflow-hidden bg-black mb-2">
              <video src="./assets/app_assets/home_cat_touch.mp4" autoplay loop muted playsinline class="w-full h-full object-cover"></video>
              <span class="absolute top-1 left-1 px-1.5 py-0.5 rounded bg-rose-500/80 text-[8px] text-white font-mono font-bold">03 抚摸互动</span>
            </div>
            <span class="text-[11px] font-black text-slate-800 truncate">home_cat_touch</span>
            <span class="text-[9px] text-slate-400 font-mono">1080x1920 · 60fps</span>
          </div>
        </div>

        <div class="p-2.5 rounded-2xl bg-slate-50 border border-slate-200 flex items-center justify-between">
          <div class="flex items-center gap-3">
            <div class="w-12 h-12 rounded-xl bg-white border border-slate-200 p-1 flex items-center justify-center">
              <img src="./assets/app_assets/hero_cat_sitting_tight.png" class="w-full h-full object-contain" alt="老马">
            </div>
            <div class="w-12 h-12 rounded-xl bg-white border border-slate-200 p-1 flex items-center justify-center">
              <img src="./assets/app_assets/hero_cat_carrier_tight.png" class="w-full h-full object-contain" alt="航空箱">
            </div>
            <div>
              <div class="text-xs font-bold text-slate-800">老马高清透明剪影贴纸</div>
              <div class="text-[9.5px] text-slate-400">高精度 Alpha 通道免抠图层</div>
            </div>
          </div>
          <span class="text-[10px] font-mono text-emerald-600 font-bold bg-emerald-50 px-2 py-1 rounded-lg">PNG 300DPI</span>
        </div>
      </div>

      <!-- 4. 发动机环绕总成 03 (左侧) · 24H 空间感知时间轴与 11 道具物料 -->
      <div id="module-timeline" class="exploded-module absolute z-20 bg-white/95 backdrop-blur-md p-5 rounded-3xl border border-indigo-200/80 shadow-xl glow-indigo cursor-pointer" style="left: 1840px; top: 1580px; width: 660px;" onclick="inspectComponent('timeline')">
        <div class="flex items-center justify-between border-b border-slate-100 pb-3 mb-3">
          <div class="flex items-center gap-2.5">
            <span class="w-8 h-8 rounded-xl bg-indigo-50 border border-indigo-200 flex items-center justify-center text-base">⏳</span>
            <div>
              <h3 class="font-black text-slate-900 text-sm">24H 空间感知时间轴总成 (11大道具零部件)</h3>
              <span class="text-[10px] font-mono text-indigo-600 font-bold">[ASM-03 · 24H SPATIAL TIMELINE & 11 BOARD ITEMS]</span>
            </div>
          </div>
          <span class="text-[10px] px-2.5 py-0.5 rounded-full bg-indigo-50 text-indigo-700 font-mono font-bold">11 ITEMS ALL EXPANDED</span>
        </div>

        <div id="timeline-scroll-list" class="space-y-2 max-h-[720px] overflow-y-auto pr-2">
          <!-- 11 items rendered via JS -->
        </div>
      </div>

      <!-- 5. 发动机环绕总成 04 (右侧) · 双梯形 Bento 交互机能矩阵 -->
      <div id="module-bento" class="exploded-module absolute z-20 bg-white/95 backdrop-blur-md p-5 rounded-3xl border border-amber-200/80 shadow-xl glow-amber cursor-pointer" style="left: 3120px; top: 1580px; width: 560px;" onclick="inspectComponent('bento')">
        <div class="flex items-center justify-between border-b border-slate-100 pb-3 mb-4">
          <div class="flex items-center gap-2.5">
            <span class="w-8 h-8 rounded-xl bg-amber-50 border border-amber-200 flex items-center justify-center text-base">🍱</span>
            <div>
              <h3 class="font-black text-slate-900 text-sm">双梯形 Bento 交互机能矩阵</h3>
              <span class="text-[10px] font-mono text-amber-600 font-bold">[ASM-04 · DUAL TRAPEZOID INTERACTIVE HUB]</span>
            </div>
          </div>
          <span class="text-[10px] px-2 py-0.5 rounded-full bg-amber-50 text-amber-700 font-mono font-bold">10.3° 倾角微几何</span>
        </div>

        <div class="grid grid-cols-2 gap-4 mb-4">
          <!-- Left Trapezoid -->
          <div class="p-3.5 rounded-2xl bg-slate-50 border border-slate-200 flex flex-col justify-between">
            <div class="flex items-center gap-2 mb-2">
              <img src="./assets/app_assets/ui_icons/ic_btn_trophy.png" class="w-6 h-6 object-contain" alt="奖杯">
              <div>
                <div class="text-xs font-black text-slate-800">左梯形 · 爱喵排行榜</div>
                <div class="text-[9px] text-slate-400 font-mono">顶窄 124px / 底宽 160px</div>
              </div>
            </div>

            <div class="relative w-full h-24 my-2 flex items-end justify-center">
              <div class="absolute inset-0 flex items-center justify-around z-20">
                <div class="flex flex-col items-center">
                  <img src="./assets/app_assets/avatars/avatar_xiaobai.png" class="w-6 h-6 rounded-full ring-2 ring-slate-200" alt="晓白">
                  <span class="text-[9px] font-bold text-slate-600 mt-0.5">晓白 🥈</span>
                </div>
                <div class="flex flex-col items-center -translate-y-2">
                  <img src="./assets/app_assets/avatars/avatar_lex.png" class="w-8 h-8 rounded-full ring-2 ring-amber-400" alt="Lex">
                  <span class="text-[10px] font-black text-slate-800 mt-0.5">Lex 👑</span>
                </div>
                <div class="flex flex-col items-center">
                  <img src="./assets/app_assets/avatars/avatar_linyi.png" class="w-6 h-6 rounded-full ring-2 ring-amber-700/40" alt="林亦">
                  <span class="text-[9px] font-bold text-slate-600 mt-0.5">林亦 🥉</span>
                </div>
              </div>
              <img src="./assets/app_assets/generated/podium_3d.png" class="w-full h-auto object-contain z-10 opacity-70" alt="领奖台">
            </div>

            <div class="text-[10px] text-slate-500 bg-white p-2 rounded-xl border border-slate-200">
              <span class="font-bold text-emerald-600">林亦加权分: 86分</span> (我的排名第3)
            </div>
          </div>

          <!-- Right Trapezoid -->
          <div class="p-3.5 rounded-2xl bg-slate-50 border border-slate-200 flex flex-col justify-between">
            <div class="flex items-center gap-2 mb-2">
              <img src="./assets/app_assets/ic_tile_journal.png" class="w-6 h-6 object-contain" alt="档案">
              <div>
                <div class="text-xs font-black text-slate-800">右梯形 · 老马档案馆</div>
                <div class="text-[9px] text-slate-400 font-mono">顶宽 160px / 底窄 124px</div>
              </div>
            </div>

            <div class="relative w-full h-24 my-2 flex items-center justify-center bg-white rounded-xl border border-slate-200 p-2 overflow-hidden">
              <img src="./assets/app_assets/hero_cat_sitting_tight.png" class="h-16 object-contain drop-shadow-sm" alt="老马">
              <div class="absolute bottom-1 right-2 px-1.5 py-0.2 rounded bg-amber-500/10 text-amber-700 font-bold text-[8.5px]">
                可自由拖拽贴纸
              </div>
            </div>

            <div class="text-[10px] text-slate-500 bg-white p-2 rounded-xl border border-slate-200">
              <span class="font-bold text-slate-700">珍藏生活与回忆:</span> 7 篇深度手账
            </div>
          </div>
        </div>

        <div class="p-2.5 rounded-xl bg-slate-50 border border-slate-200 text-[10px] font-mono text-slate-600 flex items-center justify-between">
          <span>缝隙间距: 14px (对称贴合)</span>
          <span>圆角半径: R18.0px</span>
          <span>矢量高光: 1.5px 纯白</span>
        </div>
      </div>

      <!-- ===================================================================== -->
      <!-- ZONE EAST (东侧总成 · X: 3780) · 8 张真机高分辨率运行截图全矩阵 -->
      <!-- ===================================================================== -->
      <div id="zone-screens" class="absolute z-20 bg-white/95 backdrop-blur-md p-8 rounded-3xl border border-slate-300/80 shadow-xl" style="left: 3780px; top: 1120px; width: 1680px;">
        <div class="flex items-center justify-between border-b border-slate-200 pb-4 mb-6">
          <div class="flex items-center gap-3">
            <span class="w-10 h-10 rounded-2xl bg-blue-50 border border-blue-200 flex items-center justify-center text-xl">📱</span>
            <div>
              <h2 class="text-lg font-black text-slate-900 tracking-tight">真机设备原生运行截图全矩阵 (8大工况全览)</h2>
              <span class="text-xs font-mono text-blue-600 font-bold">[ZONE-EAST · 8 NATIVE DEVICE SCREENSHOTS · 1320 × 2868]</span>
            </div>
          </div>
          <div class="flex items-center gap-2">
            <span class="text-xs font-mono text-slate-400">来自真机录制真实提取</span>
            <span class="text-xs px-2.5 py-1 rounded-full bg-blue-50 text-blue-700 font-bold border border-blue-200">8 UNITS ALL EXPANDED</span>
          </div>
        </div>

        <!-- 8 Screenshots Grid (2 Rows x 4 Columns) -->
        <div class="grid grid-cols-4 gap-6">
          
          <!-- 1 -->
          <div class="bg-slate-50 rounded-2xl p-3 border border-slate-200">
            <img src="./assets/screenshots/Screenshot_20260919_174540_com_lyi_laomayoyo_MainActivity.JPG" class="w-full h-auto rounded-xl shadow-xs mb-2 cursor-pointer hover:scale-105 transition-transform" alt="截图1" onclick="inspectImage(this.src, '01 首页默认全景装配态 (17:45:40)')">
            <div class="text-xs font-black text-slate-800">01 · 首页主屏 (初始态)</div>
            <div class="text-[10px] text-slate-500 mt-0.5">健康活力工况下老马正坐，左侧吸附 09:14 体检。</div>
          </div>

          <!-- 2 -->
          <div class="bg-slate-50 rounded-2xl p-3 border border-slate-200">
            <img src="./assets/screenshots/Screenshot_20260919_174600_com_lyi_laomayoyo_MainActivity.JPG" class="w-full h-auto rounded-xl shadow-xs mb-2 cursor-pointer hover:scale-105 transition-transform" alt="截图2" onclick="inspectImage(this.src, '02 时间轴卡片展开态 (17:46:00)')">
            <div class="text-xs font-black text-slate-800">02 · 时间轴卡片展开</div>
            <div class="text-[10px] text-slate-500 mt-0.5">向下滑动时间轴触发黑黑全身梳毛卡片平滑展开。</div>
          </div>

          <!-- 3 -->
          <div class="bg-slate-50 rounded-2xl p-3 border border-slate-200">
            <img src="./assets/screenshots/Screenshot_20260919_174613_com_lyi_laomayoyo_MainActivity.JPG" class="w-full h-auto rounded-xl shadow-xs mb-2 cursor-pointer hover:scale-105 transition-transform" alt="截图3" onclick="inspectImage(this.src, '03 抚摸微交互反馈 (17:46:13)')">
            <div class="text-xs font-black text-slate-800">03 · 抚摸微交互反馈</div>
            <div class="text-[10px] text-slate-500 mt-0.5">手指在屏幕中心轻抚老马额头，触发呼噜涟漪。</div>
          </div>

          <!-- 4 -->
          <div class="bg-slate-50 rounded-2xl p-3 border border-slate-200">
            <img src="./assets/screenshots/Screenshot_20260919_174628_com_lyi_laomayoyo_MainActivity.JPG" class="w-full h-auto rounded-xl shadow-xs mb-2 cursor-pointer hover:scale-105 transition-transform" alt="截图4" onclick="inspectImage(this.src, '04 亲密度跃升状态 (17:46:28)')">
            <div class="text-xs font-black text-slate-800">04 · 亲密度跃升状态</div>
            <div class="text-[10px] text-slate-500 mt-0.5">互动后爱猫指数刷新，老马眨动蓝眼恢复平静。</div>
          </div>

          <!-- 5 -->
          <div class="bg-slate-50 rounded-2xl p-3 border border-slate-200">
            <img src="./assets/screenshots/Screenshot_20260919_174648_com_lyi_laomayoyo_MainActivity.JPG" class="w-full h-auto rounded-xl shadow-xs mb-2 cursor-pointer hover:scale-105 transition-transform" alt="截图5" onclick="inspectImage(this.src, '05 饥饿脏污预警工况 (17:46:48)')">
            <div class="text-xs font-black text-slate-800">05 · 饥饿脏污预警工况</div>
            <div class="text-[10px] text-slate-500 mt-0.5">毛发出现灰污斑点，胶囊变橙提示“该洗澡了”。</div>
          </div>

          <!-- 6 -->
          <div class="bg-slate-50 rounded-2xl p-3 border border-slate-200">
            <img src="./assets/screenshots/Screenshot_20260919_174700_com_lyi_laomayoyo_MainActivity.JPG" class="w-full h-auto rounded-xl shadow-xs mb-2 cursor-pointer hover:scale-105 transition-transform" alt="截图6" onclick="inspectImage(this.src, '06 爱喵排行榜全览 (17:47:00)')">
            <div class="text-xs font-black text-slate-800">06 · 爱喵排行榜全览</div>
            <div class="text-[10px] text-slate-500 mt-0.5">点击左梯形平滑展开全员打赏榜，3D金银铜领奖台。</div>
          </div>

          <!-- 7 -->
          <div class="bg-slate-50 rounded-2xl p-3 border border-slate-200">
            <img src="./assets/screenshots/Screenshot_20260919_174713_com_lyi_laomayoyo_MainActivity.JPG" class="w-full h-auto rounded-xl shadow-xs mb-2 cursor-pointer hover:scale-105 transition-transform" alt="截图7" onclick="inspectImage(this.src, '07 老马档案馆时间轴 (17:47:13)')">
            <div class="text-xs font-black text-slate-800">07 · 老马档案馆时间轴</div>
            <div class="text-[10px] text-slate-500 mt-0.5">点击右梯形滑入手账时间流，珍藏生活回忆。</div>
          </div>

          <!-- 8 -->
          <div class="bg-slate-50 rounded-2xl p-3 border border-slate-200">
            <img src="./assets/screenshots/Screenshot_20260919_174724_com_lyi_laomayoyo_MainActivity.JPG" class="w-full h-auto rounded-xl shadow-xs mb-2 cursor-pointer hover:scale-105 transition-transform" alt="截图8" onclick="inspectImage(this.src, '08 手账详情与日志展开 (17:47:24)')">
            <div class="text-xs font-black text-slate-800">08 · 手账详情与日志展开</div>
            <div class="text-[10px] text-slate-500 mt-0.5">手账大图、打卡人头像、日记文本完整自适应。</div>
          </div>

        </div>
      </div>

      <!-- ===================================================================== -->
      <!-- ZONE WEST (西侧总成 · X: 240) · 全量零部件物料清单墙 (Full BOM Asset Wall) -->
      <!-- ===================================================================== -->
      <div id="zone-bom" class="absolute z-20 bg-white/95 backdrop-blur-md p-8 rounded-3xl border border-slate-300/80 shadow-xl" style="left: 240px; top: 1120px; width: 1520px;">
        <div class="flex items-center justify-between border-b border-slate-200 pb-4 mb-6">
          <div class="flex items-center gap-3">
            <span class="w-10 h-10 rounded-2xl bg-indigo-50 border border-indigo-200 flex items-center justify-center text-xl">📦</span>
            <div>
              <h2 class="text-lg font-black text-slate-900 tracking-tight">全量零部件物料清单与数字资产全景墙 (BOM Wall)</h2>
              <span class="text-xs font-mono text-indigo-600 font-bold">[ZONE-WEST · BILL OF MATERIALS & 100% DISCLOSED ASSETS]</span>
            </div>
          </div>
          <span class="text-xs px-2.5 py-1 rounded-full bg-indigo-50 text-indigo-700 font-bold border border-indigo-200">零遗漏真实物料</span>
        </div>

        <!-- 11 Board Items Grid -->
        <div class="mb-6">
          <h3 class="text-xs font-black text-slate-700 font-mono mb-3 uppercase tracking-wider">🔹 11 大手绘 3D 爱猫道具零部件 (/assets/app_assets/ic_board_*.png)</h3>
          <div id="unified-bom-items" class="grid grid-cols-6 gap-3">
            <!-- Rendered via JS -->
          </div>
        </div>

        <!-- UI Icons & Action Buttons -->
        <div class="mb-6">
          <h3 class="text-xs font-black text-slate-700 font-mono mb-3 uppercase tracking-wider">🔹 核心 UI 图标与 3D 渲染模型</h3>
          <div id="unified-bom-icons" class="grid grid-cols-6 gap-3">
            <!-- Rendered via JS -->
          </div>
        </div>

        <!-- 7 Archive Cards -->
        <div>
          <h3 class="text-xs font-black text-slate-700 font-mono mb-3 uppercase tracking-wider">🔹 老马手账卡片 163-169 完整展开</h3>
          <div id="unified-bom-archives" class="grid grid-cols-7 gap-3">
            <!-- Rendered via JS -->
          </div>
        </div>
      </div>

      <!-- ===================================================================== -->
      <!-- ZONE SOUTH (南侧总成 · Y: 2600) · 真实研创 14 人全员图谱与贡献矩阵 -->
      <!-- ===================================================================== -->
      <div id="zone-team" class="absolute z-20 bg-white/95 backdrop-blur-md p-8 rounded-3xl border border-slate-300/80 shadow-xl" style="left: 1700px; top: 2550px; width: 2200px;">
        <div class="flex items-center justify-between border-b border-slate-200 pb-4 mb-6">
          <div class="flex items-center gap-3">
            <span class="w-10 h-10 rounded-2xl bg-blue-50 border border-blue-200 flex items-center justify-center text-xl">👥</span>
            <div>
              <h2 class="text-lg font-black text-slate-900 tracking-tight">14 位真实研创团队全员名册与技术职能矩阵</h2>
              <span class="text-xs font-mono text-blue-600 font-bold">[ZONE-SOUTH · 14 REAL CONTRIBUTORS MAPPING · NO AI FAKE AVATARS]</span>
            </div>
          </div>
          <div class="flex items-center gap-2">
            <span class="text-xs font-mono text-slate-400">规范源: 01_PERSONNEL_MAPPING.md</span>
            <span class="text-xs px-2.5 py-1 rounded-full bg-emerald-50 text-emerald-700 font-bold border border-emerald-200">14/14 真实无虚构</span>
          </div>
        </div>

        <div id="unified-team-grid" class="grid grid-cols-7 gap-4">
          <!-- Rendered via JS -->
        </div>
      </div>

    </div>
  </main>

  <!-- ========================================================================= -->
  <!-- 侧边零部件工程检视抽屉 (Component Inspector Drawer) -->
  <!-- ========================================================================= -->
  <div id="inspector-drawer" class="fixed top-20 right-6 bottom-20 w-[420px] bg-white/95 backdrop-blur-2xl border border-slate-200 shadow-2xl rounded-3xl z-50 transform translate-x-[460px] transition-transform duration-300 flex flex-col overflow-hidden">
    <div class="p-5 border-b border-slate-100 flex items-center justify-between shrink-0">
      <div class="flex items-center gap-2">
        <span class="w-7 h-7 rounded-lg bg-blue-50 border border-blue-200 flex items-center justify-center text-sm">🔬</span>
        <div>
          <h3 class="font-black text-slate-900 text-sm" id="insp-title">零部件物料检视</h3>
          <span class="text-[10px] font-mono text-blue-600 font-bold" id="insp-tag">[ENG-SPEC-000]</span>
        </div>
      </div>
      <button onclick="closeInspector()" class="w-7 h-7 rounded-lg bg-slate-100 hover:bg-slate-200 flex items-center justify-center text-slate-500 text-xs font-bold transition-all">✕</button>
    </div>

    <div class="flex-1 overflow-y-auto p-6 space-y-5">
      <div class="w-full h-44 rounded-2xl bg-slate-50 border border-slate-200 p-3 flex items-center justify-center overflow-hidden">
        <img id="insp-img" src="./assets/app_assets/app_icon_preview.png" class="max-h-full max-w-full object-contain drop-shadow-md" alt="预览">
      </div>

      <div class="space-y-2">
        <h4 class="text-xs font-black text-slate-800 uppercase font-mono tracking-wider">技术物料参数 (Engineering Specs)</h4>
        <div class="bg-slate-50 rounded-2xl p-3.5 border border-slate-200 space-y-2 text-xs">
          <div class="flex items-center justify-between">
            <span class="text-slate-400">物料名称:</span>
            <span class="font-bold text-slate-800" id="insp-name">软针气垫梳部件</span>
          </div>
          <div class="flex items-center justify-between">
            <span class="text-slate-400">文件路径:</span>
            <span class="font-mono text-[10.5px] text-slate-600 truncate max-w-[220px]" id="insp-path">/assets/...</span>
          </div>
          <div class="flex items-center justify-between">
            <span class="text-slate-400">资产类型:</span>
            <span class="font-mono text-blue-600 font-bold" id="insp-type">3D Handcrafted PNG</span>
          </div>
          <div class="flex items-center justify-between">
            <span class="text-slate-400">绑定研发:</span>
            <span class="font-bold text-slate-800" id="insp-author">黑黑 / 阿杰</span>
          </div>
        </div>
      </div>

      <div class="space-y-2">
        <h4 class="text-xs font-black text-slate-800 uppercase font-mono tracking-wider">业务逻辑与官方正版文案</h4>
        <p class="text-xs text-slate-600 leading-relaxed bg-slate-50 p-3.5 rounded-2xl border border-slate-200" id="insp-desc">
          使用软针气垫梳整理背部浮毛，检查颈部毛发光泽；YOYO 同步播报今日进食正常、眼神清澈，养猫指数稳步提升！
        </p>
      </div>
    </div>
  </div>

  <!-- ========================================================================= -->
  <!-- JavaScript: 触控板平滑手势引擎 + 单页无限视窗驱动 -->
  <!-- ========================================================================= -->
  <script>
    // -------------------------------------------------------------------------
    // 1. Data Store
    // -------------------------------------------------------------------------
    const SCHEDULE_DATA = [
      { id: 0, time: '09:14', title: '晨间体检巡视', person: '林亦', avatar: './assets/app_assets/avatars/avatar_linyi.png', icon: './assets/app_assets/ic_board_stethoscope.png', desc: '全面检查老马眼鼻分泌物，检查耳廓与毛发光泽度，称量晨间空腹体重。' },
      { id: 1, time: '09:15', title: '全身梳毛', person: '黑黑', avatar: './assets/app_assets/avatars/avatar_heihei.png', icon: './assets/app_assets/ic_board_brush.png', desc: '使用软针气垫梳整理背部浮毛，检查颈部毛发光泽；YOYO 同步播报今日进食正常、眼神清澈，养猫指数稳步提升！' },
      { id: 2, time: '12:43', title: '严选鸡肉冻干加餐', person: 'Bingo', avatar: './assets/app_assets/avatars/avatar_bingo.png', icon: './assets/app_assets/ic_board_treat.png', desc: '奖励 3 粒原切冻干生骨肉，配合温水复水诱导饮水，进行握爪互动建立信任。' },
      { id: 3, time: '10:30', title: '猫洗澡人洗头协同安排', person: '林亦', avatar: './assets/app_assets/avatars/avatar_linyi.png', icon: './assets/app_assets/ic_board_fountain.png', desc: '去年过年洗过澡，老马钻完机箱全员弹提醒！YOYO 高德协同排班：老马洗澡 150、我剪头 30，下午三点前焕然一新回办公室。' },
      { id: 4, time: '15:46', title: '周末寄养出行交接', person: '木子', avatar: './assets/app_assets/avatars/avatar_muzi.png', icon: './assets/app_assets/ic_board_crate.png', desc: '核对寄养随行物品：益生菌、常备处方罐头与专属抓板，确认航空箱锁扣紧固出行。' },
      { id: 5, time: '15:20', title: '非工作日路过楼下精准陪伴', person: '木子', avatar: './assets/app_assets/avatars/avatar_muzi.png', icon: './assets/app_assets/ic_board_wand.png', desc: 'YOYO 空间感知触发：非工作日经过公司楼下，收到“老马可能无聊了”提醒，APP 里老马敲屏幕急需上楼拿逗猫棒贴贴！' },
      { id: 6, time: '18:30', title: '晚间照料自动交接', person: '荣耀 YOYO', avatar: './assets/app_assets/avatars/avatar_linyi.png', icon: './assets/app_assets/ic_board_feishu_badge.png', desc: 'YOYO 任务准时触发：汇总今日已完成 6 项与待完成 3 项，自动推送交接提醒至飞书老马群。' },
      { id: 7, time: '18:52', title: '三层实木猫爬架巡检', person: 'ImYrS', avatar: './assets/app_assets/avatars/avatar_imyrs.png', icon: './assets/app_assets/ic_board_cat_tree.png', desc: '清理剑麻柱脱落麻屑，擦拭顶层观察台，确认立柱结构稳固无摇晃松动。' },
      { id: 8, time: '20:26', title: '膨润土猫砂深度清理', person: 'Adam', avatar: './assets/app_assets/avatars/avatar_adam.png', icon: './assets/app_assets/ic_board_litter_box.png', desc: '铲除今日结团，补充新鲜无尘矿砂至 8cm 刻度线，开启除臭杀菌喷雾循环。' },
      { id: 9, time: '21:44', title: '渴望全价鲜肉猫粮投喂', person: '小六', avatar: './assets/app_assets/avatars/avatar_xiaoliu.png', icon: './assets/app_assets/ic_board_bowl.png', desc: '清洗陶瓷浅食碗，称量定额干粮投放，记录当日总进食量无异常并记录留档。' },
      { id: 10, time: '23:18', title: '静音恒温猫窝安睡准备', person: 'farest', avatar: './assets/app_assets/avatars/avatar_fangsheng.png', icon: './assets/app_assets/ic_board_cat_bed.png', desc: '巡视门窗关闭，将走廊夜灯调至暖光睡眠模式，确认老马回到休息垫安静入睡。' }
    ];

    const TEAM_MEMBERS = [
      { name: '柯子杰', alias: '阿杰', role: '视觉设计总监', avatar: './assets/app_assets/avatars/avatar_ajie.png', desc: '全套 3D 物品图标、主视觉风格定义、梯形几何切角与质感打造。' },
      { name: '琮宇', alias: 'Howwoy', role: '客户端与原生交互', avatar: './assets/app_assets/avatars/avatar_congyu.png', desc: 'Android WebView 混合容器架设，手势触控与物理惯性回弹驱动。' },
      { name: '方晟', alias: 'farest', role: '智能体系统架构', avatar: './assets/app_assets/avatars/avatar_fangsheng.png', desc: '有限状态机 (FSM) 架构设计、视频工况流转与端云事件总线。' },
      { name: '传鹏', alias: '阿鹏', role: '硬件协同与测试', avatar: './assets/app_assets/avatars/avatar_bingo.png', desc: '智能项圈/传感器联调，硬件环境与端侧信号采集验证。' },
      { name: '张桂滨', alias: 'Gbin', role: '硬件与外设集成', avatar: './assets/app_assets/avatars/avatar_congyu.png', desc: '外设蓝牙广播与低功耗监听，端侧多模态协同实现。' },
      { name: '帅华', alias: '小六', role: '3D / 动效 / 渲染', avatar: './assets/app_assets/avatars/avatar_xiaoliu.png', desc: '3D 奖杯与领奖台建模、光影渲染、手势微反馈粒子动效。' },
      { name: '天鸣', alias: '木子', role: '产品负责人', avatar: './assets/app_assets/avatars/avatar_muzi.png', desc: '产品全功能定义、24H 空间照护旅程制定、老马生活故事线梳理。' },
      { name: '王斌', alias: 'Bingo', role: '核心架构 / AI工程', avatar: './assets/app_assets/avatars/avatar_bingo.png', desc: '荣耀 YOYO 智能体核心接入、本地模型决策网络、全工程技术总舵。' },
      { name: '家源', alias: 'ImYrS', role: '安全 / 测试保障', avatar: './assets/app_assets/avatars/avatar_imyrs.png', desc: '真机自动化测试用例、极限并发压测与安全隐私防护。' },
      { name: '刘旭', alias: 'Lex', role: '后端 / 数据服务', avatar: './assets/app_assets/avatars/avatar_lex.png', desc: '高并发爱猫排行榜加权算法、飞书数据机器人联动与日志同步。' },
      { name: '爱德', alias: 'Adam', role: '交互设计', avatar: './assets/app_assets/avatars/avatar_adam.png', desc: '圆角梯形交互剪裁规范、微纹理混合模式与卡片视差设计。' },
      { name: '黑黑', alias: '黑黑', role: '运营 / 体验测试', avatar: './assets/app_assets/avatars/avatar_heihei.png', desc: '老马真实行为数据沉淀、多场景抚摸实测与用户关爱体验调优。' },
      { name: '嘉浩', alias: '加号', role: '算法工程', avatar: './assets/app_assets/avatars/avatar_jiahao.png', desc: '多模态行为感知模型、猫咪健康状态预测算法工程化。' },
      { name: '栾屹', alias: '林亦', role: '创始人 / 主理人', avatar: './assets/app_assets/avatars/avatar_linyi.png', desc: '老马喵务局立项发起人、全项目资源统筹与参赛战略决策。' }
    ];

    // -------------------------------------------------------------------------
    // 2. Mac Trackpad Native Gestures & Canvas Viewport Engine
    // -------------------------------------------------------------------------
    const viewport = document.getElementById('canvas-viewport');
    const stage = document.getElementById('canvas-stage');
    const hudZoom = document.getElementById('hud-zoom');

    let panX = -1800; // default centered at central phone
    let panY = -1250;
    let zoomScale = 0.85;
    let isMouseDown = false;
    let startMouseX = 0;
    let startMouseY = 0;
    let showLeaderLines = true;
    let explosionRate = 0.8;

    function applyTransform() {
      stage.style.transform = `translate(${panX}px, ${panY}px) scale(${zoomScale})`;
      hudZoom.textContent = `${Math.round(zoomScale * 100)}%`;
      if (showLeaderLines) {
        drawLeaderLines();
      }
    }

    function resetCanvasTransform() {
      focusZone('center');
    }

    function zoomStep(factor) {
      const wCenter = window.innerWidth / 2;
      const hCenter = window.innerHeight / 2;
      const prevScale = zoomScale;
      const nextScale = Math.min(Math.max(0.15, prevScale * factor), 2.5);
      panX = wCenter - (wCenter - panX) * (nextScale / prevScale);
      panY = hCenter - (hCenter - panY) * (nextScale / prevScale);
      zoomScale = nextScale;
      applyTransform();
    }

    // --- Mac Trackpad Wheel Event Listener ---
    // 1. Two-finger scroll (e.ctrlKey === false): Translates/Pans the canvas!
    // 2. Pinch-to-zoom (e.ctrlKey === true): Zooms pivoted at cursor position!
    viewport.addEventListener('wheel', (e) => {
      e.preventDefault();

      if (e.ctrlKey) {
        // macOS Pinch-to-zoom on trackpad!
        const rect = viewport.getBoundingClientRect();
        const cursorX = e.clientX - rect.left;
        const cursorY = e.clientY - rect.top;
        const prevScale = zoomScale;
        // Smooth exponential zoom
        const zoomDelta = -e.deltaY * 0.015;
        const newScale = Math.min(Math.max(0.15, prevScale * Math.exp(zoomDelta)), 2.8);

        panX = cursorX - (cursorX - panX) * (newScale / prevScale);
        panY = cursorY - (cursorY - panY) * (newScale / prevScale);
        zoomScale = newScale;
      } else {
        // macOS Two-finger swipe on trackpad!
        panX -= e.deltaX;
        panY -= e.deltaY;
      }

      applyTransform();
    }, { passive: false });

    // --- Safari Gesture Events for Trackpad Pinch ---
    let gestureStartScale = 1;
    viewport.addEventListener('gesturestart', (e) => {
      e.preventDefault();
      gestureStartScale = zoomScale;
    }, { passive: false });

    viewport.addEventListener('gesturechange', (e) => {
      e.preventDefault();
      const rect = viewport.getBoundingClientRect();
      const cursorX = e.clientX - rect.left;
      const cursorY = e.clientY - rect.top;
      const prevScale = zoomScale;
      const newScale = Math.min(Math.max(0.15, gestureStartScale * e.scale), 2.8);

      panX = cursorX - (cursorX - panX) * (newScale / prevScale);
      panY = cursorY - (cursorY - panY) * (newScale / prevScale);
      zoomScale = newScale;
      applyTransform();
    }, { passive: false });

    // --- Mouse Drag for Desktops / Left-Click Pan ---
    viewport.addEventListener('mousedown', (e) => {
      if (e.target.closest('.exploded-module') || e.target.closest('#core-device-frame') || e.target.closest('button') || e.target.closest('input')) {
        return;
      }
      isMouseDown = true;
      startMouseX = e.clientX - panX;
      startMouseY = e.clientY - panY;
    });

    window.addEventListener('mousemove', (e) => {
      if (!isMouseDown) return;
      panX = e.clientX - startMouseX;
      panY = e.clientY - startMouseY;
      applyTransform();
    });

    window.addEventListener('mouseup', () => {
      isMouseDown = false;
    });

    // -------------------------------------------------------------------------
    // 3. Smooth Zone Focus / Camera Navigation
    // -------------------------------------------------------------------------
    const ZONE_COORDS = {
      center: { x: 2800, y: 1970, zoom: 0.85 },
      screens: { x: 4620, y: 1550, zoom: 0.75 },
      team: { x: 2800, y: 2850, zoom: 0.75 },
      bom: { x: 1000, y: 1550, zoom: 0.75 },
      north: { x: 2800, y: 700, zoom: 0.75 }
    };

    function focusZone(zoneKey) {
      const z = ZONE_COORDS[zoneKey];
      if (!z) return;

      const targetScale = z.zoom;
      const targetPanX = (window.innerWidth / 2) - (z.x * targetScale);
      const targetPanY = (window.innerHeight / 2) - (z.y * targetScale);

      // Smooth animated pan
      const startPanX = panX;
      const startPanY = panY;
      const startScale = zoomScale;
      const startTime = performance.now();
      const duration = 550;

      function anim(time) {
        const elapsed = time - startTime;
        const progress = Math.min(1, elapsed / duration);
        // easeOutCubic
        const ease = 1 - Math.pow(1 - progress, 3);

        panX = startPanX + (targetPanX - startPanX) * ease;
        panY = startPanY + (targetPanY - startPanY) * ease;
        zoomScale = startScale + (targetScale - startScale) * ease;
        applyTransform();

        if (progress < 1) {
          requestAnimationFrame(anim);
        }
      }
      requestAnimationFrame(anim);
    }

    // -------------------------------------------------------------------------
    // 4. Exploded Module Offsets & Dynamic Leader Lines
    // -------------------------------------------------------------------------
    const BASE_OFFSETS = {
      gauges: { x: -625, y: -430 },
      media: { x: 515, y: -430 },
      timeline: { x: -765, y: 30 },
      bento: { x: 515, y: 30 }
    };

    function updateExplosion(val) {
      explosionRate = val / 100;
      document.getElementById('explode-val').textContent = `${val}%`;

      const coreX = 2605;
      const coreY = 1550;

      const gEl = document.getElementById('module-gauges');
      gEl.style.left = `${coreX + (BASE_OFFSETS.gauges.x * explosionRate)}px`;
      gEl.style.top = `${coreY + (BASE_OFFSETS.gauges.y * explosionRate)}px`;

      const mEl = document.getElementById('module-media');
      mEl.style.left = `${coreX + (BASE_OFFSETS.media.x * explosionRate)}px`;
      mEl.style.top = `${coreY + (BASE_OFFSETS.media.y * explosionRate)}px`;

      const tEl = document.getElementById('module-timeline');
      tEl.style.left = `${coreX + (BASE_OFFSETS.timeline.x * explosionRate)}px`;
      tEl.style.top = `${coreY + (BASE_OFFSETS.timeline.y * explosionRate)}px`;

      const bEl = document.getElementById('module-bento');
      bEl.style.left = `${coreX + (BASE_OFFSETS.bento.x * explosionRate)}px`;
      bEl.style.top = `${coreY + (BASE_OFFSETS.bento.y * explosionRate)}px`;

      drawLeaderLines();
    }

    function drawLeaderLines() {
      const svg = document.getElementById('svg-leader-lines');
      if (!showLeaderLines) {
        svg.innerHTML = '';
        return;
      }

      const coreX = 2605;
      const coreY = 1550;
      const coreW = 390;
      const coreH = 844;

      const conns = [
        { id: 'module-gauges', color: '#06B6D4', from: 'right', to: { x: coreX + 80, y: coreY + 40 } },
        { id: 'module-media', color: '#10B981', from: 'left', to: { x: coreX + 310, y: coreY + 120 } },
        { id: 'module-timeline', color: '#6366F1', from: 'right', to: { x: coreX + 20, y: coreY + 420 } },
        { id: 'module-bento', color: '#F59E0B', from: 'left', to: { x: coreX + 370, y: coreY + 640 } }
      ];

      let paths = '';
      conns.forEach(c => {
        const el = document.getElementById(c.id);
        if (!el) return;
        const elX = parseFloat(el.style.left);
        const elY = parseFloat(el.style.top);
        const elW = el.offsetWidth;
        const elH = el.offsetHeight;

        let startX = c.from === 'right' ? elX + elW : elX;
        let startY = elY + elH / 2;

        const endX = c.to.x;
        const endY = c.to.y;

        const midX = (startX + endX) / 2;
        const midY = (startY + endY) / 2;
        const d = `M ${startX} ${startY} Q ${midX} ${startY} ${midX} ${midY} T ${endX} ${endY}`;

        paths += `
          <g>
            <circle cx="${startX}" cy="${startY}" r="4" fill="${c.color}" />
            <path d="${d}" fill="none" stroke="${c.color}" stroke-width="2" stroke-dasharray="6 5" opacity="0.8" />
            <circle cx="${endX}" cy="${endY}" r="4" fill="${c.color}" />
          </g>
        `;
      });

      svg.innerHTML = paths;
    }

    function toggleLeaderLines() {
      showLeaderLines = !showLeaderLines;
      const btn = document.getElementById('toggle-lines-btn');
      if (showLeaderLines) {
        btn.innerHTML = '<span>🔗</span> 导线开';
        btn.className = 'px-2.5 py-1 rounded-xl bg-blue-50 text-blue-700 hover:bg-blue-100 text-[11px] font-bold border border-blue-200 transition-all flex items-center gap-1';
      } else {
        btn.innerHTML = '<span>🔗</span> 导线关';
        btn.className = 'px-2.5 py-1 rounded-xl bg-slate-100 text-slate-500 hover:bg-slate-200 text-[11px] font-bold border border-slate-200 transition-all flex items-center gap-1';
      }
      drawLeaderLines();
    }

    // -------------------------------------------------------------------------
    // 5. Global Cat State Machine Control
    // -------------------------------------------------------------------------
    const STATE_MAP = {
      normal: {
        video: './assets/app_assets/home_cat_clean.mp4',
        text: '精神不错',
        care: '3/5',
        activeItem: 1
      },
      dirty: {
        video: './assets/app_assets/home_cat_dirty.mp4',
        text: '该洗澡了',
        care: '42分',
        activeItem: 3
      },
      touch: {
        video: './assets/app_assets/home_cat_touch.mp4',
        text: '已到楼下',
        care: '急需陪伴',
        activeItem: 5
      }
    };

    function setGlobalCatState(st) {
      const cfg = STATE_MAP[st];
      const vid = document.getElementById('phone-cat-video');
      vid.src = cfg.video;
      vid.play();

      document.getElementById('phone-state-text').textContent = cfg.text;
      document.getElementById('phone-care-ratio').textContent = cfg.care;

      ['normal', 'dirty', 'touch'].forEach(s => {
        const btn = document.getElementById(`btn-state-${s}`);
        if (s === st) {
          btn.className = `px-2.5 py-1 rounded-lg text-[11px] font-black transition-all shadow-2xs flex items-center gap-1 ${
            s === 'normal' ? 'bg-emerald-500 text-white' : s === 'dirty' ? 'bg-amber-500 text-white' : 'bg-rose-500 text-white'
          }`;
        } else {
          btn.className = 'px-2.5 py-1 rounded-lg text-[11px] font-black transition-all text-slate-600 hover:bg-slate-200 flex items-center gap-1';
        }
      });

      const item = SCHEDULE_DATA[cfg.activeItem];
      if (item) {
        document.getElementById('phone-active-icon').src = item.icon;
        document.getElementById('phone-active-title').textContent = item.title;
        document.getElementById('phone-active-time').textContent = item.time;
        document.getElementById('phone-active-desc').textContent = item.desc;
      }
    }

    // -------------------------------------------------------------------------
    // 6. Dynamic Populate Timeline, BOM & Team
    // -------------------------------------------------------------------------
    function populateTimeline() {
      const container = document.getElementById('timeline-scroll-list');
      let html = '';
      SCHEDULE_DATA.forEach(it => {
        html += `
          <div class="p-2.5 rounded-2xl bg-slate-50 border border-slate-200/80 hover:border-indigo-500 hover:bg-white transition-all flex items-start gap-3 cursor-pointer" onclick="event.stopPropagation(); inspectItem(${it.id})">
            <div class="w-10 h-10 rounded-xl bg-white border border-slate-200 p-1 flex items-center justify-center shrink-0 shadow-2xs">
              <img src="${it.icon}" class="w-full h-full object-contain" alt="${it.title}">
            </div>
            <div class="flex-1 min-w-0">
              <div class="flex items-center justify-between">
                <span class="text-xs font-black text-slate-900">${it.time} · ${it.title}</span>
                <div class="flex items-center gap-1.5">
                  <img src="${it.avatar}" class="w-4 h-4 rounded-full object-cover" alt="${it.person}">
                  <span class="text-[10px] font-bold text-slate-600">${it.person}</span>
                </div>
              </div>
              <p class="text-[10.5px] text-slate-500 mt-1 leading-relaxed">${it.desc}</p>
            </div>
          </div>
        `;
      });
      container.innerHTML = html;
    }

    function populateBOM() {
      // 11 Board Items
      const bContainer = document.getElementById('unified-bom-items');
      let bHtml = '';
      SCHEDULE_DATA.forEach(it => {
        bHtml += `
          <div class="bg-slate-50 p-3 rounded-2xl border border-slate-200 hover:border-indigo-400 transition-all flex flex-col items-center text-center cursor-pointer" onclick="inspectItem(${it.id})">
            <img src="${it.icon}" class="w-12 h-12 object-contain mb-1.5 drop-shadow-2xs" alt="${it.title}">
            <span class="text-[11px] font-black text-slate-800 truncate w-full">${it.title}</span>
            <span class="text-[9px] text-slate-400 font-mono mt-0.5">${it.time} · ${it.person}</span>
          </div>
        `;
      });
      bContainer.innerHTML = bHtml;

      // UI Icons
      const uContainer = document.getElementById('unified-bom-icons');
      const uiIcons = [
        { name: 'ic_btn_trophy.png', title: '3D 荣誉金杯', path: './assets/app_assets/ui_icons/ic_btn_trophy.png' },
        { name: 'ic_tile_journal.png', title: '档案手册磁贴', path: './assets/app_assets/ic_tile_journal.png' },
        { name: 'ic_index_catlove.png', title: '爱猫加权徽标', path: './assets/app_assets/ui_icons/ic_index_catlove.png' },
        { name: 'ic_index_happiness.png', title: '快乐值仪表', path: './assets/app_assets/ui_icons/ic_index_happiness.png' },
        { name: 'ic_btn_like_active.png', title: '点赞激活状态', path: './assets/app_assets/ui_icons/ic_btn_like_active.png' },
        { name: 'podium_3d.png', title: '3D 领奖台模型', path: './assets/app_assets/generated/podium_3d.png' }
      ];
      let uHtml = '';
      uiIcons.forEach(ui => {
        uHtml += `
          <div class="bg-slate-50 p-3 rounded-2xl border border-slate-200 hover:border-indigo-400 transition-all flex flex-col items-center text-center">
            <img src="${ui.path}" class="w-12 h-12 object-contain mb-1.5 drop-shadow-2xs" alt="${ui.title}">
            <span class="text-[11px] font-black text-slate-800 truncate w-full">${ui.title}</span>
            <span class="text-[9px] text-slate-400 font-mono mt-0.5 truncate w-full">${ui.name}</span>
          </div>
        `;
      });
      uContainer.innerHTML = uHtml;

      // Archives
      const aContainer = document.getElementById('unified-bom-archives');
      let aHtml = '';
      [163, 164, 165, 166, 167, 168, 169].forEach(id => {
        aHtml += `
          <div class="bg-slate-50 p-2.5 rounded-2xl border border-slate-200 hover:border-indigo-400 transition-all">
            <img src="./assets/app_assets/archives/archive_${id}.png" class="w-full h-auto rounded-xl object-cover mb-1.5 cursor-pointer hover:scale-105 transition-transform" alt="手账${id}" onclick="inspectImage(this.src, '老马手账 #${id}')">
            <div class="text-[10px] font-bold text-slate-700 text-center">手账日常 #${id}</div>
          </div>
        `;
      });
      aContainer.innerHTML = aHtml;
    }

    function populateTeam() {
      const container = document.getElementById('unified-team-grid');
      let html = '';
      TEAM_MEMBERS.forEach(m => {
        html += `
          <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 hover:border-blue-500 hover:bg-white transition-all flex flex-col items-center text-center cursor-pointer" onclick="inspectMember('${m.alias}')">
            <img src="${m.avatar}" class="w-12 h-12 rounded-full object-cover shadow-xs ring-2 ring-slate-200 mb-2" alt="${m.alias}">
            <span class="text-xs font-black text-slate-900">${m.alias} <span class="text-[10px] font-normal text-slate-400">(${m.name})</span></span>
            <span class="text-[10px] font-bold text-blue-600 mt-0.5">${m.role}</span>
            <span class="text-[9px] text-slate-400 mt-1 leading-relaxed">${m.desc}</span>
          </div>
        `;
      });
      container.innerHTML = html;
    }

    // -------------------------------------------------------------------------
    // 7. Component Inspector Drawer
    // -------------------------------------------------------------------------
    function inspectComponent(type) {
      const drawer = document.getElementById('inspector-drawer');
      const titleEl = document.getElementById('insp-title');
      const tagEl = document.getElementById('insp-tag');
      const imgEl = document.getElementById('insp-img');
      const nameEl = document.getElementById('insp-name');
      const pathEl = document.getElementById('insp-path');
      const typeEl = document.getElementById('insp-type');
      const authorEl = document.getElementById('insp-author');
      const descEl = document.getElementById('insp-desc');

      if (type === 'gauges') {
        titleEl.textContent = '状态感知与生命指标仪表总成';
        tagEl.textContent = '[ASM-01 · SENSORS]';
        imgEl.src = './assets/app_assets/ui_icons/ic_index_catlove.png';
        nameEl.textContent = 'HUD 生命力与加权爱猫指数';
        pathEl.textContent = '/assets/app_assets/ui_icons/ic_index_*.png';
        typeEl.textContent = 'Vector SVG / Alpha PNG';
        authorEl.textContent = '阿杰 (视觉) / Lex (数据)';
        descEl.textContent = '实时显示老马的心情指数、快乐值、脏污预警及本周养猫指数加权得分，端侧 1000ms 心跳轮询保障。';
      } else if (type === 'media') {
        titleEl.textContent = '视觉多媒体内核与工况视频总成';
        tagEl.textContent = '[ASM-02 · MEDIA ENGINE]';
        imgEl.src = './assets/app_assets/hero_cat_sitting_tight.png';
        nameEl.textContent = '老马 1080P 60fps 工况录播视频';
        pathEl.textContent = '/assets/app_assets/home_cat_*.mp4';
        typeEl.textContent = 'H.264 High Profile MP4 (60fps)';
        authorEl.textContent = '小六 (动效) / Bingo (架构)';
        descEl.textContent = '包含活力健康、饥饿脏污、抚摸贴贴三大无缝切换高画质视频循环，搭配 5 张免抠 Alpha 剪影贴纸。';
      } else if (type === 'timeline') {
        titleEl.textContent = '24H 空间感知与事件流总成';
        tagEl.textContent = '[ASM-03 · TIMELINE 11 ITEMS]';
        imgEl.src = './assets/app_assets/ic_board_brush.png';
        nameEl.textContent = '11 大手绘 3D 爱猫道具总成';
        pathEl.textContent = '/assets/app_assets/ic_board_*.png';
        typeEl.textContent = '3D 拟物渲染透明图';
        authorEl.textContent = '阿杰 (手绘) / 木子 (产品旅程)';
        descEl.textContent = '由听诊器、气垫梳、鸡肉冻干、恒温饮水机、航空箱、逗猫棒、飞书徽章等 11 个独立道具构成老马 24 小时照护事件流。';
      } else if (type === 'bento') {
        titleEl.textContent = '双梯形 Bento 交互机能矩阵';
        tagEl.textContent = '[ASM-04 · DUAL TRAPEZOID]';
        imgEl.src = './assets/app_assets/ui_icons/ic_btn_trophy.png';
        nameEl.textContent = '10.3° 倾角圆角直角双梯形';
        pathEl.textContent = 'SVG ClipPath + DropShadow';
        typeEl.textContent = '硬件级矢量边缘裁切';
        authorEl.textContent = 'Adam (交互) / Howwoy (原生)';
        descEl.textContent = '左梯形承载爱喵排行榜与 3D 金银铜领奖台；右梯形承载老马档案馆与可自由拖拽贴纸画廊，中间精确保持 14px 缝隙贴合。';
      }

      drawer.classList.remove('translate-x-[460px]');
    }

    function inspectItem(idx) {
      const it = SCHEDULE_DATA[idx];
      if (!it) return;
      const drawer = document.getElementById('inspector-drawer');
      document.getElementById('insp-title').textContent = it.title;
      document.getElementById('insp-tag').textContent = `[ITEM-${idx} · ${it.time}]`;
      document.getElementById('insp-img').src = it.icon;
      document.getElementById('insp-name').textContent = it.title;
      document.getElementById('insp-path').textContent = it.icon;
      document.getElementById('insp-type').textContent = '24H 照护事件道具';
      document.getElementById('insp-author').textContent = `${it.person} (执行人)`;
      document.getElementById('insp-desc').textContent = it.desc;
      drawer.classList.remove('translate-x-[460px]');
    }

    function inspectMember(alias) {
      const mem = TEAM_MEMBERS.find(m => m.alias.toLowerCase() === alias.toLowerCase());
      if (!mem) return;
      const drawer = document.getElementById('inspector-drawer');
      document.getElementById('insp-title').textContent = `${mem.alias} (${mem.name})`;
      document.getElementById('insp-tag').textContent = `[PERSONNEL-${mem.alias.toUpperCase()}]`;
      document.getElementById('insp-img').src = mem.avatar;
      document.getElementById('insp-name').textContent = mem.role;
      document.getElementById('insp-path').textContent = mem.avatar;
      document.getElementById('insp-type').textContent = '团队真实核心成员';
      document.getElementById('insp-author').textContent = `${mem.name} · ${mem.alias}`;
      document.getElementById('insp-desc').textContent = mem.desc;
      drawer.classList.remove('translate-x-[460px]');
    }

    function inspectImage(src, title) {
      const drawer = document.getElementById('inspector-drawer');
      document.getElementById('insp-title').textContent = title;
      document.getElementById('insp-tag').textContent = '[SCREENSHOT / ARCHIVE]';
      document.getElementById('insp-img').src = src;
      document.getElementById('insp-name').textContent = title;
      document.getElementById('insp-path').textContent = src;
      document.getElementById('insp-type').textContent = 'High-Res Device JPG / PNG';
      document.getElementById('insp-author').textContent = '真机环境实录提取';
      document.getElementById('insp-desc').textContent = '完整呈现真实设备运行效果，包含状态流转、手账日记及微交互反馈。';
      drawer.classList.remove('translate-x-[460px]');
    }

    function closeInspector() {
      document.getElementById('inspector-drawer').classList.add('translate-x-[460px]');
    }

    // -------------------------------------------------------------------------
    // 8. Boot Initialization
    // -------------------------------------------------------------------------
    window.addEventListener('DOMContentLoaded', () => {
      populateTimeline();
      populateBOM();
      populateTeam();
      updateExplosion(80);
      focusZone('center');
    });

    window.addEventListener('resize', () => {
      drawLeaderLines();
    });
  </script>
</body>
</html>
"""

with open('/Users/bingo/Code/LYi/projects/laoma-engine-showcase/index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Unified index.html updated successfully!")
