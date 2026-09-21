import json
import os

html_content = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>老马喵务局 · 荣耀 YOYO 智能体 | 发动机全景工程有机拆解系统</title>
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
              cyan: '#06B6D4',
              emerald: '#10B981',
              amber: '#F59E0B',
              rose: '#F43F5E',
              indigo: '#6366F1'
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
      background-size: 24px 24px;
    }
    .bg-blueprint-grid-dense {
      background-image: radial-gradient(#94A3B8 0.8px, transparent 0.8px);
      background-size: 12px 12px;
    }
    /* Smooth pan/zoom canvas */
    #canvas-container {
      cursor: grab;
      user-select: none;
    }
    #canvas-container:active {
      cursor: grabbing;
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
    /* Dynamic leader lines */
    .leader-line {
      pointer-events: none;
      transition: stroke-dashoffset 0.3s ease;
    }
    /* Exploded module cards */
    .exploded-module {
      transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.3s ease;
    }
    /* Glow highlights */
    .glow-cyan {
      box-shadow: 0 0 25px -5px rgba(6, 182, 212, 0.25);
    }
    .glow-amber {
      box-shadow: 0 0 25px -5px rgba(245, 158, 11, 0.25);
    }
    .glow-emerald {
      box-shadow: 0 0 25px -5px rgba(16, 185, 129, 0.25);
    }
    .glow-indigo {
      box-shadow: 0 0 25px -5px rgba(99, 102, 241, 0.25);
    }
  </style>
</head>
<body class="bg-slate-100 text-slate-800 antialiased overflow-hidden font-sans h-screen flex flex-col">

  <!-- ========================================================================= -->
  <!-- 顶部 HUD 导航栏 (Top Engineering Header & Global Control Center) -->
  <!-- ========================================================================= -->
  <header class="h-16 bg-white/90 backdrop-blur-md border-b border-slate-200 px-6 flex items-center justify-between z-50 shrink-0 shadow-xs">
    <!-- Left: Authentic Logo & Project Specs -->
    <div class="flex items-center gap-4">
      <div class="relative w-11 h-11 rounded-2xl overflow-hidden shadow-md ring-2 ring-blue-500/20 bg-slate-900 shrink-0 flex items-center justify-center">
        <img src="./assets/app_assets/app_icon_preview.png" alt="老马" class="w-full h-full object-cover">
        <div class="absolute inset-0 ring-1 ring-inset ring-white/30 rounded-2xl"></div>
      </div>
      <div>
        <div class="flex items-center gap-2">
          <h1 class="font-black text-slate-900 text-base tracking-tight flex items-center gap-2">
            <span>老马喵务局</span>
            <span class="text-xs px-2 py-0.5 rounded-md bg-blue-50 text-blue-600 font-bold border border-blue-200/60 font-mono">荣耀 YOYO 智能体</span>
          </h1>
          <span class="text-[11px] px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-700 font-medium border border-emerald-200/80 flex items-center gap-1">
            <span class="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-pulse"></span>
            100% 正版素材拆解
          </span>
        </div>
        <p class="text-[11px] text-slate-500 font-medium flex items-center gap-2 mt-0.5">
          <span>选题汇报全历程</span>
          <span class="text-slate-300">|</span>
          <span class="font-mono text-slate-600 font-bold">ENGINE EXPLODED ARCHITECTURE · 发动机有机全景工程拆解</span>
        </p>
      </div>
    </div>

    <!-- Center: Main Navigation Tabs -->
    <div class="flex items-center bg-slate-100/90 p-1 rounded-xl border border-slate-200">
      <button onclick="switchTab('exploded')" id="tab-btn-exploded" class="tab-btn px-4 py-1.5 rounded-lg text-xs font-bold text-blue-700 bg-white shadow-xs transition-all flex items-center gap-1.5">
        <span>⚙️</span>
        <span>发动机全景拆解</span>
        <span class="px-1.5 py-0.2 text-[9px] font-mono rounded bg-blue-100 text-blue-800">EXPLODED</span>
      </button>
      <button onclick="switchTab('screens')" id="tab-btn-screens" class="tab-btn px-4 py-1.5 rounded-lg text-xs font-bold text-slate-600 hover:text-slate-900 transition-all flex items-center gap-1.5">
        <span>📱</span>
        <span>真机运行多态 (8图+3视频)</span>
      </button>
      <button onclick="switchTab('bom')" id="tab-btn-bom" class="tab-btn px-4 py-1.5 rounded-lg text-xs font-bold text-slate-600 hover:text-slate-900 transition-all flex items-center gap-1.5">
        <span>📦</span>
        <span>全量零部件清单 (BOM)</span>
      </button>
      <button onclick="switchTab('team')" id="tab-btn-team" class="tab-btn px-4 py-1.5 rounded-lg text-xs font-bold text-slate-600 hover:text-slate-900 transition-all flex items-center gap-1.5">
        <span>👥</span>
        <span>真实研创14人图谱</span>
      </button>
      <button onclick="switchTab('milestones')" id="tab-btn-milestones" class="tab-btn px-4 py-1.5 rounded-lg text-xs font-bold text-slate-600 hover:text-slate-900 transition-all flex items-center gap-1.5">
        <span>📜</span>
        <span>开发历程与架构</span>
      </button>
    </div>

    <!-- Right: Exploded Controls & Fullscreen -->
    <div class="flex items-center gap-4">
      <!-- Explosion Slider -->
      <div id="explosion-controls" class="flex items-center gap-2.5 bg-slate-50 px-3 py-1.5 rounded-xl border border-slate-200 shadow-2xs">
        <span class="text-[11px] font-bold text-slate-600 flex items-center gap-1">
          <span class="text-xs">💥</span> 拆解幅度:
        </span>
        <input type="range" id="explode-slider" min="0" max="100" value="80" class="w-28 accent-blue-600 cursor-pointer" oninput="updateExplosion(this.value)">
        <span id="explode-val" class="font-mono text-xs font-black text-blue-600 w-9 text-right">80%</span>
      </div>

      <!-- Reset Canvas View -->
      <button onclick="resetCanvasTransform()" class="px-2.5 py-1.5 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-700 text-xs font-bold transition-all border border-slate-200 active:scale-95" title="复位画布居中">
        🎯 复位
      </button>

      <!-- Toggle Leader Lines -->
      <button id="toggle-lines-btn" onclick="toggleLeaderLines()" class="px-2.5 py-1.5 rounded-xl bg-blue-50 text-blue-700 hover:bg-blue-100 text-xs font-bold transition-all border border-blue-200 active:scale-95 flex items-center gap-1">
        <span>🔗</span> 导线开
      </button>
    </div>
  </header>

  <!-- ========================================================================= -->
  <!-- 主内容区域 (Main Content Tabs) -->
  <!-- ========================================================================= -->
  <main class="flex-1 relative overflow-hidden">

    <!-- ----------------------------------------------------------------------- -->
    <!-- TAB 1: 发动机全景有机拆解大屏 (The Engine Exploded Canvas View) -->
    <!-- ----------------------------------------------------------------------- -->
    <div id="view-exploded" class="tab-view w-full h-full relative overflow-hidden bg-blueprint-grid">
      <!-- Floating Canvas Info HUD (左上角工程坐标与提示) -->
      <div class="absolute top-4 left-6 z-40 pointer-events-none flex flex-col gap-1.5">
        <div class="flex items-center gap-2 bg-white/90 backdrop-blur-md px-3 py-1.5 rounded-lg border border-slate-200 shadow-sm">
          <span class="w-2 h-2 rounded-full bg-blue-500 animate-ping"></span>
          <span class="text-xs font-mono font-black text-slate-800">VIEWPORT: <span id="hud-zoom">100%</span></span>
          <span class="text-slate-300">|</span>
          <span class="text-[11px] text-slate-500 font-medium">按住左键拖动画布 · 滚轮自由缩放 · 点击任意零部件查看物料参数</span>
        </div>
        <div class="flex items-center gap-2 text-[10px] text-slate-400 font-mono">
          <span>X: <span id="hud-x">0</span>px</span>
          <span>Y: <span id="hud-y">0</span>px</span>
          <span>COMPONENTS: 38 UNITS</span>
        </div>
      </div>

      <!-- Floating State Selector Capsule (浮动工况切换栏) -->
      <div class="absolute top-4 right-6 z-40 bg-white/95 backdrop-blur-md p-1.5 rounded-2xl border border-slate-200 shadow-md flex items-center gap-1.5">
        <span class="text-[11px] font-bold text-slate-400 pl-2 pr-1">工况状态:</span>
        <button onclick="setGlobalCatState('normal')" id="btn-state-normal" class="state-pill px-3 py-1.5 rounded-xl text-xs font-black transition-all bg-emerald-500 text-white shadow-xs flex items-center gap-1.5">
          <span class="w-2 h-2 rounded-full bg-white animate-pulse"></span>
          <span>活力健康态</span>
        </button>
        <button onclick="setGlobalCatState('dirty')" id="btn-state-dirty" class="state-pill px-3 py-1.5 rounded-xl text-xs font-black transition-all bg-slate-100 text-slate-600 hover:bg-slate-200 flex items-center gap-1.5">
          <span class="w-2 h-2 rounded-full bg-amber-500"></span>
          <span>饥饿脏污态</span>
        </button>
        <button onclick="setGlobalCatState('touch')" id="btn-state-touch" class="state-pill px-3 py-1.5 rounded-xl text-xs font-black transition-all bg-slate-100 text-slate-600 hover:bg-slate-200 flex items-center gap-1.5">
          <span class="w-2 h-2 rounded-full bg-rose-500"></span>
          <span>抚摸互动态</span>
        </button>
      </div>

      <!-- Infinite Interactive Canvas Stage -->
      <div id="canvas-container" class="w-full h-full relative overflow-hidden" onmousedown="startPan(event)" onwheel="handleWheelZoom(event)">
        <!-- Transform Wrapper for Pan & Zoom -->
        <div id="canvas-stage" class="absolute origin-center transition-transform duration-75 ease-out" style="width: 3200px; height: 2200px; left: calc(50% - 1600px); top: calc(50% - 1100px);">
          
          <!-- SVG Leader Lines Layer (Connecting Central Phone to Assemblies) -->
          <svg id="svg-leader-lines" class="absolute inset-0 w-full h-full pointer-events-none z-10" xmlns="http://www.w3.org/2000/svg">
            <!-- Dynamic paths generated via JavaScript -->
          </svg>

          <!-- =============================================================== -->
          <!-- 1. 中央整机装配体 (The Central Core - Honor Device Mockup) -->
          <!-- =============================================================== -->
          <div id="core-device-frame" class="absolute z-30" style="left: 1405px; top: 678px; width: 390px; height: 844px;">
            <!-- Tech Frame Annotation Tag -->
            <div class="absolute -top-7 left-0 right-0 flex items-center justify-between font-mono text-[10px] text-blue-600 font-bold pointer-events-none px-1">
              <span>[CORE-ASM-000] 整机中央总成</span>
              <span>DIM: 390 × 844 (HONOR NATIVE)</span>
            </div>

            <!-- Realistic Phone Outer Shell -->
            <div class="relative w-full h-full rounded-[48px] bg-slate-900 p-3 shadow-2xl ring-1 ring-slate-800 ring-offset-4 ring-offset-slate-200">
              <!-- Titanium Bezel Inner -->
              <div class="relative w-full h-full rounded-[40px] overflow-hidden bg-white flex flex-col border border-slate-700 shadow-inner">
                
                <!-- Dynamic Pill / Camera Notch -->
                <div class="absolute top-2.5 left-1/2 -translate-x-1/2 w-28 h-6 bg-black rounded-full z-50 flex items-center justify-between px-2 text-[10px] text-white">
                  <div class="flex items-center gap-1">
                    <span class="w-2 h-2 rounded-full bg-blue-500 animate-pulse"></span>
                    <span class="text-[8.5px] font-mono font-bold text-blue-300">YOYO</span>
                  </div>
                  <span class="w-2 h-2 rounded-full bg-slate-800 ring-1 ring-slate-700"></span>
                </div>

                <!-- Phone Screen Content (100% Authentic App Representation) -->
                <div class="relative w-full h-full flex flex-col bg-[#F8FAFC] overflow-hidden select-none">
                  
                  <!-- Top Status Bar & Cat Health HUD -->
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

                  <!-- Phone Cat Live Media Stage (Video + Background) -->
                  <div class="relative w-full h-[360px] overflow-hidden bg-slate-200 shrink-0">
                    <!-- Background Image -->
                    <img id="phone-bg-img" src="./assets/app_assets/home_bg_clean.png" class="absolute inset-0 w-full h-full object-cover" alt="背景">
                    
                    <!-- Live Cat Video Player -->
                    <video id="phone-cat-video" src="./assets/app_assets/home_cat_clean.mp4" autoplay loop muted playsinline class="absolute inset-0 w-full h-full object-contain z-10"></video>
                    
                    <!-- Fallback Tap Indicator -->
                    <div class="absolute bottom-3 right-3 z-20 bg-black/40 backdrop-blur-md px-2.5 py-1 rounded-full text-[10px] text-white font-bold flex items-center gap-1">
                      <span>🐾</span> 点击切换工况
                    </div>
                  </div>

                  <!-- Middle Docked Timeline Event Preview -->
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

                  <!-- Bottom Bento Trapezoid Hub in Phone -->
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

          <!-- =============================================================== -->
          <!-- 2. 发动机有机环绕五大总成 (Surrounding Exploded Assemblies) -->
          <!-- =============================================================== -->

          <!-- ------------------------------------------------------------- -->
          <!-- ASSEMBLY 01 (左上) · 状态感知与生命指标仪表总成 (Sensors & Gauges) -->
          <!-- ------------------------------------------------------------- -->
          <div id="module-gauges" class="exploded-module absolute z-20 bg-white/95 backdrop-blur-md p-5 rounded-3xl border border-cyan-200/80 shadow-xl glow-cyan" style="left: 820px; top: 180px; width: 480px;" onclick="inspectComponent('gauges')">
            <!-- Header -->
            <div class="flex items-center justify-between border-b border-slate-100 pb-3 mb-4">
              <div class="flex items-center gap-2.5">
                <span class="w-8 h-8 rounded-xl bg-cyan-50 border border-cyan-200 flex items-center justify-center text-base">📊</span>
                <div>
                  <h3 class="font-black text-slate-900 text-sm">状态感知与生命指标仪表总成</h3>
                  <span class="text-[10px] font-mono text-cyan-600 font-bold">[ASM-01 · SENSORS & STATUS GAUGES]</span>
                </div>
              </div>
              <span class="text-[10px] px-2 py-0.5 rounded-full bg-cyan-50 text-cyan-700 font-mono font-bold">5 UNITS</span>
            </div>

            <!-- Gauges Grid -->
            <div class="grid grid-cols-2 gap-3">
              <!-- Gauge 1: Cat Love Index -->
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

              <!-- Gauge 2: Happiness Master -->
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

              <!-- Gauge 3: Normal Green State -->
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

              <!-- Gauge 4: Hungry / Dirty Orange -->
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

            <!-- Technical Specification Footnote -->
            <div class="mt-3 pt-2.5 border-t border-slate-100 flex items-center justify-between text-[10px] text-slate-500 font-mono">
              <span>刷新频率: 1000ms 端侧心跳</span>
              <span class="text-cyan-600 font-bold">直连中央整机 HUD</span>
            </div>
          </div>

          <!-- ------------------------------------------------------------- -->
          <!-- ASSEMBLY 02 (右上) · 视觉多媒体内核总成 (Visual & Media Engine) -->
          <!-- ------------------------------------------------------------- -->
          <div id="module-media" class="exploded-module absolute z-20 bg-white/95 backdrop-blur-md p-5 rounded-3xl border border-emerald-200/80 shadow-xl glow-emerald" style="left: 1910px; top: 180px; width: 520px;" onclick="inspectComponent('media')">
            <!-- Header -->
            <div class="flex items-center justify-between border-b border-slate-100 pb-3 mb-4">
              <div class="flex items-center gap-2.5">
                <span class="w-8 h-8 rounded-xl bg-emerald-50 border border-emerald-200 flex items-center justify-center text-base">🎬</span>
                <div>
                  <h3 class="font-black text-slate-900 text-sm">视觉多媒体内核与工况视频总成</h3>
                  <span class="text-[10px] font-mono text-emerald-600 font-bold">[ASM-02 · MULTIMEDIA VIDEO & SPRITE ENGINE]</span>
                </div>
              </div>
              <span class="text-[10px] px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-700 font-mono font-bold">3 CLIPS + 5 TILES</span>
            </div>

            <!-- Video State Matrix Cards (3 Videos) -->
            <div class="grid grid-cols-3 gap-2.5 mb-3">
              <!-- Video 1: Clean -->
              <div class="p-2 rounded-2xl bg-slate-50 border border-slate-200 hover:border-emerald-500 transition-all cursor-pointer flex flex-col" onclick="event.stopPropagation(); setGlobalCatState('normal')">
                <div class="relative w-full h-28 rounded-xl overflow-hidden bg-black mb-2">
                  <video src="./assets/app_assets/home_cat_clean.mp4" autoplay loop muted playsinline class="w-full h-full object-cover"></video>
                  <span class="absolute top-1 left-1 px-1.5 py-0.5 rounded bg-emerald-500/80 text-[8px] text-white font-mono font-bold">01 活力健康</span>
                </div>
                <span class="text-[11px] font-black text-slate-800">home_cat_clean</span>
                <span class="text-[9px] text-slate-400 font-mono">1080x1920 · 60fps</span>
              </div>

              <!-- Video 2: Dirty -->
              <div class="p-2 rounded-2xl bg-slate-50 border border-slate-200 hover:border-amber-500 transition-all cursor-pointer flex flex-col" onclick="event.stopPropagation(); setGlobalCatState('dirty')">
                <div class="relative w-full h-28 rounded-xl overflow-hidden bg-black mb-2">
                  <video src="./assets/app_assets/home_cat_dirty.mp4" autoplay loop muted playsinline class="w-full h-full object-cover"></video>
                  <span class="absolute top-1 left-1 px-1.5 py-0.5 rounded bg-amber-500/80 text-[8px] text-white font-mono font-bold">02 饥饿脏污</span>
                </div>
                <span class="text-[11px] font-black text-slate-800">home_cat_dirty</span>
                <span class="text-[9px] text-slate-400 font-mono">1080x1920 · 60fps</span>
              </div>

              <!-- Video 3: Touch -->
              <div class="p-2 rounded-2xl bg-slate-50 border border-slate-200 hover:border-rose-500 transition-all cursor-pointer flex flex-col" onclick="event.stopPropagation(); setGlobalCatState('touch')">
                <div class="relative w-full h-28 rounded-xl overflow-hidden bg-black mb-2">
                  <video src="./assets/app_assets/home_cat_touch.mp4" autoplay loop muted playsinline class="w-full h-full object-cover"></video>
                  <span class="absolute top-1 left-1 px-1.5 py-0.5 rounded bg-rose-500/80 text-[8px] text-white font-mono font-bold">03 抚摸互动</span>
                </div>
                <span class="text-[11px] font-black text-slate-800">home_cat_touch</span>
                <span class="text-[9px] text-slate-400 font-mono">1080x1920 · 60fps</span>
              </div>
            </div>

            <!-- Real Cat Transparent Cutout Gallery -->
            <div class="p-2.5 rounded-2xl bg-slate-50 border border-slate-200 flex items-center justify-between">
              <div class="flex items-center gap-3">
                <div class="w-12 h-12 rounded-xl bg-white border border-slate-200 p-1 flex items-center justify-center">
                  <img src="./assets/app_assets/hero_cat_sitting_tight.png" class="w-full h-full object-contain" alt="老马免抠正坐">
                </div>
                <div class="w-12 h-12 rounded-xl bg-white border border-slate-200 p-1 flex items-center justify-center">
                  <img src="./assets/app_assets/hero_cat_carrier_tight.png" class="w-full h-full object-contain" alt="老马免抠航空箱">
                </div>
                <div>
                  <div class="text-xs font-bold text-slate-800">老马高清透明剪影贴纸</div>
                  <div class="text-[9.5px] text-slate-400">高精度 Alpha 通道免抠图层</div>
                </div>
              </div>
              <span class="text-[10px] font-mono text-emerald-600 font-bold bg-emerald-50 px-2 py-1 rounded-lg">PNG 300DPI</span>
            </div>
          </div>

          <!-- ------------------------------------------------------------- -->
          <!-- ASSEMBLY 03 (左侧) · 24H 空间感知与事件总线 (11 道具零部件物料表) -->
          <!-- ------------------------------------------------------------- -->
          <div id="module-timeline" class="exploded-module absolute z-20 bg-white/95 backdrop-blur-md p-5 rounded-3xl border border-indigo-200/80 shadow-xl glow-indigo" style="left: 680px; top: 720px; width: 620px;" onclick="inspectComponent('timeline')">
            <!-- Header -->
            <div class="flex items-center justify-between border-b border-slate-100 pb-3 mb-3">
              <div class="flex items-center gap-2.5">
                <span class="w-8 h-8 rounded-xl bg-indigo-50 border border-indigo-200 flex items-center justify-center text-base">⏳</span>
                <div>
                  <h3 class="font-black text-slate-900 text-sm">24H 空间感知与事件流总成 (11大道具零部件)</h3>
                  <span class="text-[10px] font-mono text-indigo-600 font-bold">[ASM-03 · 24H SPATIAL TIMELINE & 11 BOARD ITEMS]</span>
                </div>
              </div>
              <span class="text-[10px] px-2.5 py-0.5 rounded-full bg-indigo-50 text-indigo-700 font-mono font-bold">11 ITEMS ALL EXPANDED</span>
            </div>

            <!-- Scrollable List of All 11 Authentic Items -->
            <div class="space-y-2 max-h-[580px] overflow-y-auto pr-2">
              
              <!-- Item 0 -->
              <div class="p-2.5 rounded-2xl bg-slate-50 border border-slate-200/80 hover:border-indigo-500 hover:bg-white transition-all flex items-start gap-3 cursor-pointer" onclick="event.stopPropagation(); inspectItem(0)">
                <div class="w-10 h-10 rounded-xl bg-white border border-slate-200 p-1 flex items-center justify-center shrink-0 shadow-2xs">
                  <img src="./assets/app_assets/ic_board_stethoscope.png" class="w-full h-full object-contain" alt="听诊器">
                </div>
                <div class="flex-1 min-w-0">
                  <div class="flex items-center justify-between">
                    <span class="text-xs font-black text-slate-900">09:14 · 晨间体检巡视</span>
                    <div class="flex items-center gap-1.5">
                      <img src="./assets/app_assets/avatars/avatar_linyi.png" class="w-4 h-4 rounded-full object-cover" alt="林亦">
                      <span class="text-[10px] font-bold text-slate-600">林亦</span>
                    </div>
                  </div>
                  <p class="text-[10.5px] text-slate-500 mt-1 leading-relaxed">全面检查老马眼鼻分泌物，检查耳廓与毛发光泽度，称量晨间空腹体重。</p>
                </div>
              </div>

              <!-- Item 1 -->
              <div class="p-2.5 rounded-2xl bg-slate-50 border border-slate-200/80 hover:border-indigo-500 hover:bg-white transition-all flex items-start gap-3 cursor-pointer" onclick="event.stopPropagation(); inspectItem(1)">
                <div class="w-10 h-10 rounded-xl bg-white border border-slate-200 p-1 flex items-center justify-center shrink-0 shadow-2xs">
                  <img src="./assets/app_assets/ic_board_brush.png" class="w-full h-full object-contain" alt="软毛梳">
                </div>
                <div class="flex-1 min-w-0">
                  <div class="flex items-center justify-between">
                    <span class="text-xs font-black text-slate-900">09:15 · 全身梳毛</span>
                    <div class="flex items-center gap-1.5">
                      <img src="./assets/app_assets/avatars/avatar_heihei.png" class="w-4 h-4 rounded-full object-cover" alt="黑黑">
                      <span class="text-[10px] font-bold text-slate-600">黑黑</span>
                    </div>
                  </div>
                  <p class="text-[10.5px] text-slate-500 mt-1 leading-relaxed">使用软针气垫梳整理背部浮毛，检查颈部毛发光泽；YOYO 同步播报今日进食正常、眼神清澈，养猫指数稳步提升！</p>
                </div>
              </div>

              <!-- Item 2 -->
              <div class="p-2.5 rounded-2xl bg-slate-50 border border-slate-200/80 hover:border-indigo-500 hover:bg-white transition-all flex items-start gap-3 cursor-pointer" onclick="event.stopPropagation(); inspectItem(2)">
                <div class="w-10 h-10 rounded-xl bg-white border border-slate-200 p-1 flex items-center justify-center shrink-0 shadow-2xs">
                  <img src="./assets/app_assets/ic_board_treat.png" class="w-full h-full object-contain" alt="鸡肉冻干">
                </div>
                <div class="flex-1 min-w-0">
                  <div class="flex items-center justify-between">
                    <span class="text-xs font-black text-slate-900">12:43 · 严选鸡肉冻干加餐</span>
                    <div class="flex items-center gap-1.5">
                      <img src="./assets/app_assets/avatars/avatar_bingo.png" class="w-4 h-4 rounded-full object-cover" alt="Bingo">
                      <span class="text-[10px] font-bold text-slate-600">Bingo</span>
                    </div>
                  </div>
                  <p class="text-[10.5px] text-slate-500 mt-1 leading-relaxed">奖励 3 粒原切冻干生骨肉，配合温水复水诱导饮水，进行握爪互动建立信任。</p>
                </div>
              </div>

              <!-- Item 3 -->
              <div class="p-2.5 rounded-2xl bg-slate-50 border border-slate-200/80 hover:border-indigo-500 hover:bg-white transition-all flex items-start gap-3 cursor-pointer" onclick="event.stopPropagation(); inspectItem(3)">
                <div class="w-10 h-10 rounded-xl bg-white border border-slate-200 p-1 flex items-center justify-center shrink-0 shadow-2xs">
                  <img src="./assets/app_assets/ic_board_fountain.png" class="w-full h-full object-contain" alt="饮水机">
                </div>
                <div class="flex-1 min-w-0">
                  <div class="flex items-center justify-between">
                    <span class="text-xs font-black text-slate-900">10:30 (周六) · 猫洗澡人洗头协同安排</span>
                    <div class="flex items-center gap-1.5">
                      <img src="./assets/app_assets/avatars/avatar_linyi.png" class="w-4 h-4 rounded-full object-cover" alt="林亦">
                      <span class="text-[10px] font-bold text-slate-600">林亦</span>
                    </div>
                  </div>
                  <p class="text-[10.5px] text-slate-500 mt-1 leading-relaxed">去年过年洗过澡，老马钻完机箱全员弹提醒！YOYO 高德协同排班：老马洗澡 150、我剪头 30，下午三点前焕然一新回办公室。</p>
                </div>
              </div>

              <!-- Item 4 -->
              <div class="p-2.5 rounded-2xl bg-slate-50 border border-slate-200/80 hover:border-indigo-500 hover:bg-white transition-all flex items-start gap-3 cursor-pointer" onclick="event.stopPropagation(); inspectItem(4)">
                <div class="w-10 h-10 rounded-xl bg-white border border-slate-200 p-1 flex items-center justify-center shrink-0 shadow-2xs">
                  <img src="./assets/app_assets/ic_board_crate.png" class="w-full h-full object-contain" alt="航空箱">
                </div>
                <div class="flex-1 min-w-0">
                  <div class="flex items-center justify-between">
                    <span class="text-xs font-black text-slate-900">15:46 · 周末寄养出行交接</span>
                    <div class="flex items-center gap-1.5">
                      <img src="./assets/app_assets/avatars/avatar_muzi.png" class="w-4 h-4 rounded-full object-cover" alt="木子">
                      <span class="text-[10px] font-bold text-slate-600">木子</span>
                    </div>
                  </div>
                  <p class="text-[10.5px] text-slate-500 mt-1 leading-relaxed">核对寄养随行物品：益生菌、常备处方罐头与专属抓板，确认航空箱锁扣紧固出行。</p>
                </div>
              </div>

              <!-- Item 5 -->
              <div class="p-2.5 rounded-2xl bg-slate-50 border border-slate-200/80 hover:border-indigo-500 hover:bg-white transition-all flex items-start gap-3 cursor-pointer" onclick="event.stopPropagation(); inspectItem(5)">
                <div class="w-10 h-10 rounded-xl bg-white border border-slate-200 p-1 flex items-center justify-center shrink-0 shadow-2xs">
                  <img src="./assets/app_assets/ic_board_wand.png" class="w-full h-full object-contain" alt="逗猫棒">
                </div>
                <div class="flex-1 min-w-0">
                  <div class="flex items-center justify-between">
                    <span class="text-xs font-black text-slate-900">15:20 (周日) · 非工作日路过楼下精准陪伴</span>
                    <div class="flex items-center gap-1.5">
                      <img src="./assets/app_assets/avatars/avatar_muzi.png" class="w-4 h-4 rounded-full object-cover" alt="木子">
                      <span class="text-[10px] font-bold text-slate-600">木子</span>
                    </div>
                  </div>
                  <p class="text-[10.5px] text-slate-500 mt-1 leading-relaxed">YOYO 空间感知触发：非工作日经过公司楼下，收到“老马可能无聊了”提醒，APP 里老马敲屏幕急需上楼拿逗猫棒贴贴！</p>
                </div>
              </div>

              <!-- Item 6 -->
              <div class="p-2.5 rounded-2xl bg-slate-50 border border-slate-200/80 hover:border-indigo-500 hover:bg-white transition-all flex items-start gap-3 cursor-pointer" onclick="event.stopPropagation(); inspectItem(6)">
                <div class="w-10 h-10 rounded-xl bg-white border border-slate-200 p-1 flex items-center justify-center shrink-0 shadow-2xs">
                  <img src="./assets/app_assets/ic_board_feishu_badge.png" class="w-full h-full object-contain" alt="飞书工牌">
                </div>
                <div class="flex-1 min-w-0">
                  <div class="flex items-center justify-between">
                    <span class="text-xs font-black text-slate-900">18:30 · 晚间照料自动交接</span>
                    <div class="flex items-center gap-1.5">
                      <span class="text-[10px] font-mono font-bold text-blue-600 bg-blue-50 px-1.5 rounded">荣耀 YOYO</span>
                    </div>
                  </div>
                  <p class="text-[10.5px] text-slate-500 mt-1 leading-relaxed">YOYO 任务准时触发：汇总今日已完成 6 项与待完成 3 项，自动推送交接提醒至飞书老马群。</p>
                </div>
              </div>

              <!-- Item 7 -->
              <div class="p-2.5 rounded-2xl bg-slate-50 border border-slate-200/80 hover:border-indigo-500 hover:bg-white transition-all flex items-start gap-3 cursor-pointer" onclick="event.stopPropagation(); inspectItem(7)">
                <div class="w-10 h-10 rounded-xl bg-white border border-slate-200 p-1 flex items-center justify-center shrink-0 shadow-2xs">
                  <img src="./assets/app_assets/ic_board_cat_tree.png" class="w-full h-full object-contain" alt="猫爬架">
                </div>
                <div class="flex-1 min-w-0">
                  <div class="flex items-center justify-between">
                    <span class="text-xs font-black text-slate-900">18:52 · 三层实木猫爬架巡检</span>
                    <div class="flex items-center gap-1.5">
                      <img src="./assets/app_assets/avatars/avatar_imyrs.png" class="w-4 h-4 rounded-full object-cover" alt="ImYrS">
                      <span class="text-[10px] font-bold text-slate-600">ImYrS</span>
                    </div>
                  </div>
                  <p class="text-[10.5px] text-slate-500 mt-1 leading-relaxed">清理剑麻柱脱落麻屑，擦拭顶层观察台，确认立柱结构稳固无摇晃松动。</p>
                </div>
              </div>

              <!-- Item 8 -->
              <div class="p-2.5 rounded-2xl bg-slate-50 border border-slate-200/80 hover:border-indigo-500 hover:bg-white transition-all flex items-start gap-3 cursor-pointer" onclick="event.stopPropagation(); inspectItem(8)">
                <div class="w-10 h-10 rounded-xl bg-white border border-slate-200 p-1 flex items-center justify-center shrink-0 shadow-2xs">
                  <img src="./assets/app_assets/ic_board_litter_box.png" class="w-full h-full object-contain" alt="猫砂盆">
                </div>
                <div class="flex-1 min-w-0">
                  <div class="flex items-center justify-between">
                    <span class="text-xs font-black text-slate-900">20:26 · 膨润土猫砂深度清理</span>
                    <div class="flex items-center gap-1.5">
                      <img src="./assets/app_assets/avatars/avatar_adam.png" class="w-4 h-4 rounded-full object-cover" alt="Adam">
                      <span class="text-[10px] font-bold text-slate-600">Adam</span>
                    </div>
                  </div>
                  <p class="text-[10.5px] text-slate-500 mt-1 leading-relaxed">铲除今日结团，补充新鲜无尘矿砂至 8cm 刻度线，开启除臭杀菌喷雾循环。</p>
                </div>
              </div>

              <!-- Item 9 -->
              <div class="p-2.5 rounded-2xl bg-slate-50 border border-slate-200/80 hover:border-indigo-500 hover:bg-white transition-all flex items-start gap-3 cursor-pointer" onclick="event.stopPropagation(); inspectItem(9)">
                <div class="w-10 h-10 rounded-xl bg-white border border-slate-200 p-1 flex items-center justify-center shrink-0 shadow-2xs">
                  <img src="./assets/app_assets/ic_board_bowl.png" class="w-full h-full object-contain" alt="猫粮碗">
                </div>
                <div class="flex-1 min-w-0">
                  <div class="flex items-center justify-between">
                    <span class="text-xs font-black text-slate-900">21:44 · 渴望全价鲜肉猫粮投喂</span>
                    <div class="flex items-center gap-1.5">
                      <img src="./assets/app_assets/avatars/avatar_xiaoliu.png" class="w-4 h-4 rounded-full object-cover" alt="小六">
                      <span class="text-[10px] font-bold text-slate-600">小六</span>
                    </div>
                  </div>
                  <p class="text-[10.5px] text-slate-500 mt-1 leading-relaxed">清洗陶瓷浅食碗，称量定额干粮投放，记录当日总进食量无异常并记录留档。</p>
                </div>
              </div>

              <!-- Item 10 -->
              <div class="p-2.5 rounded-2xl bg-slate-50 border border-slate-200/80 hover:border-indigo-500 hover:bg-white transition-all flex items-start gap-3 cursor-pointer" onclick="event.stopPropagation(); inspectItem(10)">
                <div class="w-10 h-10 rounded-xl bg-white border border-slate-200 p-1 flex items-center justify-center shrink-0 shadow-2xs">
                  <img src="./assets/app_assets/ic_board_cat_bed.png" class="w-full h-full object-contain" alt="猫窝">
                </div>
                <div class="flex-1 min-w-0">
                  <div class="flex items-center justify-between">
                    <span class="text-xs font-black text-slate-900">23:18 · 静音恒温猫窝安睡准备</span>
                    <div class="flex items-center gap-1.5">
                      <img src="./assets/app_assets/avatars/avatar_fangsheng.png" class="w-4 h-4 rounded-full object-cover" alt="farest">
                      <span class="text-[10px] font-bold text-slate-600">farest</span>
                    </div>
                  </div>
                  <p class="text-[10.5px] text-slate-500 mt-1 leading-relaxed">巡视门窗关闭，将走廊夜灯调至暖光睡眠模式，确认老马回到休息垫安静入睡。</p>
                </div>
              </div>

            </div>
          </div>

          <!-- ------------------------------------------------------------- -->
          <!-- ASSEMBLY 04 (右侧) · 双梯形 Bento 交互机能矩阵 (Bento Action Hub) -->
          <!-- ------------------------------------------------------------- -->
          <div id="module-bento" class="exploded-module absolute z-20 bg-white/95 backdrop-blur-md p-5 rounded-3xl border border-amber-200/80 shadow-xl glow-amber" style="left: 1910px; top: 680px; width: 540px;" onclick="inspectComponent('bento')">
            <!-- Header -->
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

            <!-- Bento Trapezoid Visual Deconstruction -->
            <div class="grid grid-cols-2 gap-4 mb-4">
              <!-- Left Trapezoid Deconstruction: Leaderboard -->
              <div class="p-3.5 rounded-2xl bg-slate-50 border border-slate-200 flex flex-col justify-between">
                <div class="flex items-center gap-2 mb-2">
                  <img src="./assets/app_assets/ui_icons/ic_btn_trophy.png" class="w-6 h-6 object-contain" alt="奖杯">
                  <div>
                    <div class="text-xs font-black text-slate-800">左梯形 · 爱喵排行榜</div>
                    <div class="text-[9px] text-slate-400 font-mono">顶窄 124px / 底宽 160px</div>
                  </div>
                </div>

                <!-- 3D Podium & Top 3 Avatars Preview -->
                <div class="relative w-full h-24 my-2 flex items-end justify-center">
                  <div class="absolute inset-0 flex items-center justify-around z-20">
                    <!-- 2: 晓白 -->
                    <div class="flex flex-col items-center">
                      <img src="./assets/app_assets/avatars/avatar_xiaobai.png" class="w-6 h-6 rounded-full ring-2 ring-slate-200" alt="晓白">
                      <span class="text-[9px] font-bold text-slate-600 mt-0.5">晓白 🥈</span>
                    </div>
                    <!-- 1: Lex -->
                    <div class="flex flex-col items-center -translate-y-2">
                      <img src="./assets/app_assets/avatars/avatar_lex.png" class="w-8 h-8 rounded-full ring-2 ring-amber-400" alt="Lex">
                      <span class="text-[10px] font-black text-slate-800 mt-0.5">Lex 👑</span>
                    </div>
                    <!-- 3: 林亦 -->
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

              <!-- Right Trapezoid Deconstruction: Archives -->
              <div class="p-3.5 rounded-2xl bg-slate-50 border border-slate-200 flex flex-col justify-between">
                <div class="flex items-center gap-2 mb-2">
                  <img src="./assets/app_assets/ic_tile_journal.png" class="w-6 h-6 object-contain" alt="档案">
                  <div>
                    <div class="text-xs font-black text-slate-800">右梯形 · 老马档案馆</div>
                    <div class="text-[9px] text-slate-400 font-mono">顶宽 160px / 底窄 124px</div>
                  </div>
                </div>

                <!-- Gallery Silhouette Preview -->
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

            <!-- Geometric Seam Details -->
            <div class="p-2.5 rounded-xl bg-slate-50 border border-slate-200 text-[10px] font-mono text-slate-600 flex items-center justify-between">
              <span>缝隙间距: 14px (对称贴合)</span>
              <span>圆角半径: R18.0px</span>
              <span>矢量高光: 1.5px 纯白</span>
            </div>
          </div>

          <!-- ------------------------------------------------------------- -->
          <!-- ASSEMBLY 05 (底部) · 真实产研 14 人全员映射总成 (Personnel Matrix) -->
          <!-- ------------------------------------------------------------- -->
          <div id="module-team" class="exploded-module absolute z-20 bg-white/95 backdrop-blur-md p-6 rounded-3xl border border-slate-300 shadow-xl" style="left: 780px; top: 1600px; width: 1640px;" onclick="inspectComponent('team')">
            <!-- Header -->
            <div class="flex items-center justify-between border-b border-slate-100 pb-3 mb-4">
              <div class="flex items-center gap-2.5">
                <span class="w-8 h-8 rounded-xl bg-blue-50 border border-blue-200 flex items-center justify-center text-base">👥</span>
                <div>
                  <h3 class="font-black text-slate-900 text-sm">真实产研 14 人全员映射与技术职能矩阵</h3>
                  <span class="text-[10px] font-mono text-blue-600 font-bold">[ASM-05 · 14 REAL TEAM MEMBERS PERSONNEL MAPPING & ROLES]</span>
                </div>
              </div>
              <div class="flex items-center gap-2">
                <span class="text-[10px] text-slate-400 font-mono">规范源: docs/specs/01_PERSONNEL_MAPPING.md</span>
                <span class="text-[10px] px-2.5 py-0.5 rounded-full bg-emerald-50 text-emerald-700 font-mono font-bold">14/14 真实无虚构</span>
              </div>
            </div>

            <!-- 14 Team Members Grid -->
            <div class="grid grid-cols-7 gap-3">
              
              <!-- 1: 柯子杰 (阿杰) -->
              <div class="p-3 rounded-2xl bg-slate-50 border border-slate-200 hover:border-blue-500 hover:bg-white transition-all flex flex-col items-center text-center cursor-pointer" onclick="event.stopPropagation(); inspectMember('ajie')">
                <img src="./assets/app_assets/avatars/avatar_ajie.png" class="w-12 h-12 rounded-full object-cover shadow-xs ring-2 ring-slate-200 mb-2" alt="阿杰">
                <span class="text-xs font-black text-slate-900">阿杰 <span class="text-[10px] font-normal text-slate-400">(柯子杰)</span></span>
                <span class="text-[10px] font-bold text-blue-600 mt-0.5">视觉设计总监</span>
                <span class="text-[9px] text-slate-400 mt-1">UI体系与艺术手绘</span>
              </div>

              <!-- 2: 琮宇 (Howwoy) -->
              <div class="p-3 rounded-2xl bg-slate-50 border border-slate-200 hover:border-blue-500 hover:bg-white transition-all flex flex-col items-center text-center cursor-pointer" onclick="event.stopPropagation(); inspectMember('congyu')">
                <img src="./assets/app_assets/avatars/avatar_congyu.png" class="w-12 h-12 rounded-full object-cover shadow-xs ring-2 ring-slate-200 mb-2" alt="Howwoy">
                <span class="text-xs font-black text-slate-900">Howwoy <span class="text-[10px] font-normal text-slate-400">(琮宇)</span></span>
                <span class="text-[10px] font-bold text-blue-600 mt-0.5">客户端与原生交互</span>
                <span class="text-[9px] text-slate-400 mt-1">手势引擎与物理回弹</span>
              </div>

              <!-- 3: 方晟 (farest) -->
              <div class="p-3 rounded-2xl bg-slate-50 border border-slate-200 hover:border-blue-500 hover:bg-white transition-all flex flex-col items-center text-center cursor-pointer" onclick="event.stopPropagation(); inspectMember('fangsheng')">
                <img src="./assets/app_assets/avatars/avatar_fangsheng.png" class="w-12 h-12 rounded-full object-cover shadow-xs ring-2 ring-slate-200 mb-2" alt="farest">
                <span class="text-xs font-black text-slate-900">farest <span class="text-[10px] font-normal text-slate-400">(方晟)</span></span>
                <span class="text-[10px] font-bold text-blue-600 mt-0.5">智能体系统架构</span>
                <span class="text-[9px] text-slate-400 mt-1">状态机与事件调度</span>
              </div>

              <!-- 4: 传鹏 (阿鹏) -->
              <div class="p-3 rounded-2xl bg-slate-50 border border-slate-200 hover:border-blue-500 hover:bg-white transition-all flex flex-col items-center text-center cursor-pointer" onclick="event.stopPropagation(); inspectMember('apeng')">
                <div class="w-12 h-12 rounded-full bg-slate-200 flex items-center justify-center font-bold text-slate-500 ring-2 ring-slate-200 mb-2">鹏</div>
                <span class="text-xs font-black text-slate-900">阿鹏 <span class="text-[10px] font-normal text-slate-400">(传鹏)</span></span>
                <span class="text-[10px] font-bold text-blue-600 mt-0.5">硬件协同与测试</span>
                <span class="text-[9px] text-slate-400 mt-1">外设与端侧信号采集</span>
              </div>

              <!-- 5: 张桂滨 (Gbin) -->
              <div class="p-3 rounded-2xl bg-slate-50 border border-slate-200 hover:border-blue-500 hover:bg-white transition-all flex flex-col items-center text-center cursor-pointer" onclick="event.stopPropagation(); inspectMember('gbin')">
                <div class="w-12 h-12 rounded-full bg-slate-200 flex items-center justify-center font-bold text-slate-500 ring-2 ring-slate-200 mb-2">滨</div>
                <span class="text-xs font-black text-slate-900">Gbin <span class="text-[10px] font-normal text-slate-400">(张桂滨)</span></span>
                <span class="text-[10px] font-bold text-blue-600 mt-0.5">硬件与外设集成</span>
                <span class="text-[9px] text-slate-400 mt-1">蓝牙/传感器协同</span>
              </div>

              <!-- 6: 帅华 (小六) -->
              <div class="p-3 rounded-2xl bg-slate-50 border border-slate-200 hover:border-blue-500 hover:bg-white transition-all flex flex-col items-center text-center cursor-pointer" onclick="event.stopPropagation(); inspectMember('xiaoliu')">
                <img src="./assets/app_assets/avatars/avatar_xiaoliu.png" class="w-12 h-12 rounded-full object-cover shadow-xs ring-2 ring-slate-200 mb-2" alt="小六">
                <span class="text-xs font-black text-slate-900">小六 <span class="text-[10px] font-normal text-slate-400">(帅华)</span></span>
                <span class="text-[10px] font-bold text-blue-600 mt-0.5">3D / 动效 / 渲染</span>
                <span class="text-[9px] text-slate-400 mt-1">3D奖杯与物理动效</span>
              </div>

              <!-- 7: 天鸣 (木子) -->
              <div class="p-3 rounded-2xl bg-slate-50 border border-slate-200 hover:border-blue-500 hover:bg-white transition-all flex flex-col items-center text-center cursor-pointer" onclick="event.stopPropagation(); inspectMember('muzi')">
                <img src="./assets/app_assets/avatars/avatar_muzi.png" class="w-12 h-12 rounded-full object-cover shadow-xs ring-2 ring-slate-200 mb-2" alt="木子">
                <span class="text-xs font-black text-slate-900">木子 <span class="text-[10px] font-normal text-slate-400">(天鸣)</span></span>
                <span class="text-[10px] font-bold text-blue-600 mt-0.5">产品负责人</span>
                <span class="text-[9px] text-slate-400 mt-1">照护日程与用户旅程</span>
              </div>

              <!-- 8: 王斌 (Bingo) -->
              <div class="p-3 rounded-2xl bg-slate-50 border border-slate-200 hover:border-blue-500 hover:bg-white transition-all flex flex-col items-center text-center cursor-pointer" onclick="event.stopPropagation(); inspectMember('bingo')">
                <img src="./assets/app_assets/avatars/avatar_bingo.png" class="w-12 h-12 rounded-full object-cover shadow-xs ring-2 ring-slate-200 mb-2" alt="Bingo">
                <span class="text-xs font-black text-slate-900">Bingo <span class="text-[10px] font-normal text-slate-400">(王斌)</span></span>
                <span class="text-[10px] font-bold text-blue-600 mt-0.5">核心架构 / AI工程</span>
                <span class="text-[9px] text-slate-400 mt-1">端侧模型/YOYO对接</span>
              </div>

              <!-- 9: 家源 (ImYrS) -->
              <div class="p-3 rounded-2xl bg-slate-50 border border-slate-200 hover:border-blue-500 hover:bg-white transition-all flex flex-col items-center text-center cursor-pointer" onclick="event.stopPropagation(); inspectMember('imyrs')">
                <img src="./assets/app_assets/avatars/avatar_imyrs.png" class="w-12 h-12 rounded-full object-cover shadow-xs ring-2 ring-slate-200 mb-2" alt="ImYrS">
                <span class="text-xs font-black text-slate-900">ImYrS <span class="text-[10px] font-normal text-slate-400">(家源)</span></span>
                <span class="text-[10px] font-bold text-blue-600 mt-0.5">安全 / 测试保障</span>
                <span class="text-[9px] text-slate-400 mt-1">真机自动化与异常排查</span>
              </div>

              <!-- 10: 刘旭 (Lex) -->
              <div class="p-3 rounded-2xl bg-slate-50 border border-slate-200 hover:border-blue-500 hover:bg-white transition-all flex flex-col items-center text-center cursor-pointer" onclick="event.stopPropagation(); inspectMember('lex')">
                <img src="./assets/app_assets/avatars/avatar_lex.png" class="w-12 h-12 rounded-full object-cover shadow-xs ring-2 ring-slate-200 mb-2" alt="Lex">
                <span class="text-xs font-black text-slate-900">Lex <span class="text-[10px] font-normal text-slate-400">(刘旭)</span></span>
                <span class="text-[10px] font-bold text-blue-600 mt-0.5">后端 / 数据服务</span>
                <span class="text-[9px] text-slate-400 mt-1">排行榜加权与日志同步</span>
              </div>

              <!-- 11: 爱德 (Adam) -->
              <div class="p-3 rounded-2xl bg-slate-50 border border-slate-200 hover:border-blue-500 hover:bg-white transition-all flex flex-col items-center text-center cursor-pointer" onclick="event.stopPropagation(); inspectMember('adam')">
                <img src="./assets/app_assets/avatars/avatar_adam.png" class="w-12 h-12 rounded-full object-cover shadow-xs ring-2 ring-slate-200 mb-2" alt="Adam">
                <span class="text-xs font-black text-slate-900">Adam <span class="text-[10px] font-normal text-slate-400">(爱德)</span></span>
                <span class="text-[10px] font-bold text-blue-600 mt-0.5">交互设计</span>
                <span class="text-[9px] text-slate-400 mt-1">微动效与梯形裁切设计</span>
              </div>

              <!-- 12: 黑黑 -->
              <div class="p-3 rounded-2xl bg-slate-50 border border-slate-200 hover:border-blue-500 hover:bg-white transition-all flex flex-col items-center text-center cursor-pointer" onclick="event.stopPropagation(); inspectMember('heihei')">
                <img src="./assets/app_assets/avatars/avatar_heihei.png" class="w-12 h-12 rounded-full object-cover shadow-xs ring-2 ring-slate-200 mb-2" alt="黑黑">
                <span class="text-xs font-black text-slate-900">黑黑</span>
                <span class="text-[10px] font-bold text-blue-600 mt-0.5">运营 / 体验测试</span>
                <span class="text-[9px] text-slate-400 mt-1">老马生活真实照护数据</span>
              </div>

              <!-- 13: 嘉浩 (加号) -->
              <div class="p-3 rounded-2xl bg-slate-50 border border-slate-200 hover:border-blue-500 hover:bg-white transition-all flex flex-col items-center text-center cursor-pointer" onclick="event.stopPropagation(); inspectMember('jiahao')">
                <img src="./assets/app_assets/avatars/avatar_jiahao.png" class="w-12 h-12 rounded-full object-cover shadow-xs ring-2 ring-slate-200 mb-2" alt="加号">
                <span class="text-xs font-black text-slate-900">加号 <span class="text-[10px] font-normal text-slate-400">(嘉浩)</span></span>
                <span class="text-[10px] font-bold text-blue-600 mt-0.5">算法工程</span>
                <span class="text-[9px] text-slate-400 mt-1">行为预测与加餐推荐</span>
              </div>

              <!-- 14: 栾屹 (林亦) -->
              <div class="p-3 rounded-2xl bg-slate-50 border border-slate-200 hover:border-blue-500 hover:bg-white transition-all flex flex-col items-center text-center cursor-pointer" onclick="event.stopPropagation(); inspectMember('linyi')">
                <img src="./assets/app_assets/avatars/avatar_linyi.png" class="w-12 h-12 rounded-full object-cover shadow-xs ring-2 ring-blue-500 mb-2" alt="林亦">
                <span class="text-xs font-black text-slate-900">林亦 <span class="text-[10px] font-normal text-slate-400">(栾屹)</span></span>
                <span class="text-[10px] font-bold text-blue-600 mt-0.5">创始人 / 主理人</span>
                <span class="text-[9px] text-slate-400 mt-1">项目立项与总指挥</span>
              </div>

            </div>
          </div>

          <!-- ------------------------------------------------------------- -->
          <!-- ASSEMBLY 06 (右下) · 二级系统全览（手账卡片 163-169 全展开） -->
          <!-- ------------------------------------------------------------- -->
          <div id="module-archives" class="exploded-module absolute z-20 bg-white/95 backdrop-blur-md p-5 rounded-3xl border border-slate-200 shadow-xl" style="left: 2470px; top: 680px; width: 440px;" onclick="inspectComponent('archives')">
            <div class="flex items-center justify-between border-b border-slate-100 pb-3 mb-3">
              <div class="flex items-center gap-2">
                <span class="text-base">📖</span>
                <div>
                  <h3 class="font-black text-slate-900 text-sm">老马手账卡片全量物料 (7张完整展开)</h3>
                  <span class="text-[10px] font-mono text-slate-500 font-bold">[ARCHIVE CARDS 163-169]</span>
                </div>
              </div>
              <span class="text-[10px] px-2 py-0.5 rounded-full bg-slate-100 font-mono font-bold">7 CARDS</span>
            </div>

            <div class="space-y-2 max-h-[580px] overflow-y-auto pr-1">
              <img src="./assets/app_assets/archives/archive_163.png" class="w-full rounded-xl border border-slate-200 shadow-2xs hover:scale-[1.02] transition-transform cursor-pointer" alt="手账163">
              <img src="./assets/app_assets/archives/archive_164.png" class="w-full rounded-xl border border-slate-200 shadow-2xs hover:scale-[1.02] transition-transform cursor-pointer" alt="手账164">
              <img src="./assets/app_assets/archives/archive_165.png" class="w-full rounded-xl border border-slate-200 shadow-2xs hover:scale-[1.02] transition-transform cursor-pointer" alt="手账165">
              <img src="./assets/app_assets/archives/archive_166.png" class="w-full rounded-xl border border-slate-200 shadow-2xs hover:scale-[1.02] transition-transform cursor-pointer" alt="手账166">
              <img src="./assets/app_assets/archives/archive_167.png" class="w-full rounded-xl border border-slate-200 shadow-2xs hover:scale-[1.02] transition-transform cursor-pointer" alt="手账167">
              <img src="./assets/app_assets/archives/archive_168.png" class="w-full rounded-xl border border-slate-200 shadow-2xs hover:scale-[1.02] transition-transform cursor-pointer" alt="手账168">
              <img src="./assets/app_assets/archives/archive_169.png" class="w-full rounded-xl border border-slate-200 shadow-2xs hover:scale-[1.02] transition-transform cursor-pointer" alt="手账169">
            </div>
          </div>

        </div>
      </div>
    </div>

    <!-- ----------------------------------------------------------------------- -->
    <!-- TAB 2: 真机运行多态矩阵 (The 8 Real Device Screenshots & Live Comparison) -->
    <!-- ----------------------------------------------------------------------- -->
    <div id="view-screens" class="tab-view w-full h-full relative overflow-y-auto bg-slate-50 p-8 hidden">
      <div class="max-w-7xl mx-auto">
        <!-- Section Header -->
        <div class="mb-8 flex items-center justify-between">
          <div>
            <h2 class="text-2xl font-black text-slate-900 tracking-tight flex items-center gap-3">
              <span>📱 真机设备原生运行截图全矩阵</span>
              <span class="text-xs px-2.5 py-1 rounded-md bg-blue-100 text-blue-700 font-mono font-bold">8 NATIVE DEVICE SCREENSHOTS</span>
            </h2>
            <p class="text-sm text-slate-500 mt-1">从真实真机环境录制截取的 8 张高精度 (1320 × 2868) 原生画质界面，完整覆盖工况流转与二级页面</p>
          </div>
          <div class="flex items-center gap-2 text-xs font-mono text-slate-500 bg-white px-3 py-1.5 rounded-xl border border-slate-200 shadow-xs">
            <span>分辨率: 1320 × 2868</span>
            <span>|</span>
            <span>格式: 32-bit RGB</span>
          </div>
        </div>

        <!-- 8 Screenshots Responsive Grid -->
        <div class="grid grid-cols-4 gap-6">
          
          <!-- Screen 1 -->
          <div class="bg-white rounded-3xl p-4 border border-slate-200 shadow-sm flex flex-col">
            <div class="relative w-full rounded-2xl overflow-hidden bg-slate-100 mb-3 border border-slate-200 group">
              <img src="./assets/screenshots/Screenshot_20260919_174540_com_lyi_laomayoyo_MainActivity.JPG" class="w-full h-auto object-cover group-hover:scale-105 transition-transform duration-300" alt="截图1">
              <span class="absolute top-2 left-2 px-2 py-0.5 rounded-md bg-black/60 backdrop-blur-md text-[10px] text-white font-mono font-bold">01 · 首页主屏 (初始态)</span>
            </div>
            <div class="flex items-center justify-between text-xs font-black text-slate-800">
              <span>首页默认全景装配</span>
              <span class="text-[10px] font-mono text-slate-400">17:45:40</span>
            </div>
            <p class="text-[11px] text-slate-500 mt-1">健康活力工况下老马正坐状态，左侧时间轴已吸附 09:14 体检事件。</p>
          </div>

          <!-- Screen 2 -->
          <div class="bg-white rounded-3xl p-4 border border-slate-200 shadow-sm flex flex-col">
            <div class="relative w-full rounded-2xl overflow-hidden bg-slate-100 mb-3 border border-slate-200 group">
              <img src="./assets/screenshots/Screenshot_20260919_174600_com_lyi_laomayoyo_MainActivity.JPG" class="w-full h-auto object-cover group-hover:scale-105 transition-transform duration-300" alt="截图2">
              <span class="absolute top-2 left-2 px-2 py-0.5 rounded-md bg-black/60 backdrop-blur-md text-[10px] text-white font-mono font-bold">02 · 时间轴卡片展开</span>
            </div>
            <div class="flex items-center justify-between text-xs font-black text-slate-800">
              <span>全身梳毛卡片展开</span>
              <span class="text-[10px] font-mono text-slate-400">17:46:00</span>
            </div>
            <p class="text-[11px] text-slate-500 mt-1">向下滑动时间轴触发 09:15 黑黑负责梳毛卡片平滑展开，显示完整文案。</p>
          </div>

          <!-- Screen 3 -->
          <div class="bg-white rounded-3xl p-4 border border-slate-200 shadow-sm flex flex-col">
            <div class="relative w-full rounded-2xl overflow-hidden bg-slate-100 mb-3 border border-slate-200 group">
              <img src="./assets/screenshots/Screenshot_20260919_174613_com_lyi_laomayoyo_MainActivity.JPG" class="w-full h-auto object-cover group-hover:scale-105 transition-transform duration-300" alt="截图3">
              <span class="absolute top-2 left-2 px-2 py-0.5 rounded-md bg-rose-500/80 backdrop-blur-md text-[10px] text-white font-mono font-bold">03 · 抚摸微交互反馈</span>
            </div>
            <div class="flex items-center justify-between text-xs font-black text-slate-800">
              <span>抚摸呼噜波纹反馈</span>
              <span class="text-[10px] font-mono text-slate-400">17:46:13</span>
            </div>
            <p class="text-[11px] text-slate-500 mt-1">手指在屏幕中心轻抚老马额头，触发高潮呼噜微动效与爱心涟漪。</p>
          </div>

          <!-- Screen 4 -->
          <div class="bg-white rounded-3xl p-4 border border-slate-200 shadow-sm flex flex-col">
            <div class="relative w-full rounded-2xl overflow-hidden bg-slate-100 mb-3 border border-slate-200 group">
              <img src="./assets/screenshots/Screenshot_20260919_174628_com_lyi_laomayoyo_MainActivity.JPG" class="w-full h-auto object-cover group-hover:scale-105 transition-transform duration-300" alt="截图4">
              <span class="absolute top-2 left-2 px-2 py-0.5 rounded-md bg-black/60 backdrop-blur-md text-[10px] text-white font-mono font-bold">04 · 亲密度跃升状态</span>
            </div>
            <div class="flex items-center justify-between text-xs font-black text-slate-800">
              <span>互动后亲密度刷新</span>
              <span class="text-[10px] font-mono text-slate-400">17:46:28</span>
            </div>
            <p class="text-[11px] text-slate-500 mt-1">顶部爱猫指数由加权 86 分上升，老马眨动蓝眼恢复平静呼吸。</p>
          </div>

          <!-- Screen 5 -->
          <div class="bg-white rounded-3xl p-4 border border-slate-200 shadow-sm flex flex-col">
            <div class="relative w-full rounded-2xl overflow-hidden bg-slate-100 mb-3 border border-slate-200 group">
              <img src="./assets/screenshots/Screenshot_20260919_174648_com_lyi_laomayoyo_MainActivity.JPG" class="w-full h-auto object-cover group-hover:scale-105 transition-transform duration-300" alt="截图5">
              <span class="absolute top-2 left-2 px-2 py-0.5 rounded-md bg-amber-500/80 backdrop-blur-md text-[10px] text-white font-mono font-bold">05 · 饥饿脏污预警工况</span>
            </div>
            <div class="flex items-center justify-between text-xs font-black text-slate-800">
              <span>机箱钻灰脏污报警</span>
              <span class="text-[10px] font-mono text-slate-400">17:46:48</span>
            </div>
            <p class="text-[11px] text-slate-500 mt-1">老马毛发出现灰污斑点，胶囊变橙提示“该洗澡了”，自动推荐洗澡排班。</p>
          </div>

          <!-- Screen 6 -->
          <div class="bg-white rounded-3xl p-4 border border-slate-200 shadow-sm flex flex-col">
            <div class="relative w-full rounded-2xl overflow-hidden bg-slate-100 mb-3 border border-slate-200 group">
              <img src="./assets/screenshots/Screenshot_20260919_174700_com_lyi_laomayoyo_MainActivity.JPG" class="w-full h-auto object-cover group-hover:scale-105 transition-transform duration-300" alt="截图6">
              <span class="absolute top-2 left-2 px-2 py-0.5 rounded-md bg-blue-500/80 backdrop-blur-md text-[10px] text-white font-mono font-bold">06 · 爱喵排行榜全览</span>
            </div>
            <div class="flex items-center justify-between text-xs font-black text-slate-800">
              <span>爱喵排行榜二级页</span>
              <span class="text-[10px] font-mono text-slate-400">17:47:00</span>
            </div>
            <p class="text-[11px] text-slate-500 mt-1">点击左梯形平滑展开全员打赏榜，3D金银铜领奖台托举全公司爱喵先锋。</p>
          </div>

          <!-- Screen 7 -->
          <div class="bg-white rounded-3xl p-4 border border-slate-200 shadow-sm flex flex-col">
            <div class="relative w-full rounded-2xl overflow-hidden bg-slate-100 mb-3 border border-slate-200 group">
              <img src="./assets/screenshots/Screenshot_20260919_174713_com_lyi_laomayoyo_MainActivity.JPG" class="w-full h-auto object-cover group-hover:scale-105 transition-transform duration-300" alt="截图7">
              <span class="absolute top-2 left-2 px-2 py-0.5 rounded-md bg-indigo-500/80 backdrop-blur-md text-[10px] text-white font-mono font-bold">07 · 老马档案馆时间轴</span>
            </div>
            <div class="flex items-center justify-between text-xs font-black text-slate-800">
              <span>老马档案馆二级页</span>
              <span class="text-[10px] font-mono text-slate-400">17:47:13</span>
            </div>
            <p class="text-[11px] text-slate-500 mt-1">点击右梯形滑入手账时间流，记录老马入职至今的每一个感动瞬间。</p>
          </div>

          <!-- Screen 8 -->
          <div class="bg-white rounded-3xl p-4 border border-slate-200 shadow-sm flex flex-col">
            <div class="relative w-full rounded-2xl overflow-hidden bg-slate-100 mb-3 border border-slate-200 group">
              <img src="./assets/screenshots/Screenshot_20260919_174724_com_lyi_laomayoyo_MainActivity.JPG" class="w-full h-auto object-cover group-hover:scale-105 transition-transform duration-300" alt="截图8">
              <span class="absolute top-2 left-2 px-2 py-0.5 rounded-md bg-emerald-500/80 backdrop-blur-md text-[10px] text-white font-mono font-bold">08 · 手账详情与日志展开</span>
            </div>
            <div class="flex items-center justify-between text-xs font-black text-slate-800">
              <span>手账图文卡片详情</span>
              <span class="text-[10px] font-mono text-slate-400">17:47:24</span>
            </div>
            <p class="text-[11px] text-slate-500 mt-1">手账大图、打卡人头像、点赞互动与日记文本无裁切完整自适应呈现。</p>
          </div>

        </div>
      </div>
    </div>

    <!-- ----------------------------------------------------------------------- -->
    <!-- TAB 3: 全量零部件物料清单 (Bill of Materials - Asset Wall) -->
    <!-- ----------------------------------------------------------------------- -->
    <div id="view-bom" class="tab-view w-full h-full relative overflow-y-auto bg-slate-50 p-8 hidden">
      <div class="max-w-7xl mx-auto">
        <div class="mb-8">
          <h2 class="text-2xl font-black text-slate-900 tracking-tight flex items-center gap-3">
            <span>📦 全量零部件物料清单与数字资产全景墙 (BOM)</span>
            <span class="text-xs px-2.5 py-1 rounded-md bg-indigo-100 text-indigo-700 font-mono font-bold">ALL ASSETS DISCLOSURE</span>
          </h2>
          <p class="text-sm text-slate-500 mt-1">项目中所使用的全部 3D 图标、手绘道具、音视频、真实头像、手账卡片与字体文件，零遗漏陈列</p>
        </div>

        <!-- Category 1: 11 Board Items (手绘 3D 物品) -->
        <div class="mb-10">
          <h3 class="text-base font-black text-slate-800 mb-4 flex items-center gap-2">
            <span>🔹 24H 照护日程 11 大道具零部件</span>
            <span class="text-xs text-slate-400 font-mono font-normal">(/assets/app_assets/ic_board_*.png)</span>
          </h3>
          <div id="bom-board-items" class="grid grid-cols-6 gap-4">
            <!-- Rendered via JS -->
          </div>
        </div>

        <!-- Category 2: UI Icons & Action Buttons -->
        <div class="mb-10">
          <h3 class="text-base font-black text-slate-800 mb-4 flex items-center gap-2">
            <span>🔹 交互控件、指标微动效与功能磁贴</span>
            <span class="text-xs text-slate-400 font-mono font-normal">(/assets/app_assets/ui_icons/ & ic_tile_*.png)</span>
          </h3>
          <div id="bom-ui-icons" class="grid grid-cols-6 gap-4">
            <!-- Rendered via JS -->
          </div>
        </div>

        <!-- Category 3: 7 Archive Cards -->
        <div class="mb-10">
          <h3 class="text-base font-black text-slate-800 mb-4 flex items-center gap-2">
            <span>🔹 老马手账卡片 163-169 完整物料</span>
            <span class="text-xs text-slate-400 font-mono font-normal">(/assets/app_assets/archives/archive_*.png)</span>
          </h3>
          <div id="bom-archives" class="grid grid-cols-4 gap-4">
            <!-- Rendered via JS -->
          </div>
        </div>
      </div>
    </div>

    <!-- ----------------------------------------------------------------------- -->
    <!-- TAB 4: 真实研创 14 人全员图谱 (Team Personnel Matrix) -->
    <!-- ----------------------------------------------------------------------- -->
    <div id="view-team" class="tab-view w-full h-full relative overflow-y-auto bg-slate-50 p-8 hidden">
      <div class="max-w-7xl mx-auto">
        <div class="mb-8">
          <h2 class="text-2xl font-black text-slate-900 tracking-tight flex items-center gap-3">
            <span>👥 14 人真实研创团队技术职能与工程贡献全图谱</span>
            <span class="text-xs px-2.5 py-1 rounded-md bg-blue-100 text-blue-700 font-mono font-bold">14 CORE CONTRIBUTORS</span>
          </h2>
          <p class="text-sm text-slate-500 mt-1">严格溯源自《老马搭子》与项目权威规范，严禁任何 AI 自制虚拟名称与自画头像，全员真实名册与系统称谓完整映射</p>
        </div>

        <div id="team-full-grid" class="grid grid-cols-3 gap-6">
          <!-- Rendered via JS -->
        </div>
      </div>
    </div>

    <!-- ----------------------------------------------------------------------- -->
    <!-- TAB 5: 选题背景与系统架构 (Milestones & Architecture) -->
    <!-- ----------------------------------------------------------------------- -->
    <div id="view-milestones" class="tab-view w-full h-full relative overflow-y-auto bg-slate-50 p-8 hidden">
      <div class="max-w-5xl mx-auto space-y-10">
        <div>
          <h2 class="text-2xl font-black text-slate-900 tracking-tight flex items-center gap-3">
            <span>📜 荣耀 YOYO 智能体 · 选题历程与端侧架构全览</span>
            <span class="text-xs px-2.5 py-1 rounded-md bg-emerald-100 text-emerald-700 font-mono font-bold">PROJECT EVOLUTION</span>
          </h2>
          <p class="text-sm text-slate-500 mt-1">向甲方与评审委员会深度展示老马喵务局从立项、失败探索到端侧大模型协同成功的完整历程</p>
        </div>

        <!-- 3 Milestone Cards -->
        <div class="grid grid-cols-3 gap-6">
          <div class="bg-white p-6 rounded-3xl border border-slate-200 shadow-sm flex flex-col">
            <span class="text-xs font-mono font-black text-blue-600 mb-2">PHASE 01 · 选题立项</span>
            <h3 class="text-base font-black text-slate-800 mb-2">办公室智慧伴侣与团宠</h3>
            <p class="text-xs text-slate-500 leading-relaxed">
              将真实存在的公司蓝眼布偶猫“老马”数字化，结合荣耀 MagicOS 端侧空间感知能力，打造首个集生命体感知、照护协作、空间陪伴于一体的软硬件原生智能体。
            </p>
          </div>

          <div class="bg-white p-6 rounded-3xl border border-slate-200 shadow-sm flex flex-col border-l-4 border-l-amber-500">
            <span class="text-xs font-mono font-black text-amber-600 mb-2">PHASE 02 · 架构反思与沉淀</span>
            <h3 class="text-base font-black text-slate-800 mb-2">摒弃重构盲动 · 拥抱真实沉淀</h3>
            <p class="text-xs text-slate-500 leading-relaxed">
              项目经历了 Native 重构等技术弯路，最终全团队统一战线：以沉淀数万行真机测试经验的混合容器架构为基石，彻底解决手势卡顿与状态断连。
            </p>
          </div>

          <div class="bg-white p-6 rounded-3xl border border-slate-200 shadow-sm flex flex-col border-l-4 border-l-emerald-500">
            <span class="text-xs font-mono font-black text-emerald-600 mb-2">PHASE 03 · 智能体与端云协同</span>
            <h3 class="text-base font-black text-slate-800 mb-2">YOYO + 飞书 + 高德全链路闭环</h3>
            <p class="text-xs text-slate-500 leading-relaxed">
              当老马出现脏污或非工作日经过楼下，YOYO 空间智能体主动感知，联动高德地图计算洗猫剪发排班，并通过飞书机器人自动完成晚间交接。
            </p>
          </div>
        </div>

        <!-- Technical Architecture Diagram (SVG) -->
        <div class="bg-white p-8 rounded-3xl border border-slate-200 shadow-sm">
          <h3 class="text-base font-black text-slate-800 mb-6 flex items-center gap-2">
            <span>⚙️ 核心状态机 (FSM) 与端侧双向感知通信拓扑</span>
            <span class="text-xs font-mono text-slate-400">FINITE STATE MACHINE & HARDWARE BRIDGE</span>
          </h3>

          <div class="p-6 rounded-2xl bg-slate-50 border border-slate-200 font-mono text-xs text-slate-700 leading-loose">
            <div class="grid grid-cols-3 gap-6 text-center">
              <div class="p-4 rounded-xl bg-emerald-50 border border-emerald-200">
                <div class="font-black text-emerald-800">STATE: NORMAL (活力健康态)</div>
                <div class="text-[11px] text-emerald-600 mt-1">视频: home_cat_clean.mp4 (1.15x)</div>
                <div class="text-[10px] text-slate-500 mt-1">指标: 快乐 98 / 亲密 86</div>
              </div>
              <div class="p-4 rounded-xl bg-amber-50 border border-amber-200">
                <div class="font-black text-amber-800">STATE: DIRTY (饥饿脏污态)</div>
                <div class="text-[11px] text-amber-600 mt-1">视频: home_cat_dirty.mp4 (1.0x)</div>
                <div class="text-[10px] text-slate-500 mt-1">触发: 尘屑传感器 / 8h未进食</div>
              </div>
              <div class="p-4 rounded-xl bg-rose-50 border border-rose-200">
                <div class="font-black text-rose-800">STATE: TOUCH (抚摸互动态)</div>
                <div class="text-[11px] text-rose-600 mt-1">视频: home_cat_touch.mp4 (1.0x)</div>
                <div class="text-[10px] text-slate-500 mt-1">交互: 屏幕轻抚 / 呼噜音频触发</div>
              </div>
            </div>

            <div class="my-4 text-center text-slate-400 text-sm">⬇ 统一事件总线 (Event Stream Hub) ⬇</div>

            <div class="p-4 rounded-xl bg-white border border-slate-200 flex items-center justify-between text-[11px]">
              <span>[荣耀 MagicOS 空间感知引擎]</span>
              <span>↔</span>
              <span>[Web/Android Native Bridge 协议]</span>
              <span>↔</span>
              <span>[飞书自动同步机器人 / 高德日程]</span>
            </div>
          </div>
        </div>
      </div>
    </div>

  </main>

  <!-- ========================================================================= -->
  <!-- 侧边零部件工程检视抽屉 (Component Inspector Drawer) -->
  <!-- ========================================================================= -->
  <div id="inspector-drawer" class="fixed top-16 right-0 bottom-0 w-[420px] bg-white/95 backdrop-blur-xl border-l border-slate-200 shadow-2xl z-50 transform translate-x-full transition-transform duration-300 flex flex-col">
    <!-- Drawer Header -->
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

    <!-- Drawer Body -->
    <div class="flex-1 overflow-y-auto p-6 space-y-6">
      <!-- Big Preview Box -->
      <div class="w-full h-48 rounded-2xl bg-slate-50 border border-slate-200 p-4 flex items-center justify-center overflow-hidden">
        <img id="insp-img" src="./assets/app_assets/app_icon_preview.png" class="max-h-full max-w-full object-contain drop-shadow-md" alt="预览">
      </div>

      <!-- Specs Table -->
      <div class="space-y-3">
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
            <span class="text-slate-400">绑定研发人员:</span>
            <span class="font-bold text-slate-800" id="insp-author">黑黑 / 阿杰</span>
          </div>
        </div>
      </div>

      <!-- Detailed Description & Copy -->
      <div class="space-y-2">
        <h4 class="text-xs font-black text-slate-800 uppercase font-mono tracking-wider">官方正版文案与业务逻辑</h4>
        <p class="text-xs text-slate-600 leading-relaxed bg-slate-50 p-3.5 rounded-2xl border border-slate-200" id="insp-desc">
          使用软针气垫梳整理背部浮毛，检查颈部毛发光泽；YOYO 同步播报今日进食正常、眼神清澈，养猫指数稳步提升！
        </p>
      </div>
    </div>
  </div>

  <!-- ========================================================================= -->
  <!-- JavaScript 交互驱动引擎 (Interactivity Engine) -->
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
    // 2. Pan & Zoom Canvas Engine
    // -------------------------------------------------------------------------
    let panX = 0;
    let panY = 0;
    let zoomScale = 0.85;
    let isDraggingCanvas = false;
    let dragStartX = 0;
    let dragStartY = 0;
    let showLeaderLines = true;
    let explosionRate = 0.8; // 80% default

    const stageEl = document.getElementById('canvas-stage');
    const hudZoomEl = document.getElementById('hud-zoom');
    const hudXEl = document.getElementById('hud-x');
    const hudYEl = document.getElementById('hud-y');

    function applyCanvasTransform() {
      stageEl.style.transform = `translate(${panX}px, ${panY}px) scale(${zoomScale})`;
      hudZoomEl.textContent = `${Math.round(zoomScale * 100)}%`;
      hudXEl.textContent = Math.round(panX);
      hudYEl.textContent = Math.round(panY);
      if (showLeaderLines) {
        drawLeaderLines();
      }
    }

    function resetCanvasTransform() {
      panX = 0;
      panY = 0;
      zoomScale = 0.85;
      applyCanvasTransform();
    }

    function startPan(e) {
      if (e.target.closest('.exploded-module') || e.target.closest('#core-device-frame') || e.target.closest('button')) {
        return;
      }
      isDraggingCanvas = true;
      dragStartX = e.clientX - panX;
      dragStartY = e.clientY - panY;
      window.addEventListener('mousemove', onPanMove);
      window.addEventListener('mouseup', endPan);
    }

    function onPanMove(e) {
      if (!isDraggingCanvas) return;
      panX = e.clientX - dragStartX;
      panY = e.clientY - dragStartY;
      applyCanvasTransform();
    }

    function endPan() {
      isDraggingCanvas = false;
      window.removeEventListener('mousemove', onPanMove);
      window.removeEventListener('mouseup', endPan);
    }

    function handleWheelZoom(e) {
      e.preventDefault();
      const zoomFactor = e.deltaY > 0 ? 0.92 : 1.08;
      zoomScale = Math.min(Math.max(0.3, zoomScale * zoomFactor), 2.5);
      applyCanvasTransform();
    }

    // -------------------------------------------------------------------------
    // 3. Exploded Assembly Organic Positioning
    // -------------------------------------------------------------------------
    // Baseline organic offsets when explosion = 100%
    const BASE_OFFSETS = {
      gauges: { x: -450, y: -380 },    // Top-Left
      media: { x: 420, y: -380 },      // Top-Right
      timeline: { x: -580, y: 30 },     // Left-Center
      bento: { x: 450, y: 30 },        // Right-Center
      team: { x: -280, y: 780 },       // Bottom-Center
      archives: { x: 920, y: 30 }      // Far-Right
    };

    function updateExplosion(val) {
      explosionRate = val / 100;
      document.getElementById('explode-val').textContent = `${val}%`;

      // Central core stays at base (1405, 678)
      const coreX = 1405;
      const coreY = 678;

      // Interpolate each module towards or away from the core
      // module-gauges
      const gEl = document.getElementById('module-gauges');
      gEl.style.left = `${coreX + (BASE_OFFSETS.gauges.x * explosionRate)}px`;
      gEl.style.top = `${coreY + (BASE_OFFSETS.gauges.y * explosionRate)}px`;

      // module-media
      const mEl = document.getElementById('module-media');
      mEl.style.left = `${coreX + (BASE_OFFSETS.media.x * explosionRate)}px`;
      mEl.style.top = `${coreY + (BASE_OFFSETS.media.y * explosionRate)}px`;

      // module-timeline
      const tEl = document.getElementById('module-timeline');
      tEl.style.left = `${coreX + (BASE_OFFSETS.timeline.x * explosionRate)}px`;
      tEl.style.top = `${coreY + (BASE_OFFSETS.timeline.y * explosionRate)}px`;

      // module-bento
      const bEl = document.getElementById('module-bento');
      bEl.style.left = `${coreX + (BASE_OFFSETS.bento.x * explosionRate)}px`;
      bEl.style.top = `${coreY + (BASE_OFFSETS.bento.y * explosionRate)}px`;

      // module-team
      const tmEl = document.getElementById('module-team');
      tmEl.style.left = `${coreX + (BASE_OFFSETS.team.x * explosionRate)}px`;
      tmEl.style.top = `${coreY + (BASE_OFFSETS.team.y * explosionRate)}px`;

      // module-archives
      const arEl = document.getElementById('module-archives');
      arEl.style.left = `${coreX + (BASE_OFFSETS.archives.x * explosionRate)}px`;
      arEl.style.top = `${coreY + (BASE_OFFSETS.archives.y * explosionRate)}px`;

      drawLeaderLines();
    }

    // -------------------------------------------------------------------------
    // 4. SVG Dynamic Leader Lines (连接装配导线)
    // -------------------------------------------------------------------------
    function drawLeaderLines() {
      const svg = document.getElementById('svg-leader-lines');
      if (!showLeaderLines) {
        svg.innerHTML = '';
        return;
      }

      const coreEl = document.getElementById('core-device-frame');
      const coreRect = {
        x: parseFloat(coreEl.style.left),
        y: parseFloat(coreEl.style.top),
        w: 390,
        h: 844
      };

      const connections = [
        { id: 'module-gauges', color: '#06B6D4', fromAnchor: 'right', toAnchor: { x: coreRect.x + 80, y: coreRect.y + 40 } },
        { id: 'module-media', color: '#10B981', fromAnchor: 'left', toAnchor: { x: coreRect.x + 310, y: coreRect.y + 120 } },
        { id: 'module-timeline', color: '#6366F1', fromAnchor: 'right', toAnchor: { x: coreRect.x + 20, y: coreRect.y + 420 } },
        { id: 'module-bento', color: '#F59E0B', fromAnchor: 'left', toAnchor: { x: coreRect.x + 370, y: coreRect.y + 640 } },
        { id: 'module-team', color: '#3B82F6', fromAnchor: 'top', toAnchor: { x: coreRect.x + 195, y: coreRect.y + 830 } }
      ];

      let paths = '';
      connections.forEach(conn => {
        const el = document.getElementById(conn.id);
        if (!el) return;
        const elX = parseFloat(el.style.left);
        const elY = parseFloat(el.style.top);
        const elW = el.offsetWidth;
        const elH = el.offsetHeight;

        let startX, startY;
        if (conn.fromAnchor === 'right') {
          startX = elX + elW;
          startY = elY + elH / 2;
        } else if (conn.fromAnchor === 'left') {
          startX = elX;
          startY = elY + elH / 2;
        } else {
          startX = elX + elW / 2;
          startY = elY;
        }

        const endX = conn.toAnchor.x;
        const endY = conn.toAnchor.y;

        // Curved organic bezier
        const midX = (startX + endX) / 2;
        const midY = (startY + endY) / 2;
        const pathData = `M ${startX} ${startY} Q ${midX} ${startY} ${midX} ${midY} T ${endX} ${endY}`;

        paths += `
          <g>
            <circle cx="${startX}" cy="${startY}" r="4" fill="${conn.color}" />
            <path d="${pathData}" fill="none" stroke="${conn.color}" stroke-width="1.8" stroke-dasharray="5 4" opacity="0.85" />
            <circle cx="${endX}" cy="${endY}" r="4" fill="${conn.color}" />
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
        btn.className = 'px-2.5 py-1.5 rounded-xl bg-blue-50 text-blue-700 hover:bg-blue-100 text-xs font-bold transition-all border border-blue-200 active:scale-95 flex items-center gap-1';
      } else {
        btn.innerHTML = '<span>🔗</span> 导线关';
        btn.className = 'px-2.5 py-1.5 rounded-xl bg-slate-100 text-slate-500 hover:bg-slate-200 text-xs font-bold transition-all border border-slate-200 active:scale-95 flex items-center gap-1';
      }
      drawLeaderLines();
    }

    // -------------------------------------------------------------------------
    // 5. Global Cat State Machine Control
    // -------------------------------------------------------------------------
    let currentCatState = 'normal';

    const STATE_MAP = {
      normal: {
        video: './assets/app_assets/home_cat_clean.mp4',
        badgeColor: 'bg-emerald-100 text-emerald-800',
        dotColor: 'bg-emerald-500',
        text: '精神不错',
        care: '3/5',
        activeItem: 1
      },
      dirty: {
        video: './assets/app_assets/home_cat_dirty.mp4',
        badgeColor: 'bg-amber-100 text-amber-800',
        dotColor: 'bg-amber-500',
        text: '该洗澡了',
        care: '42分',
        activeItem: 3
      },
      touch: {
        video: './assets/app_assets/home_cat_touch.mp4',
        badgeColor: 'bg-rose-100 text-rose-800',
        dotColor: 'bg-rose-500',
        text: '已到楼下',
        care: '急需陪伴',
        activeItem: 5
      }
    };

    function setGlobalCatState(state) {
      currentCatState = state;
      const cfg = STATE_MAP[state];

      // Update phone video
      const vid = document.getElementById('phone-cat-video');
      vid.src = cfg.video;
      vid.play();

      // Update phone badge
      document.getElementById('phone-state-text').textContent = cfg.text;
      document.getElementById('phone-care-ratio').textContent = cfg.care;

      // Update top state buttons
      ['normal', 'dirty', 'touch'].forEach(st => {
        const btn = document.getElementById(`btn-state-${st}`);
        if (st === state) {
          btn.className = `state-pill px-3 py-1.5 rounded-xl text-xs font-black transition-all shadow-xs flex items-center gap-1.5 ${
            st === 'normal' ? 'bg-emerald-500 text-white' : st === 'dirty' ? 'bg-amber-500 text-white' : 'bg-rose-500 text-white'
          }`;
        } else {
          btn.className = 'state-pill px-3 py-1.5 rounded-xl text-xs font-black transition-all bg-slate-100 text-slate-600 hover:bg-slate-200 flex items-center gap-1.5';
        }
      });

      // Update docked item
      const item = SCHEDULE_DATA[cfg.activeItem];
      if (item) {
        document.getElementById('phone-active-icon').src = item.icon;
        document.getElementById('phone-active-title').textContent = item.title;
        document.getElementById('phone-active-time').textContent = item.time;
        document.getElementById('phone-active-desc').textContent = item.desc;
      }
    }

    // -------------------------------------------------------------------------
    // 6. Navigation Tabs Switcher
    // -------------------------------------------------------------------------
    function switchTab(tabId) {
      document.querySelectorAll('.tab-view').forEach(el => el.classList.add('hidden'));
      document.querySelectorAll('.tab-btn').forEach(btn => {
        btn.className = 'tab-btn px-4 py-1.5 rounded-lg text-xs font-bold text-slate-600 hover:text-slate-900 transition-all flex items-center gap-1.5';
      });

      const activeView = document.getElementById(`view-${tabId}`);
      if (activeView) activeView.classList.remove('hidden');

      const activeBtn = document.getElementById(`tab-btn-${tabId}`);
      if (activeBtn) {
        activeBtn.className = 'tab-btn px-4 py-1.5 rounded-lg text-xs font-bold text-blue-700 bg-white shadow-xs transition-all flex items-center gap-1.5';
      }

      // Hide explosion controls in other tabs
      const expCtrl = document.getElementById('explosion-controls');
      const linesBtn = document.getElementById('toggle-lines-btn');
      if (tabId === 'exploded') {
        expCtrl.style.display = 'flex';
        linesBtn.style.display = 'flex';
        applyCanvasTransform();
      } else {
        expCtrl.style.display = 'none';
        linesBtn.style.display = 'none';
      }
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
      } else if (type === 'team') {
        titleEl.textContent = '真实产研 14 人全员映射总成';
        tagEl.textContent = '[ASM-05 · 14 CONTRIBUTORS]';
        imgEl.src = './assets/app_assets/avatars/avatar_linyi.png';
        nameEl.textContent = '14 位真实产研团队全员名册';
        pathEl.textContent = '/assets/app_assets/avatars/avatar_*.png';
        typeEl.textContent = '真实正版免冠头像';
        authorEl.textContent = '栾屹 (林亦) 领衔 14 人产研全员';
        descEl.textContent = '零假名、零 AI 虚构生成！全员严格对应视觉、3D、原生、算法、安全与硬件分工，承载选拔赛真实交付。';
      }

      drawer.classList.remove('translate-x-full');
    }

    function inspectItem(idx) {
      const item = SCHEDULE_DATA[idx];
      if (!item) return;

      const drawer = document.getElementById('inspector-drawer');
      document.getElementById('insp-title').textContent = item.title;
      document.getElementById('insp-tag').textContent = `[ITEM-${idx} · ${item.time}]`;
      document.getElementById('insp-img').src = item.icon;
      document.getElementById('insp-name').textContent = item.title;
      document.getElementById('insp-path').textContent = item.icon;
      document.getElementById('insp-type').textContent = '24H 照护事件道具';
      document.getElementById('insp-author').textContent = `${item.person} (执行人)`;
      document.getElementById('insp-desc').textContent = item.desc;

      drawer.classList.remove('translate-x-full');
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

      drawer.classList.remove('translate-x-full');
    }

    function closeInspector() {
      document.getElementById('inspector-drawer').classList.add('translate-x-full');
    }

    // -------------------------------------------------------------------------
    // 8. Render BOM & Team Tabs
    // -------------------------------------------------------------------------
    function renderBOMTab() {
      // 11 Board items
      const boardContainer = document.getElementById('bom-board-items');
      let bHtml = '';
      SCHEDULE_DATA.forEach(it => {
        bHtml += `
          <div class="bg-white p-3.5 rounded-2xl border border-slate-200 shadow-2xs hover:border-blue-400 transition-all flex flex-col items-center text-center cursor-pointer" onclick="inspectItem(${it.id})">
            <img src="${it.icon}" class="w-14 h-14 object-contain mb-2 drop-shadow-xs" alt="${it.title}">
            <span class="text-xs font-black text-slate-800 truncate w-full">${it.title}</span>
            <span class="text-[10px] text-slate-400 font-mono mt-0.5">${it.time} · ${it.person}</span>
          </div>
        `;
      });
      boardContainer.innerHTML = bHtml;

      // UI Icons
      const uiIcons = [
        { name: 'ic_btn_trophy.png', title: '3D 荣誉金杯', path: './assets/app_assets/ui_icons/ic_btn_trophy.png' },
        { name: 'ic_tile_journal.png', title: '档案手册磁贴', path: './assets/app_assets/ic_tile_journal.png' },
        { name: 'ic_index_catlove.png', title: '爱猫加权徽标', path: './assets/app_assets/ui_icons/ic_index_catlove.png' },
        { name: 'ic_index_happiness.png', title: '快乐值仪表', path: './assets/app_assets/ui_icons/ic_index_happiness.png' },
        { name: 'ic_btn_like_active.png', title: '心动点赞状态', path: './assets/app_assets/ui_icons/ic_btn_like_active.png' },
        { name: 'podium_3d.png', title: '3D 领奖台模型', path: './assets/app_assets/generated/podium_3d.png' }
      ];
      const uiContainer = document.getElementById('bom-ui-icons');
      let uHtml = '';
      uiIcons.forEach(ui => {
        uHtml += `
          <div class="bg-white p-3.5 rounded-2xl border border-slate-200 shadow-2xs hover:border-blue-400 transition-all flex flex-col items-center text-center">
            <img src="${ui.path}" class="w-14 h-14 object-contain mb-2 drop-shadow-xs" alt="${ui.title}">
            <span class="text-xs font-black text-slate-800 truncate w-full">${ui.title}</span>
            <span class="text-[9px] text-slate-400 font-mono mt-0.5 truncate w-full">${ui.name}</span>
          </div>
        `;
      });
      uiContainer.innerHTML = uHtml;

      // Archives
      const archContainer = document.getElementById('bom-archives');
      let aHtml = '';
      [163, 164, 165, 166, 167, 168, 169].forEach(id => {
        aHtml += `
          <div class="bg-white p-3 rounded-2xl border border-slate-200 shadow-2xs hover:border-blue-400 transition-all">
            <img src="./assets/app_assets/archives/archive_${id}.png" class="w-full h-auto rounded-xl object-cover mb-2" alt="手账${id}">
            <div class="flex items-center justify-between text-xs font-bold text-slate-800">
              <span>手账日常 #${id}</span>
              <span class="text-[9px] font-mono text-slate-400">PNG</span>
            </div>
          </div>
        `;
      });
      archContainer.innerHTML = aHtml;
    }

    function renderTeamTab() {
      const container = document.getElementById('team-full-grid');
      let html = '';
      TEAM_MEMBERS.forEach(mem => {
        html += `
          <div class="bg-white p-5 rounded-3xl border border-slate-200 shadow-xs hover:border-blue-500 hover:shadow-md transition-all flex items-start gap-4 cursor-pointer" onclick="inspectMember('${mem.alias}')">
            <img src="${mem.avatar}" class="w-14 h-14 rounded-full object-cover shadow-xs ring-2 ring-slate-200 shrink-0" alt="${mem.alias}">
            <div class="flex-1 min-w-0">
              <div class="flex items-center justify-between">
                <h4 class="text-sm font-black text-slate-900">${mem.alias} <span class="text-xs font-normal text-slate-400">(${mem.name})</span></h4>
                <span class="text-[10px] font-mono font-bold text-blue-600 bg-blue-50 px-2 py-0.5 rounded-full">${mem.role}</span>
              </div>
              <p class="text-xs text-slate-500 mt-2 leading-relaxed">${mem.desc}</p>
            </div>
          </div>
        `;
      });
      container.innerHTML = html;
    }

    // -------------------------------------------------------------------------
    // 9. Initial Boot
    // -------------------------------------------------------------------------
    window.addEventListener('DOMContentLoaded', () => {
      updateExplosion(80);
      applyCanvasTransform();
      renderBOMTab();
      renderTeamTab();
    });

    // Window resize handler
    window.addEventListener('resize', () => {
      drawLeaderLines();
    });
  </script>
</body>
</html>
"""

with open('/Users/bingo/Code/LYi/projects/laoma-engine-showcase/index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("index.html created successfully!")
