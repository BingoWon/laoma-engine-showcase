import os

html_content = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>老马喵务局 · 端侧智能体系统架构与工程全景拆解大屏</title>
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
            },
            tech: {
              blue: '#2563EB',
              cyan: '#0891B2',
              emerald: '#059669',
              amber: '#D97706',
              rose: '#E11D48',
              indigo: '#4F46E5',
              slate: '#334155'
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

    /* Technical Glow Highlights */
    .glow-cyan {
      box-shadow: 0 0 35px -5px rgba(8, 145, 178, 0.20);
    }
    .glow-amber {
      box-shadow: 0 0 35px -5px rgba(217, 119, 6, 0.20);
    }
    .glow-emerald {
      box-shadow: 0 0 35px -5px rgba(5, 150, 105, 0.20);
    }
    .glow-indigo {
      box-shadow: 0 0 35px -5px rgba(79, 70, 229, 0.20);
    }
    .glow-blue {
      box-shadow: 0 0 35px -5px rgba(37, 99, 235, 0.20);
    }
  </style>
</head>
<body class="bg-slate-100 text-slate-800 antialiased overflow-hidden font-sans h-screen w-screen flex flex-col select-none">

  <!-- ========================================================================= -->
  <!-- 顶部极简工业级 HUD 控制中心 (Top Technical HUD) -->
  <!-- ========================================================================= -->
  <header class="fixed top-4 left-6 right-6 z-50 pointer-events-none flex items-center justify-between">
    <!-- Left: Engineering System Identifier -->
    <div class="pointer-events-auto flex items-center gap-3 bg-white/95 backdrop-blur-xl px-4 py-2 rounded-2xl border border-slate-200/90 shadow-sm">
      <div class="relative w-10 h-10 rounded-xl overflow-hidden shadow-xs ring-1 ring-blue-500/30 bg-slate-900 shrink-0">
        <img src="./assets/app_assets/app_icon_preview.png" alt="系统标识" class="w-full h-full object-cover">
      </div>
      <div>
        <div class="flex items-center gap-2">
          <h1 class="font-black text-slate-900 text-sm tracking-tight">老马端侧智能体系统架构</h1>
          <span class="text-[10px] px-2 py-0.5 rounded-md bg-blue-50 text-blue-700 font-bold border border-blue-200/60 font-mono">SPEC-V2.4</span>
          <span class="text-[10px] px-2 py-0.5 rounded-full bg-slate-100 text-slate-700 font-mono font-bold">PRODUCTION VERIFIED</span>
        </div>
        <p class="text-[10.5px] text-slate-400 font-medium mt-0.5 font-mono">
          PRECISION ENGINEERING DECONSTRUCTION · 控制系统 · 动画管线 · 技术物料
        </p>
      </div>
    </div>

    <!-- Center: Exploded Engineering Controls & FSM State Trigger -->
    <div class="pointer-events-auto flex items-center gap-3 bg-white/95 backdrop-blur-xl px-4 py-2 rounded-2xl border border-slate-200/90 shadow-sm">
      <!-- Explosion Slider -->
      <div class="flex items-center gap-2">
        <span class="text-xs font-black text-slate-700 flex items-center gap-1 font-mono">
          <span>ASM DISPERSION:</span>
        </span>
        <input type="range" id="explode-slider" min="0" max="100" value="80" class="w-28 accent-blue-600 cursor-pointer" oninput="updateExplosion(this.value)">
        <span id="explode-val" class="font-mono text-xs font-black text-blue-600 w-8 text-right">80%</span>
      </div>

      <div class="w-px h-4 bg-slate-200"></div>

      <!-- FSM State Switcher -->
      <div class="flex items-center gap-1 bg-slate-100 p-1 rounded-xl">
        <button onclick="setGlobalCatState('normal')" id="btn-state-normal" class="px-2.5 py-1 rounded-lg text-[11px] font-black font-mono transition-all bg-emerald-600 text-white shadow-2xs flex items-center gap-1">
          <span class="w-1.5 h-1.5 rounded-full bg-white animate-pulse"></span>
          <span>ST-01 NORMAL</span>
        </button>
        <button onclick="setGlobalCatState('dirty')" id="btn-state-dirty" class="px-2.5 py-1 rounded-lg text-[11px] font-black font-mono transition-all text-slate-600 hover:bg-slate-200 flex items-center gap-1">
          <span class="w-1.5 h-1.5 rounded-full bg-amber-500"></span>
          <span>ST-02 DIRTY</span>
        </button>
        <button onclick="setGlobalCatState('touch')" id="btn-state-touch" class="px-2.5 py-1 rounded-lg text-[11px] font-black font-mono transition-all text-slate-600 hover:bg-slate-200 flex items-center gap-1">
          <span class="w-1.5 h-1.5 rounded-full bg-rose-500"></span>
          <span>ST-03 TOUCH</span>
        </button>
      </div>

      <div class="w-px h-4 bg-slate-200"></div>

      <!-- Toggle Lines -->
      <button id="toggle-lines-btn" onclick="toggleLeaderLines()" class="px-2.5 py-1 rounded-xl bg-blue-50 text-blue-700 hover:bg-blue-100 text-[11px] font-bold border border-blue-200 transition-all flex items-center gap-1">
        <span>🔗</span> 导线开
      </button>
    </div>

    <!-- Right: Viewport Scale & Recenter -->
    <div class="pointer-events-auto flex items-center gap-2 bg-white/95 backdrop-blur-xl px-3 py-2 rounded-2xl border border-slate-200/90 shadow-sm">
      <span class="text-xs font-mono font-black text-slate-700">SCALE: <span id="hud-zoom" class="text-blue-600">85%</span></span>
      <button onclick="zoomStep(1.15)" class="w-6 h-6 rounded-lg bg-slate-100 hover:bg-slate-200 flex items-center justify-center font-mono font-bold text-xs" title="放大">＋</button>
      <button onclick="zoomStep(0.85)" class="w-6 h-6 rounded-lg bg-slate-100 hover:bg-slate-200 flex items-center justify-center font-mono font-bold text-xs" title="缩小">－</button>
      <button onclick="resetCanvasTransform()" class="px-2 py-1 rounded-lg bg-slate-100 hover:bg-slate-200 text-xs font-bold text-slate-700 ml-1">复位居中</button>
    </div>
  </header>

  <!-- ========================================================================= -->
  <!-- 底部视窗直达导航胶囊 (Bottom Zone Navigation Dock) -->
  <!-- ========================================================================= -->
  <nav class="fixed bottom-6 left-1/2 -translate-x-1/2 z-50 pointer-events-auto flex items-center gap-2 bg-white/90 backdrop-blur-2xl px-4 py-2 rounded-2xl border border-slate-200 shadow-xl">
    <span class="text-[11px] font-bold text-slate-400 mr-1 font-mono">
      <span>NAV_INDEX:</span>
    </span>
    <button onclick="focusZone('center')" class="px-3 py-1.5 rounded-xl text-xs font-black text-slate-700 hover:bg-blue-50 hover:text-blue-600 transition-all flex items-center gap-1.5 border border-transparent hover:border-blue-200">
      <span>⚙️ 发动机核心装配体</span>
    </button>
    <button onclick="focusZone('screens')" class="px-3 py-1.5 rounded-xl text-xs font-black text-slate-700 hover:bg-blue-50 hover:text-blue-600 transition-all flex items-center gap-1.5 border border-transparent hover:border-blue-200">
      <span>📱 真机 8 大工况验证矩阵</span>
    </button>
    <button onclick="focusZone('team')" class="px-3 py-1.5 rounded-xl text-xs font-black text-slate-700 hover:bg-blue-50 hover:text-blue-600 transition-all flex items-center gap-1.5 border border-transparent hover:border-blue-200">
      <span>👥 产研 14 人工程职能矩阵</span>
    </button>
    <button onclick="focusZone('bom')" class="px-3 py-1.5 rounded-xl text-xs font-black text-slate-700 hover:bg-blue-50 hover:text-blue-600 transition-all flex items-center gap-1.5 border border-transparent hover:border-blue-200">
      <span>📦 全量工程物料清单 (BOM)</span>
    </button>
    <button onclick="focusZone('north')" class="px-3 py-1.5 rounded-xl text-xs font-black text-slate-700 hover:bg-blue-50 hover:text-blue-600 transition-all flex items-center gap-1.5 border border-transparent hover:border-blue-200">
      <span>📜 系统架构与 FSM 控制拓扑</span>
    </button>
  </nav>

  <!-- ========================================================================= -->
  <!-- 左下角触控板手势操作提示 (Trackpad Guide Badge) -->
  <!-- ========================================================================= -->
  <div class="fixed bottom-6 left-6 z-40 pointer-events-none bg-white/85 backdrop-blur-md px-3.5 py-2 rounded-xl border border-slate-200/80 shadow-sm flex items-center gap-2 text-[11px] text-slate-500 font-mono">
    <span class="w-2 h-2 rounded-full bg-emerald-500"></span>
    <span>TOUCHPAD: 双指滑动平移视窗 · 双指捏合无极缩放</span>
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
      <!-- ZONE NORTH (顶部总成 · Y: 380) · 系统技术栈架构、控制系统与 FSM 状态机拓扑 -->
      <!-- ===================================================================== -->
      <div id="zone-north" class="absolute z-20 bg-white/95 backdrop-blur-md p-8 rounded-3xl border border-slate-300/80 shadow-xl" style="left: 1700px; top: 380px; width: 2200px;">
        <!-- Header -->
        <div class="flex items-center justify-between border-b border-slate-200 pb-4 mb-6">
          <div class="flex items-center gap-3">
            <span class="w-10 h-10 rounded-2xl bg-blue-50 border border-blue-200 flex items-center justify-center text-xl">⚙️</span>
            <div>
              <h2 class="text-lg font-black text-slate-900 tracking-tight">端侧智能体系统架构 · 混合容器渲染内核与通信协议总成</h2>
              <span class="text-xs font-mono text-blue-600 font-bold">[SYS-CORE-000 · HYBRID WEBVIEW CONTAINER & IPC COMMUNICATIONS PIPELINE]</span>
            </div>
          </div>
          <div class="flex items-center gap-2">
            <span class="text-xs font-mono text-slate-400">ARCHITECTURAL SPECIFICATION</span>
            <span class="text-xs px-2.5 py-1 rounded-full bg-blue-50 text-blue-700 font-mono font-bold border border-blue-200">ACTIVE STABLE</span>
          </div>
        </div>

        <!-- 4 Core Technical Architecture Pillars -->
        <div class="grid grid-cols-4 gap-6 mb-6">
          
          <!-- Pillar 1: Technology Stack -->
          <div class="p-5 rounded-2xl bg-slate-50 border border-slate-200">
            <span class="text-xs font-mono font-black text-blue-600">LAYER 01 · 核心技术栈</span>
            <h4 class="text-sm font-black text-slate-800 mt-1 mb-2">高保真混合渲染容器</h4>
            <ul class="text-xs text-slate-500 space-y-1.5 font-mono">
              <li>• 渲染内核: Android WebView 独立进程</li>
              <li>• 样式引擎: Tailwind JIT GPU 加速</li>
              <li>• 物理驱动: React 18 Concurrent / Custom Hook</li>
              <li>• 类型契约: TypeScript 严格数据边界</li>
            </ul>
          </div>

          <!-- Pillar 2: Control System -->
          <div class="p-5 rounded-2xl bg-slate-50 border border-slate-200 border-l-4 border-l-cyan-600">
            <span class="text-xs font-mono font-black text-cyan-600">LAYER 02 · 控制系统</span>
            <h4 class="text-sm font-black text-slate-800 mt-1 mb-2">FSM 有限状态机与调度</h4>
            <ul class="text-xs text-slate-500 space-y-1.5 font-mono">
              <li>• 状态互斥: Normal / Dirty / Touch 原子流转</li>
              <li>• 轮询保活: 1000ms 心跳数据上报与采样</li>
              <li>• 触发判定: 生理数值加权与滑动窗口滤波</li>
              <li>• 异常拦截: 离线状态安全熔断与本地缓存</li>
            </ul>
          </div>

          <!-- Pillar 3: Animation Pipeline -->
          <div class="p-5 rounded-2xl bg-slate-50 border border-slate-200 border-l-4 border-l-emerald-600">
            <span class="text-xs font-mono font-black text-emerald-600">LAYER 03 · 动画与渲染管线</span>
            <h4 class="text-sm font-black text-slate-800 mt-1 mb-2">多模态流媒体与动效混合</h4>
            <ul class="text-xs text-slate-500 space-y-1.5 font-mono">
              <li>• 视频解码: H.264 High-Profile 硬件硬解</li>
              <li>• 图层合成: Alpha 通道剪影与视频无缝 Overlay</li>
              <li>• 动力学方程: 阻尼衰减回弹与弹簧物理</li>
              <li>• 帧率稳态: 60fps 恒定锁帧，零丢帧保障</li>
            </ul>
          </div>

          <!-- Pillar 4: Bridge Protocol -->
          <div class="p-5 rounded-2xl bg-slate-50 border border-slate-200 border-l-4 border-l-indigo-600">
            <span class="text-xs font-mono font-black text-indigo-600">LAYER 04 · 端侧通信协议</span>
            <h4 class="text-sm font-black text-slate-800 mt-1 mb-2">MagicOS Native Bridge 协议</h4>
            <ul class="text-xs text-slate-500 space-y-1.5 font-mono">
              <li>• 空间感知: 蓝牙 Beacon / 姿态传感器订阅</li>
              <li>• 进程通信: Native <-> Web 双向异步 IPC</li>
              <li>• 任务调度: 高德 API 排班与飞书 Bot 推送</li>
              <li>• 安全域控: 仅授权端侧白名单通信端口</li>
            </ul>
          </div>
        </div>

        <!-- FSM Mathematical State Machine Diagram -->
        <div class="p-4 rounded-2xl bg-slate-100/80 border border-slate-200 font-mono text-xs flex items-center justify-between">
          <div class="flex items-center gap-3">
            <span class="px-2.5 py-1 rounded-lg bg-emerald-100 text-emerald-800 font-bold">[ST-01: NORMAL 活力健康]</span>
            <span class="text-slate-400">──► (污垢传感器告警 ∨ 8h未照料) ──►</span>
            <span class="px-2.5 py-1 rounded-lg bg-amber-100 text-amber-800 font-bold">[ST-02: DIRTY 饥饿脏污]</span>
            <span class="text-slate-400">──► (触控抚摸手势 ∨ 物理呼噜响应) ──►</span>
            <span class="px-2.5 py-1 rounded-lg bg-rose-100 text-rose-800 font-bold">[ST-03: TOUCH 抚摸互动]</span>
          </div>
          <div class="text-slate-500 text-[11px] font-mono">
            <span>TRANSITION_LATENCY: < 16ms (1 FRAME)</span> | <span>GPU_SURFACE: HARDWARE COMPOSITED</span>
          </div>
        </div>
      </div>

      <!-- ===================================================================== -->
      <!-- ZONE CENTER (中央整机装配体与发动机有机拆解核心 · Y: 1550) -->
      <!-- ===================================================================== -->

      <!-- 1. 中央整机装配体 (The Central Core: Honor Native Target) -->
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
                <span class="text-[8.5px] font-mono font-bold text-blue-300">YOYO IPC</span>
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
                <div class="absolute bottom-3 right-3 z-20 bg-black/40 backdrop-blur-md px-2.5 py-1 rounded-full text-[10px] text-white font-mono font-bold flex items-center gap-1">
                  <span>●</span> 1080P 60FPS HARDWARE STREAM
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

      <!-- 2. 发动机环绕总成 01 (左上) · 状态感知仪表控制组 -->
      <div id="module-gauges" class="exploded-module absolute z-20 bg-white/95 backdrop-blur-md p-5 rounded-3xl border border-cyan-200/80 shadow-xl glow-cyan cursor-pointer" style="left: 1980px; top: 1120px; width: 520px;" onclick="inspectComponent('gauges')">
        <div class="flex items-center justify-between border-b border-slate-100 pb-3 mb-4">
          <div class="flex items-center gap-2.5">
            <span class="w-8 h-8 rounded-xl bg-cyan-50 border border-cyan-200 flex items-center justify-center text-base">📊</span>
            <div>
              <h3 class="font-black text-slate-900 text-sm">状态感知与生命指标控制系统</h3>
              <span class="text-[10px] font-mono text-cyan-600 font-bold">[ASM-01 · SENSORY CONTROL & VITALITY GAUGES]</span>
            </div>
          </div>
          <span class="text-[10px] px-2 py-0.5 rounded-full bg-cyan-50 text-cyan-700 font-mono font-bold">5 SENSORS</span>
        </div>

        <div class="grid grid-cols-2 gap-3">
          <div class="p-3 rounded-2xl bg-slate-50 border border-slate-200/80 hover:border-cyan-400 transition-all cursor-pointer" onclick="event.stopPropagation(); inspectComponent('gauge_love')">
            <div class="flex items-center gap-2 mb-1.5">
              <img src="./assets/app_assets/ui_icons/ic_index_catlove.png" class="w-6 h-6 object-contain" alt="爱猫指数">
              <span class="text-xs font-bold text-slate-700">爱猫加权算法模型</span>
            </div>
            <div class="flex items-baseline justify-between">
              <span class="text-2xl font-black text-rose-500 font-mono">86<span class="text-xs font-normal text-slate-400 ml-1">分</span></span>
              <span class="text-[10px] text-emerald-600 font-bold font-mono bg-emerald-50 px-1.5 py-0.2 rounded">Δ+4.2% W/W</span>
            </div>
          </div>

          <div class="p-3 rounded-2xl bg-slate-50 border border-slate-200/80 hover:border-cyan-400 transition-all cursor-pointer" onclick="event.stopPropagation(); inspectComponent('gauge_happiness')">
            <div class="flex items-center gap-2 mb-1.5">
              <img src="./assets/app_assets/ui_icons/ic_index_happiness.png" class="w-6 h-6 object-contain" alt="快乐值">
              <span class="text-xs font-bold text-slate-700">情绪感知指数</span>
            </div>
            <div class="flex items-baseline justify-between">
              <span class="text-2xl font-black text-amber-500 font-mono">98<span class="text-xs font-normal text-slate-400 ml-1">分</span></span>
              <span class="text-[10px] text-amber-600 font-bold font-mono bg-amber-50 px-1.5 py-0.2 rounded">OPTIMAL</span>
            </div>
          </div>

          <div class="p-3 rounded-2xl bg-slate-50 border border-slate-200/80 hover:border-cyan-400 transition-all cursor-pointer" onclick="event.stopPropagation(); inspectComponent('gauge_green')">
            <div class="flex items-center gap-2 mb-1.5">
              <img src="./assets/app_assets/ui_icons/ic_index_happiness_green.png" class="w-6 h-6 object-contain" alt="健康状态">
              <span class="text-xs font-bold text-slate-700">健康活力稳态</span>
            </div>
            <div class="flex items-baseline justify-between">
              <span class="text-2xl font-black text-emerald-600 font-mono">100%</span>
              <span class="text-[10px] text-slate-400 font-mono">STEADY</span>
            </div>
          </div>

          <div class="p-3 rounded-2xl bg-slate-50 border border-slate-200/80 hover:border-cyan-400 transition-all cursor-pointer" onclick="event.stopPropagation(); inspectComponent('gauge_orange')">
            <div class="flex items-center gap-2 mb-1.5">
              <img src="./assets/app_assets/ui_icons/ic_index_happiness_orange.png" class="w-6 h-6 object-contain" alt="轻度预警">
              <span class="text-xs font-bold text-slate-700">污垢与饥饿阈值报警</span>
            </div>
            <div class="flex items-baseline justify-between">
              <span class="text-2xl font-black text-amber-500 font-mono">42<span class="text-xs font-normal text-slate-400 ml-1">分</span></span>
              <span class="text-[10px] text-amber-600 font-bold font-mono bg-amber-50 px-1.5 py-0.2 rounded">THRESHOLD_ALERT</span>
            </div>
          </div>
        </div>

        <div class="mt-3 pt-2.5 border-t border-slate-100 flex items-center justify-between text-[10px] text-slate-500 font-mono">
          <span>SAMPLING: 1000ms 端侧心跳</span>
          <span class="text-cyan-600 font-bold">HARDWARE HUD DIRECT PIPELINE</span>
        </div>
      </div>

      <!-- 3. 发动机环绕总成 02 (右上) · 视觉多媒体内核与解码管线 -->
      <div id="module-media" class="exploded-module absolute z-20 bg-white/95 backdrop-blur-md p-5 rounded-3xl border border-emerald-200/80 shadow-xl glow-emerald cursor-pointer" style="left: 3120px; top: 1120px; width: 540px;" onclick="inspectComponent('media')">
        <div class="flex items-center justify-between border-b border-slate-100 pb-3 mb-4">
          <div class="flex items-center gap-2.5">
            <span class="w-8 h-8 rounded-xl bg-emerald-50 border border-emerald-200 flex items-center justify-center text-base">🎬</span>
            <div>
              <h3 class="font-black text-slate-900 text-sm">视觉多媒体硬件解码与动效管线</h3>
              <span class="text-[10px] font-mono text-emerald-600 font-bold">[ASM-02 · MULTIMEDIA CODEC & GPU RENDERING PIPELINE]</span>
            </div>
          </div>
          <span class="text-[10px] px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-700 font-mono font-bold">HARDWARE ACCEL</span>
        </div>

        <div class="grid grid-cols-3 gap-2.5 mb-3">
          <div class="p-2 rounded-2xl bg-slate-50 border border-slate-200 hover:border-emerald-500 transition-all cursor-pointer flex flex-col" onclick="event.stopPropagation(); setGlobalCatState('normal')">
            <div class="relative w-full h-28 rounded-xl overflow-hidden bg-black mb-2">
              <video src="./assets/app_assets/home_cat_clean.mp4" autoplay loop muted playsinline class="w-full h-full object-cover"></video>
              <span class="absolute top-1 left-1 px-1.5 py-0.5 rounded bg-emerald-500/80 text-[8px] text-white font-mono font-bold">STREAM 01</span>
            </div>
            <span class="text-[11px] font-black text-slate-800 truncate">home_cat_clean</span>
            <span class="text-[9px] text-slate-400 font-mono">H.264 · 1080x1920 60P</span>
          </div>

          <div class="p-2 rounded-2xl bg-slate-50 border border-slate-200 hover:border-amber-500 transition-all cursor-pointer flex flex-col" onclick="event.stopPropagation(); setGlobalCatState('dirty')">
            <div class="relative w-full h-28 rounded-xl overflow-hidden bg-black mb-2">
              <video src="./assets/app_assets/home_cat_dirty.mp4" autoplay loop muted playsinline class="w-full h-full object-cover"></video>
              <span class="absolute top-1 left-1 px-1.5 py-0.5 rounded bg-amber-500/80 text-[8px] text-white font-mono font-bold">STREAM 02</span>
            </div>
            <span class="text-[11px] font-black text-slate-800 truncate">home_cat_dirty</span>
            <span class="text-[9px] text-slate-400 font-mono">H.264 · 1080x1920 60P</span>
          </div>

          <div class="p-2 rounded-2xl bg-slate-50 border border-slate-200 hover:border-rose-500 transition-all cursor-pointer flex flex-col" onclick="event.stopPropagation(); setGlobalCatState('touch')">
            <div class="relative w-full h-28 rounded-xl overflow-hidden bg-black mb-2">
              <video src="./assets/app_assets/home_cat_touch.mp4" autoplay loop muted playsinline class="w-full h-full object-cover"></video>
              <span class="absolute top-1 left-1 px-1.5 py-0.5 rounded bg-rose-500/80 text-[8px] text-white font-mono font-bold">STREAM 03</span>
            </div>
            <span class="text-[11px] font-black text-slate-800 truncate">home_cat_touch</span>
            <span class="text-[9px] text-slate-400 font-mono">H.264 · 1080x1920 60P</span>
          </div>
        </div>

        <div class="p-2.5 rounded-2xl bg-slate-50 border border-slate-200 flex items-center justify-between">
          <div class="flex items-center gap-3">
            <div class="w-12 h-12 rounded-xl bg-white border border-slate-200 p-1 flex items-center justify-center">
              <img src="./assets/app_assets/hero_cat_sitting_tight.png" class="w-full h-full object-contain" alt="免抠图层">
            </div>
            <div class="w-12 h-12 rounded-xl bg-white border border-slate-200 p-1 flex items-center justify-center">
              <img src="./assets/app_assets/hero_cat_carrier_tight.png" class="w-full h-full object-contain" alt="航空箱图层">
            </div>
            <div>
              <div class="text-xs font-bold text-slate-800">Alpha 8-bit 透明蒙版管道</div>
              <div class="text-[9.5px] text-slate-400 font-mono">GPU MULTI-LAYER COMPOSITOR</div>
            </div>
          </div>
          <span class="text-[10px] font-mono text-emerald-600 font-bold bg-emerald-50 px-2 py-1 rounded-lg">ZERO_JITTER</span>
        </div>
      </div>

      <!-- 4. 发动机环绕总成 03 (左侧) · 24H 空间感知与事件调度总线 -->
      <div id="module-timeline" class="exploded-module absolute z-20 bg-white/95 backdrop-blur-md p-5 rounded-3xl border border-indigo-200/80 shadow-xl glow-indigo cursor-pointer" style="left: 1840px; top: 1580px; width: 660px;" onclick="inspectComponent('timeline')">
        <div class="flex items-center justify-between border-b border-slate-100 pb-3 mb-3">
          <div class="flex items-center gap-2.5">
            <span class="w-8 h-8 rounded-xl bg-indigo-50 border border-indigo-200 flex items-center justify-center text-base">⏳</span>
            <div>
              <h3 class="font-black text-slate-900 text-sm">24H 空间感知与事件调度总线 (11 部件负载)</h3>
              <span class="text-[10px] font-mono text-indigo-600 font-bold">[ASM-03 · 24H SPATIAL TIMELINE EVENT DISPATCH BUS]</span>
            </div>
          </div>
          <span class="text-[10px] px-2.5 py-0.5 rounded-full bg-indigo-50 text-indigo-700 font-mono font-bold">11 NODES ACTIVE</span>
        </div>

        <div id="timeline-scroll-list" class="space-y-2 max-h-[720px] overflow-y-auto pr-2">
          <!-- 11 items rendered via JS -->
        </div>
      </div>

      <!-- 5. 发动机环绕总成 04 (右侧) · 双梯形 Bento 交互机能矩阵 -->
      <div id="module-bento" class="exploded-module absolute z-20 bg-white/95 backdrop-blur-md p-5 rounded-3xl border border-amber-200/80 shadow-xl glow-amber cursor-pointer" style="left: 3120px; top: 1580px; width: 560px;" onclick="inspectComponent('bento')">
        <div class="flex items-center justify-between border-b border-slate-100 pb-3 mb-4">
          <div class="flex items-center gap-2.5">
            <span class="w-8 h-8 rounded-xl bg-amber-50 border border-amber-200 flex items-center justify-center text-base">📐</span>
            <div>
              <h3 class="font-black text-slate-900 text-sm">双梯形 Bento 几何裁切与动力学矩阵</h3>
              <span class="text-[10px] font-mono text-amber-600 font-bold">[ASM-04 · TRAPEZOID GEOMETRIC SHADER & PHYSICS HUB]</span>
            </div>
          </div>
          <span class="text-[10px] px-2 py-0.5 rounded-full bg-amber-50 text-amber-700 font-mono font-bold">θ = 10.3°</span>
        </div>

        <div class="grid grid-cols-2 gap-4 mb-4">
          <!-- Left Trapezoid -->
          <div class="p-3.5 rounded-2xl bg-slate-50 border border-slate-200 flex flex-col justify-between">
            <div class="flex items-center gap-2 mb-2">
              <img src="./assets/app_assets/ui_icons/ic_btn_trophy.png" class="w-6 h-6 object-contain" alt="奖杯">
              <div>
                <div class="text-xs font-black text-slate-800">左梯形 · 排行榜加权计算引擎</div>
                <div class="text-[9px] text-slate-400 font-mono">Top: 124px / Base: 160px</div>
              </div>
            </div>

            <div class="relative w-full h-24 my-2 flex items-end justify-center">
              <div class="absolute inset-0 flex items-center justify-around z-20">
                <div class="flex flex-col items-center">
                  <img src="./assets/app_assets/avatars/avatar_xiaobai.png" class="w-6 h-6 rounded-full ring-2 ring-slate-200" alt="晓白">
                  <span class="text-[9px] font-bold text-slate-600 mt-0.5">RANK 02</span>
                </div>
                <div class="flex flex-col items-center -translate-y-2">
                  <img src="./assets/app_assets/avatars/avatar_lex.png" class="w-8 h-8 rounded-full ring-2 ring-amber-400" alt="Lex">
                  <span class="text-[10px] font-black text-slate-800 mt-0.5 font-mono">TOP 01 👑</span>
                </div>
                <div class="flex flex-col items-center">
                  <img src="./assets/app_assets/avatars/avatar_linyi.png" class="w-6 h-6 rounded-full ring-2 ring-amber-700/40" alt="林亦">
                  <span class="text-[9px] font-bold text-slate-600 mt-0.5">RANK 03</span>
                </div>
              </div>
              <img src="./assets/app_assets/generated/podium_3d.png" class="w-full h-auto object-contain z-10 opacity-70" alt="领奖台">
            </div>

            <div class="text-[10px] text-slate-500 bg-white p-2 rounded-xl border border-slate-200 font-mono">
              <span>WEIGHTED_SCORE: 86.0 PTS</span>
            </div>
          </div>

          <!-- Right Trapezoid -->
          <div class="p-3.5 rounded-2xl bg-slate-50 border border-slate-200 flex flex-col justify-between">
            <div class="flex items-center gap-2 mb-2">
              <img src="./assets/app_assets/ic_tile_journal.png" class="w-6 h-6 object-contain" alt="档案">
              <div>
                <div class="text-xs font-black text-slate-800">右梯形 · 结构化日记存储子系统</div>
                <div class="text-[9px] text-slate-400 font-mono">Top: 160px / Base: 124px</div>
              </div>
            </div>

            <div class="relative w-full h-24 my-2 flex items-center justify-center bg-white rounded-xl border border-slate-200 p-2 overflow-hidden">
              <img src="./assets/app_assets/hero_cat_sitting_tight.png" class="h-16 object-contain drop-shadow-sm" alt="老马">
              <div class="absolute bottom-1 right-2 px-1.5 py-0.2 rounded bg-amber-500/10 text-amber-700 font-mono text-[8.5px]">
                DRAGGABLE_SPRITE
              </div>
            </div>

            <div class="text-[10px] text-slate-500 bg-white p-2 rounded-xl border border-slate-200 font-mono">
              <span>STORAGE: 7 PERSISTENT LOGS</span>
            </div>
          </div>
        </div>

        <div class="p-2.5 rounded-xl bg-slate-50 border border-slate-200 text-[10px] font-mono text-slate-600 flex items-center justify-between">
          <span>SEAM_TOLERANCE: 14.0px ±0.1</span>
          <span>CORNER_RADIUS: R18.0px</span>
          <span>STROKE: 1.5px WHITE_SPECULAR</span>
        </div>
      </div>

      <!-- ===================================================================== -->
      <!-- ZONE EAST (东侧总成 · X: 3780) · 8 张真机高分辨率运行工况验证矩阵 -->
      <!-- ===================================================================== -->
      <div id="zone-screens" class="absolute z-20 bg-white/95 backdrop-blur-md p-8 rounded-3xl border border-slate-300/80 shadow-xl" style="left: 3780px; top: 1120px; width: 1680px;">
        <div class="flex items-center justify-between border-b border-slate-200 pb-4 mb-6">
          <div class="flex items-center gap-3">
            <span class="w-10 h-10 rounded-2xl bg-blue-50 border border-blue-200 flex items-center justify-center text-xl">📱</span>
            <div>
              <h2 class="text-lg font-black text-slate-900 tracking-tight">原生设备真机运行工况验证矩阵 (8 组独立工况流)</h2>
              <span class="text-xs font-mono text-blue-600 font-bold">[ZONE-EAST · 8 HARDWARE VERIFICATION CAPTURES · 1320 × 2868]</span>
            </div>
          </div>
          <div class="flex items-center gap-2">
            <span class="text-xs font-mono text-slate-400">HARDWARE RUNTIME TELEMETRY</span>
            <span class="text-xs px-2.5 py-1 rounded-full bg-blue-50 text-blue-700 font-mono font-bold border border-blue-200">8/8 PASSED</span>
          </div>
        </div>

        <!-- 8 Screenshots Grid (2 Rows x 4 Columns) -->
        <div class="grid grid-cols-4 gap-6">
          
          <!-- 1 -->
          <div class="bg-slate-50 rounded-2xl p-3 border border-slate-200">
            <img src="./assets/screenshots/Screenshot_20260919_174540_com_lyi_laomayoyo_MainActivity.JPG" class="w-full h-auto rounded-xl shadow-xs mb-2 cursor-pointer hover:scale-105 transition-transform" alt="工况1" onclick="inspectImage(this.src, '01 初始稳态装配流 (17:45:40)')">
            <div class="text-xs font-black text-slate-800 font-mono">RUN-01: 初始全景渲染装配态</div>
            <div class="text-[10px] text-slate-500 font-mono mt-0.5">MEM: 48.2MB · FPS: 60 · SNAP: NODE-0</div>
          </div>

          <!-- 2 -->
          <div class="bg-slate-50 rounded-2xl p-3 border border-slate-200">
            <img src="./assets/screenshots/Screenshot_20260919_174600_com_lyi_laomayoyo_MainActivity.JPG" class="w-full h-auto rounded-xl shadow-xs mb-2 cursor-pointer hover:scale-105 transition-transform" alt="工况2" onclick="inspectImage(this.src, '02 手势滑动时间轴卡片展开 (17:46:00)')">
            <div class="text-xs font-black text-slate-800 font-mono">RUN-02: 物理手势阻尼位移展开</div>
            <div class="text-[10px] text-slate-500 font-mono mt-0.5">DAMPING: 0.94 · SNAP_LATENCY: 12ms</div>
          </div>

          <!-- 3 -->
          <div class="bg-slate-50 rounded-2xl p-3 border border-slate-200">
            <img src="./assets/screenshots/Screenshot_20260919_174613_com_lyi_laomayoyo_MainActivity.JPG" class="w-full h-auto rounded-xl shadow-xs mb-2 cursor-pointer hover:scale-105 transition-transform" alt="工况3" onclick="inspectImage(this.src, '03 屏幕轻抚触控微反馈 (17:46:13)')">
            <div class="text-xs font-black text-slate-800 font-mono">RUN-03: 触控多点采样与动效响应</div>
            <div class="text-[10px] text-slate-500 font-mono mt-0.5">TOUCH_POINTS: 1 · AUDIO_SYNC: < 5ms</div>
          </div>

          <!-- 4 -->
          <div class="bg-slate-50 rounded-2xl p-3 border border-slate-200">
            <img src="./assets/screenshots/Screenshot_20260919_174628_com_lyi_laomayoyo_MainActivity.JPG" class="w-full h-auto rounded-xl shadow-xs mb-2 cursor-pointer hover:scale-105 transition-transform" alt="工况4" onclick="inspectImage(this.src, '04 状态机指标动态重算 (17:46:28)')">
            <div class="text-xs font-black text-slate-800 font-mono">RUN-04: FSM 指标动态重算工况</div>
            <div class="text-[10px] text-slate-500 font-mono mt-0.5">SCORE_RECALC: +4.2% · FPS: 59.8</div>
          </div>

          <!-- 5 -->
          <div class="bg-slate-50 rounded-2xl p-3 border border-slate-200">
            <img src="./assets/screenshots/Screenshot_20260919_174648_com_lyi_laomayoyo_MainActivity.JPG" class="w-full h-auto rounded-xl shadow-xs mb-2 cursor-pointer hover:scale-105 transition-transform" alt="工况5" onclick="inspectImage(this.src, '05 传感器阈值脏污中断触发 (17:46:48)')">
            <div class="text-xs font-black text-slate-800 font-mono">RUN-05: 传感器阈值中断触发</div>
            <div class="text-[10px] text-slate-500 font-mono mt-0.5">EVENT: SENSOR_DIRTY · DISPATCH: GAODE</div>
          </div>

          <!-- 6 -->
          <div class="bg-slate-50 rounded-2xl p-3 border border-slate-200">
            <img src="./assets/screenshots/Screenshot_20260919_174700_com_lyi_laomayoyo_MainActivity.JPG" class="w-full h-auto rounded-xl shadow-xs mb-2 cursor-pointer hover:scale-105 transition-transform" alt="工况6" onclick="inspectImage(this.src, '06 排行榜二级渲染层 (17:47:00)')">
            <div class="text-xs font-black text-slate-800 font-mono">RUN-06: 3D 领奖台二级页面渲染</div>
            <div class="text-[10px] text-slate-500 font-mono mt-0.5">TRANSITION: 380ms CUBIC_BEZIER</div>
          </div>

          <!-- 7 -->
          <div class="bg-slate-50 rounded-2xl p-3 border border-slate-200">
            <img src="./assets/screenshots/Screenshot_20260919_174713_com_lyi_laomayoyo_MainActivity.JPG" class="w-full h-auto rounded-xl shadow-xs mb-2 cursor-pointer hover:scale-105 transition-transform" alt="工况7" onclick="inspectImage(this.src, '07 结构化时序日记二级容器 (17:47:13)')">
            <div class="text-xs font-black text-slate-800 font-mono">RUN-07: 时序结构化存储容器展开</div>
            <div class="text-[10px] text-slate-500 font-mono mt-0.5">DB_RECORDS: 7 · SCROLL_FPS: 60</div>
          </div>

          <!-- 8 -->
          <div class="bg-slate-50 rounded-2xl p-3 border border-slate-200">
            <img src="./assets/screenshots/Screenshot_20260919_174724_com_lyi_laomayoyo_MainActivity.JPG" class="w-full h-auto rounded-xl shadow-xs mb-2 cursor-pointer hover:scale-105 transition-transform" alt="工况8" onclick="inspectImage(this.src, '08 动态高度内容卡片排版 (17:47:24)')">
            <div class="text-xs font-black text-slate-800 font-mono">RUN-08: 自适应高度卡片排版计算</div>
            <div class="text-[10px] text-slate-500 font-mono mt-0.5">AUTO_LAYOUT_H: DYNAMIC · NO_CLIP</div>
          </div>

        </div>
      </div>

      <!-- ===================================================================== -->
      <!-- ZONE WEST (西侧总成 · X: 240) · 全量工程零部件物料清单 (BOM) -->
      <!-- ===================================================================== -->
      <div id="zone-bom" class="absolute z-20 bg-white/95 backdrop-blur-md p-8 rounded-3xl border border-slate-300/80 shadow-xl" style="left: 240px; top: 1120px; width: 1520px;">
        <div class="flex items-center justify-between border-b border-slate-200 pb-4 mb-6">
          <div class="flex items-center gap-3">
            <span class="w-10 h-10 rounded-2xl bg-indigo-50 border border-indigo-200 flex items-center justify-center text-xl">📦</span>
            <div>
              <h2 class="text-lg font-black text-slate-900 tracking-tight">工程物料清单与全量数字资产规格墙 (Engineering BOM)</h2>
              <span class="text-xs font-mono text-indigo-600 font-bold">[ZONE-WEST · 100% DISCLOSED BILL OF MATERIALS & TELEMETRY]</span>
            </div>
          </div>
          <span class="text-xs px-2.5 py-1 rounded-full bg-indigo-50 text-indigo-700 font-mono font-bold border border-indigo-200">TOTAL: 42 ASSETS</span>
        </div>

        <!-- 11 Board Items Grid -->
        <div class="mb-6">
          <h3 class="text-xs font-black text-slate-700 font-mono mb-3 uppercase tracking-wider">🔹 11 大 3D 照护事件道具部件 (/assets/app_assets/ic_board_*.png)</h3>
          <div id="unified-bom-items" class="grid grid-cols-6 gap-3">
            <!-- Rendered via JS -->
          </div>
        </div>

        <!-- UI Icons & Action Buttons -->
        <div class="mb-6">
          <h3 class="text-xs font-black text-slate-700 font-mono mb-3 uppercase tracking-wider">🔹 交互控件、指标微动效与功能磁贴</h3>
          <div id="unified-bom-icons" class="grid grid-cols-6 gap-3">
            <!-- Rendered via JS -->
          </div>
        </div>

        <!-- 7 Archive Cards -->
        <div>
          <h3 class="text-xs font-black text-slate-700 font-mono mb-3 uppercase tracking-wider">🔹 结构化持久存储卡片 163-169 全量物料</h3>
          <div id="unified-bom-archives" class="grid grid-cols-7 gap-3">
            <!-- Rendered via JS -->
          </div>
        </div>
      </div>

      <!-- ===================================================================== -->
      <!-- ZONE SOUTH (南侧总成 · Y: 2550) · 产研 14 人工程职能与代码交付架构 -->
      <!-- ===================================================================== -->
      <div id="zone-team" class="absolute z-20 bg-white/95 backdrop-blur-md p-8 rounded-3xl border border-slate-300/80 shadow-xl" style="left: 1700px; top: 2550px; width: 2200px;">
        <div class="flex items-center justify-between border-b border-slate-200 pb-4 mb-6">
          <div class="flex items-center gap-3">
            <span class="w-10 h-10 rounded-2xl bg-blue-50 border border-blue-200 flex items-center justify-center text-xl">👥</span>
            <div>
              <h2 class="text-lg font-black text-slate-900 tracking-tight">产研 14 人技术工程矩阵与系统职能拓扑</h2>
              <span class="text-xs font-mono text-blue-600 font-bold">[ZONE-SOUTH · 14 REAL CORE CONTRIBUTORS & SYSTEM RESPONSIBILITIES]</span>
            </div>
          </div>
          <div class="flex items-center gap-2">
            <span class="text-xs font-mono text-slate-400">ENGINEERING PERSONNEL SPECIFICATION</span>
            <span class="text-xs px-2.5 py-1 rounded-full bg-emerald-50 text-emerald-700 font-mono font-bold border border-emerald-200">14 MODULE OWNERS</span>
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
          <h3 class="font-black text-slate-900 text-sm" id="insp-title">工程零部件规格检视</h3>
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
            <span class="text-slate-400">物料标识:</span>
            <span class="font-bold text-slate-800" id="insp-name">软针气垫梳部件</span>
          </div>
          <div class="flex items-center justify-between">
            <span class="text-slate-400">资源路径:</span>
            <span class="font-mono text-[10.5px] text-slate-600 truncate max-w-[220px]" id="insp-path">/assets/...</span>
          </div>
          <div class="flex items-center justify-between">
            <span class="text-slate-400">资产规范:</span>
            <span class="font-mono text-blue-600 font-bold" id="insp-type">3D Handcrafted Alpha PNG</span>
          </div>
          <div class="flex items-center justify-between">
            <span class="text-slate-400">责任架构师:</span>
            <span class="font-bold text-slate-800" id="insp-author">黑黑 / 阿杰</span>
          </div>
        </div>
      </div>

      <div class="space-y-2">
        <h4 class="text-xs font-black text-slate-800 uppercase font-mono tracking-wider">系统事件负载 (Event Payload)</h4>
        <p class="text-xs text-slate-600 leading-relaxed bg-slate-50 p-3.5 rounded-2xl border border-slate-200 font-mono" id="insp-desc">
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
    // 1. Data Store (Pure Technical Payload)
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
      { name: '柯子杰', alias: '阿杰', role: '视觉工程总监', avatar: './assets/app_assets/avatars/avatar_ajie.png', desc: '全套 3D 物品图标建模、设计规范 Token 系统与高光 Shader 渲染管线。' },
      { name: '琮宇', alias: 'Howwoy', role: '原生交互系统', avatar: './assets/app_assets/avatars/avatar_congyu.png', desc: 'Android WebView 混合容器架设，手势触控与物理惯性回弹动力学引擎。' },
      { name: '方晟', alias: 'farest', role: '系统架构师', avatar: './assets/app_assets/avatars/avatar_fangsheng.png', desc: '有限状态机 (FSM) 架构定义、多媒体工况流转协议与系统事件总线。' },
      { name: '传鹏', alias: '阿鹏', role: '硬件协同工程', avatar: './assets/app_assets/avatars/avatar_bingo.png', desc: '智能传感器硬件对接、端侧多通道信号采集与低功耗监听模块。' },
      { name: '张桂滨', alias: 'Gbin', role: '外设集成工程', avatar: './assets/app_assets/avatars/avatar_congyu.png', desc: '外设蓝牙广播与低功耗监听，端侧多模态协同实现。' },
      { name: '帅华', alias: '小六', role: '3D 动效渲染', avatar: './assets/app_assets/avatars/avatar_xiaoliu.png', desc: '3D 领奖台与物理粒子动效开发，着色器优化与 60fps 恒定锁帧保障。' },
      { name: '天鸣', alias: '木子', role: '系统产品架构', avatar: './assets/app_assets/avatars/avatar_muzi.png', desc: '24H 空间感知时间轴业务拓扑规划、指标衰减算法与行为状态流建模。' },
      { name: '王斌', alias: 'Bingo', role: 'AI 系统工程', avatar: './assets/app_assets/avatars/avatar_bingo.png', desc: '荣耀 YOYO 智能体核心接入、本地模型端侧决策网络、端云协同总线。' },
      { name: '家源', alias: 'ImYrS', role: '安全与质量保障', avatar: './assets/app_assets/avatars/avatar_imyrs.png', desc: '端侧自动化测试管线、极限并发压测、内存泄漏与防熔断治理。' },
      { name: '刘旭', alias: 'Lex', role: '数据服务架构', avatar: './assets/app_assets/avatars/avatar_lex.png', desc: '高并发爱猫排行榜加权算法、飞书数据机器人联动与日志同步。' },
      { name: '爱德', alias: 'Adam', role: '微几何与交互规范', avatar: './assets/app_assets/avatars/avatar_adam.png', desc: '圆角梯形交互剪裁规范、微纹理混合模式与卡片视差设计。' },
      { name: '黑黑', alias: '黑黑', role: '系统测试与工程验证', avatar: './assets/app_assets/avatars/avatar_heihei.png', desc: '真机环境数据标定、多工况传感器模拟信号注入与系统稳态测试。' },
      { name: '嘉浩', alias: '加号', role: '算法工程师', avatar: './assets/app_assets/avatars/avatar_jiahao.png', desc: '多模态行为感知模型、猫咪健康状态预测算法工程化。' },
      { name: '栾屹', alias: '林亦', role: '总架构师 / 负责人', avatar: './assets/app_assets/avatars/avatar_linyi.png', desc: '老马端侧智能体全工程总体规划与技术决策总舵。' }
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
    viewport.addEventListener('wheel', (e) => {
      e.preventDefault();

      if (e.ctrlKey) {
        // macOS Pinch-to-zoom on trackpad!
        const rect = viewport.getBoundingClientRect();
        const cursorX = e.clientX - rect.left;
        const cursorY = e.clientY - rect.top;
        const prevScale = zoomScale;
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

      const startPanX = panX;
      const startPanY = panY;
      const startScale = zoomScale;
      const startTime = performance.now();
      const duration = 550;

      function anim(time) {
        const elapsed = time - startTime;
        const progress = Math.min(1, elapsed / duration);
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

      const conns = [
        { id: 'module-gauges', color: '#0891B2', from: 'right', to: { x: coreX + 80, y: coreY + 40 } },
        { id: 'module-media', color: '#059669', from: 'left', to: { x: coreX + 310, y: coreY + 120 } },
        { id: 'module-timeline', color: '#4F46E5', from: 'right', to: { x: coreX + 20, y: coreY + 420 } },
        { id: 'module-bento', color: '#D97706', from: 'left', to: { x: coreX + 370, y: coreY + 640 } }
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
          btn.className = `px-2.5 py-1 rounded-lg text-[11px] font-black font-mono transition-all shadow-2xs flex items-center gap-1 ${
            s === 'normal' ? 'bg-emerald-600 text-white' : s === 'dirty' ? 'bg-amber-600 text-white' : 'bg-rose-600 text-white'
          }`;
        } else {
          btn.className = 'px-2.5 py-1 rounded-lg text-[11px] font-black font-mono transition-all text-slate-600 hover:bg-slate-200 flex items-center gap-1';
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
                <span class="text-xs font-black text-slate-900 font-mono">${it.time} · ${it.title}</span>
                <div class="flex items-center gap-1.5">
                  <img src="${it.avatar}" class="w-4 h-4 rounded-full object-cover" alt="${it.person}">
                  <span class="text-[10px] font-bold text-slate-600 font-mono">${it.person}</span>
                </div>
              </div>
              <p class="text-[10.5px] text-slate-500 mt-1 leading-relaxed font-mono">${it.desc}</p>
            </div>
          </div>
        `;
      });
      container.innerHTML = html;
    }

    function populateBOM() {
      const bContainer = document.getElementById('unified-bom-items');
      let bHtml = '';
      SCHEDULE_DATA.forEach(it => {
        bHtml += `
          <div class="bg-slate-50 p-3 rounded-2xl border border-slate-200 hover:border-indigo-400 transition-all flex flex-col items-center text-center cursor-pointer" onclick="inspectItem(${it.id})">
            <img src="${it.icon}" class="w-12 h-12 object-contain mb-1.5 drop-shadow-2xs" alt="${it.title}">
            <span class="text-[11px] font-black text-slate-800 truncate w-full font-mono">${it.title}</span>
            <span class="text-[9px] text-slate-400 font-mono mt-0.5">${it.time} · ${it.person}</span>
          </div>
        `;
      });
      bContainer.innerHTML = bHtml;

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
            <span class="text-[11px] font-black text-slate-800 truncate w-full font-mono">${ui.title}</span>
            <span class="text-[9px] text-slate-400 font-mono mt-0.5 truncate w-full">${ui.name}</span>
          </div>
        `;
      });
      uContainer.innerHTML = uHtml;

      const aContainer = document.getElementById('unified-bom-archives');
      let aHtml = '';
      [163, 164, 165, 166, 167, 168, 169].forEach(id => {
        aHtml += `
          <div class="bg-slate-50 p-2.5 rounded-2xl border border-slate-200 hover:border-indigo-400 transition-all">
            <img src="./assets/app_assets/archives/archive_${id}.png" class="w-full h-auto rounded-xl object-cover mb-1.5 cursor-pointer hover:scale-105 transition-transform" alt="手账${id}" onclick="inspectImage(this.src, '持久化数据记录 #${id}')">
            <div class="text-[10px] font-bold text-slate-700 text-center font-mono">RECORD #${id}</div>
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
            <span class="text-xs font-black text-slate-900 font-mono">${m.alias} <span class="text-[10px] font-normal text-slate-400">(${m.name})</span></span>
            <span class="text-[10px] font-bold text-blue-600 mt-0.5 font-mono">${m.role}</span>
            <span class="text-[9px] text-slate-400 mt-1 leading-relaxed font-mono">${m.desc}</span>
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
        titleEl.textContent = '状态感知与生命指标控制系统';
        tagEl.textContent = '[ASM-01 · SENSORS]';
        imgEl.src = './assets/app_assets/ui_icons/ic_index_catlove.png';
        nameEl.textContent = 'HUD 生命力与加权爱猫指数计算模型';
        pathEl.textContent = '/assets/app_assets/ui_icons/ic_index_*.png';
        typeEl.textContent = 'Vector SVG / Alpha PNG 采样流';
        authorEl.textContent = '阿杰 (视觉工程) / Lex (数据服务)';
        descEl.textContent = '端侧 1000ms 心跳轮询驱动。包含快乐指数滤波方程、脏污预警阈值判定算法与加权爱猫积分模型。';
      } else if (type === 'media') {
        titleEl.textContent = '视觉多媒体硬件解码与动效管线';
        tagEl.textContent = '[ASM-02 · MEDIA PIPELINE]';
        imgEl.src = './assets/app_assets/hero_cat_sitting_tight.png';
        nameEl.textContent = '1080P 60FPS 硬解多媒体流';
        pathEl.textContent = '/assets/app_assets/home_cat_*.mp4';
        typeEl.textContent = 'H.264 High Profile 硬件解码流';
        authorEl.textContent = '小六 (动效工程) / Bingo (系统架构)';
        descEl.textContent = '三组无缝切换硬解短视频流水线，Alpha 通道图层混合技术与 60fps 恒定锁帧保障。';
      } else if (type === 'timeline') {
        titleEl.textContent = '24H 空间感知与事件调度总线';
        tagEl.textContent = '[ASM-03 · TIMELINE 11 ITEMS]';
        imgEl.src = './assets/app_assets/ic_board_brush.png';
        nameEl.textContent = '11 大 3D 照护事件道具部件';
        pathEl.textContent = '/assets/app_assets/ic_board_*.png';
        typeEl.textContent = '3D 拟物渲染无损 Alpha 通道';
        authorEl.textContent = '阿杰 (视觉工程) / 木子 (产品架构)';
        descEl.textContent = '24 小时事件调度总线，支持时间触发、地理围栏触发与端侧设备低功耗轮询监听。';
      } else if (type === 'bento') {
        titleEl.textContent = '双梯形 Bento 几何裁切与动力学矩阵';
        tagEl.textContent = '[ASM-04 · TRAPEZOID SHADER]';
        imgEl.src = './assets/app_assets/ui_icons/ic_btn_trophy.png';
        nameEl.textContent = '10.3° 倾角圆角直角双梯形着色器';
        pathEl.textContent = 'SVG ClipPath + DropShadow 硬件加速';
        typeEl.textContent = '硬件级矢量边缘裁切与混合模式';
        authorEl.textContent = 'Adam (交互设计) / Howwoy (原生交互)';
        descEl.textContent = '左梯形承载实时加权排行榜，右梯形承载持久化日记系统；边缘 14.0px 精密贴合公差。';
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
      document.getElementById('insp-type').textContent = '24H 空间事件道具负载';
      document.getElementById('insp-author').textContent = `${it.person} (模块责任人)`;
      document.getElementById('insp-desc').textContent = it.desc;
      drawer.classList.remove('translate-x-[460px]');
    }

    function inspectMember(alias) {
      const mem = TEAM_MEMBERS.find(m => m.alias.toLowerCase() === alias.toLowerCase());
      if (!mem) return;
      const drawer = document.getElementById('inspector-drawer');
      document.getElementById('insp-title').textContent = `${mem.alias} (${mem.name})`;
      document.getElementById('insp-tag').textContent = `[ENGINEER-${mem.alias.toUpperCase()}]`;
      document.getElementById('insp-img').src = mem.avatar;
      document.getElementById('insp-name').textContent = mem.role;
      document.getElementById('insp-path').textContent = mem.avatar;
      document.getElementById('insp-type').textContent = '核心架构成员';
      document.getElementById('insp-author').textContent = `${mem.name} · ${mem.alias}`;
      document.getElementById('insp-desc').textContent = mem.desc;
      drawer.classList.remove('translate-x-[460px]');
    }

    function inspectImage(src, title) {
      const drawer = document.getElementById('inspector-drawer');
      document.getElementById('insp-title').textContent = title;
      document.getElementById('insp-tag').textContent = '[HARDWARE TELEMETRY]';
      document.getElementById('insp-img').src = src;
      document.getElementById('insp-name').textContent = title;
      document.getElementById('insp-path').textContent = src;
      document.getElementById('insp-type').textContent = '1320 × 2868 Native Telemetry';
      document.getElementById('insp-author').textContent = '真机环境实测采样';
      document.getElementById('insp-desc').textContent = '真机运行状态验证截屏，证明端侧混合容器在复杂物理手势与多图层合成下的渲染稳态。';
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

print("Tech master index.html generated successfully!")
