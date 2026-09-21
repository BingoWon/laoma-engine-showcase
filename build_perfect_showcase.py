import os, glob

OUTPUT_FILE = "/Users/bingo/Code/LYi/projects/laoma-engine-showcase/index.html"

html_code = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>老马喵务局 · 端侧智能体系统架构与全量工程物料全景拆解总成</title>
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
      background-size: 24px 24px;
    }
    
    /* Hardware accelerated canvas stage */
    #canvas-stage {
      will-change: transform;
      transform-origin: 0 0;
    }

    /* Custom scrollbars */
    ::-webkit-scrollbar {
      width: 5px;
      height: 5px;
    }
    ::-webkit-scrollbar-track {
      background: #F1F5F9;
    }
    ::-webkit-scrollbar-thumb {
      background: #CBD5E1;
      border-radius: 3px;
    }

    /* Blueprint card styling */
    .blueprint-card {
      background: rgba(255, 255, 255, 0.96);
      backdrop-filter: blur(16px);
      border: 1px solid rgba(203, 213, 225, 0.9);
      box-shadow: 0 12px 32px -8px rgba(15, 23, 42, 0.07), 0 0 1px 1px rgba(255, 255, 255, 0.9) inset;
    }

    /* Draggable node hover and active styling */
    .draggable-node {
      touch-action: none;
      transition: box-shadow 0.2s ease, border-color 0.2s ease;
    }
    .draggable-node:hover {
      border-color: #93C5FD !important;
      box-shadow: 0 16px 40px -10px rgba(37, 99, 235, 0.12), 0 0 0 1px rgba(59, 130, 246, 0.25);
    }
    .node-drag-handle {
      cursor: grab;
    }
    .node-drag-handle:active {
      cursor: grabbing;
    }

    /* Exploded animation transition when slider moves */
    .exploded-sub-module {
      transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1);
      will-change: transform;
    }

    /* Strict aspect ratio wrappers ensuring ZERO cropping (object-contain) */
    .aspect-phone {
      aspect-ratio: 1320 / 2868; /* 0.4603 */
    }
    .aspect-phone-sample {
      aspect-ratio: 650 / 1414; /* 0.4597 */
    }
    .aspect-cine-16-9 {
      aspect-ratio: 16 / 9; /* 1.7778 */
    }
    .aspect-photo-3-4 {
      aspect-ratio: 3 / 4; /* 0.7500 */
    }
    .aspect-photo-4-3 {
      aspect-ratio: 4 / 3; /* 1.3333 */
    }
    .aspect-square-1-1 {
      aspect-ratio: 1 / 1; /* 1.0000 */
    }
    .aspect-wide-2-1 {
      aspect-ratio: 2 / 1;
    }
    .aspect-wide-2-5 {
      aspect-ratio: 2.509 / 1;
    }
    .aspect-wide-1-5 {
      aspect-ratio: 1.5 / 1;
    }
    .aspect-tex-1-2 {
      aspect-ratio: 1.2 / 1;
    }

    /* Strict Image rule: NEVER CROP - Always respect native aspect ratio */
    .no-crop-img {
      object-fit: contain;
      width: 100%;
      height: 100%;
    }

    /* Standardized engineering token box for avatars */
    .engineer-avatar-box {
      width: 48px;
      height: 48px;
      aspect-ratio: 1 / 1;
      border-radius: 14px;
      overflow: hidden;
      flex-shrink: 0;
      background-color: #F1F5F9;
    }

    /* Cleanroom optical pad for transparent PNG cutouts */
    .cleanroom-pad {
      background-image: linear-gradient(45deg, #f1f5f9 25%, transparent 25%), 
                        linear-gradient(-45deg, #f1f5f9 25%, transparent 25%), 
                        linear-gradient(45deg, transparent 75%, #f1f5f9 75%), 
                        linear-gradient(-45deg, transparent 75%, #f1f5f9 75%);
      background-size: 12px 12px;
      background-position: 0 0, 0 6px, 6px -6px, -6px 0px;
      background-color: #ffffff;
    }

    /* Leader line animated styling */
    .tech-leader-line {
      stroke: #2563EB;
      stroke-width: 1.5;
      stroke-dasharray: 4 4;
      animation: dashMove 20s linear infinite;
    }

    .tech-leader-joint {
      fill: #2563EB;
      stroke: #FFFFFF;
      stroke-width: 2;
    }

    @keyframes dashMove {
      to {
        stroke-dashoffset: -100;
      }
    }
  </style>
</head>
<body class="bg-blueprint-grid text-slate-800 font-sans antialiased overflow-hidden select-none w-screen h-screen">

  <!-- ========================================================================= -->
  <!-- TOP CONTROL TOOLBAR (Fixed HUD Dock)                                      -->
  <!-- ========================================================================= -->
  <header class="fixed top-0 left-0 right-0 h-14 z-50 bg-white/95 backdrop-blur-xl border-b border-slate-200/90 px-5 flex items-center justify-between shadow-xs">
    <!-- Left: Project Identity & Specs -->
    <div class="flex items-center gap-3">
      <div class="w-8 h-8 rounded-xl bg-gradient-to-tr from-blue-600 to-indigo-600 flex items-center justify-center text-white font-black text-sm shadow-xs">
        🐱
      </div>
      <div>
        <div class="flex items-center gap-2">
          <h1 class="font-black text-slate-900 text-xs tracking-tight">老马喵务局 · 端侧智能体系统架构与全量工程物料全景拆解总成</h1>
          <span class="text-[9px] font-mono font-bold px-1.5 py-0.5 rounded-full bg-blue-50 text-blue-700 border border-blue-200">100% 完整无省略 · 视频自动播放</span>
        </div>
        <div class="flex items-center gap-2 text-[10px] font-mono text-slate-400">
          <span>HONOR YOYO AGENT ARCHITECTURE</span>
          <span>•</span>
          <span class="text-emerald-600 font-bold">120/120 全物料覆盖</span>
          <span>•</span>
          <span class="text-indigo-600 font-bold">Figma 式全自由拖拽</span>
        </div>
      </div>
    </div>

    <!-- Center: Exploded Distance Controller -->
    <div class="flex items-center gap-2.5 bg-slate-100/90 py-1 px-3.5 rounded-xl border border-slate-200">
      <span class="text-[11px] font-bold text-slate-700 font-mono flex items-center gap-1.5">
        <span class="w-2 h-2 rounded-full bg-blue-600 animate-pulse"></span>
        <span>拆解度:</span>
      </span>
      <input id="explosion-slider" type="range" min="0" max="100" value="70" class="w-32 accent-blue-600 cursor-pointer">
      <span id="explosion-val" class="text-[11px] font-mono font-bold text-blue-600 w-8 text-right">70%</span>
      <div class="h-3.5 w-px bg-slate-300 mx-0.5"></div>
      <button onclick="setExplosion(0)" class="px-2 py-0.5 text-[9px] font-mono font-bold rounded-lg bg-white text-slate-700 border border-slate-200 hover:bg-slate-50">合拢</button>
      <button onclick="setExplosion(50)" class="px-2 py-0.5 text-[9px] font-mono font-bold rounded-lg bg-white text-slate-700 border border-slate-200 hover:bg-slate-50">标准</button>
      <button onclick="setExplosion(100)" class="px-2 py-0.5 text-[9px] font-mono font-bold rounded-lg bg-white text-blue-700 border border-blue-200 hover:bg-blue-50">全展</button>
    </div>

    <!-- Right: Quick Navigation Dock & Zoom Controls -->
    <div class="flex items-center gap-2">
      <!-- Quick Zone Focus Dock -->
      <div class="flex items-center bg-slate-100/90 p-1 rounded-xl border border-slate-200 text-[11px] font-bold font-mono">
        <button onclick="focusZone('center')" class="px-2 py-0.5 rounded-lg hover:bg-white text-slate-700 transition-all flex items-center gap-1" title="聚焦核心机身装配台">
          <span>🎯</span><span>核心</span>
        </button>
        <button onclick="focusZone('north')" class="px-2 py-0.5 rounded-lg hover:bg-white text-slate-700 transition-all flex items-center gap-1" title="聚焦系统架构总成">
          <span>⚙️</span><span>架构</span>
        </button>
        <button onclick="focusZone('ref')" class="px-2 py-0.5 rounded-lg hover:bg-white text-slate-700 transition-all flex items-center gap-1" title="聚焦生物物理样张">
          <span>📸</span><span>基准</span>
        </button>
        <button onclick="focusZone('candidates')" class="px-2 py-0.5 rounded-lg hover:bg-white text-slate-700 transition-all flex items-center gap-1" title="聚焦CV候选机身">
          <span>🧪</span><span>候选</span>
        </button>
        <button onclick="focusZone('west')" class="px-2 py-0.5 rounded-lg hover:bg-white text-slate-700 transition-all flex items-center gap-1" title="聚焦工程物料BOM">
          <span>📦</span><span>物料</span>
        </button>
        <button onclick="focusZone('east')" class="px-2 py-0.5 rounded-lg hover:bg-white text-slate-700 transition-all flex items-center gap-1" title="聚焦真机远测大屏">
          <span>📱</span><span>真机</span>
        </button>
        <button onclick="focusZone('posters')" class="px-2 py-0.5 rounded-lg hover:bg-white text-slate-700 transition-all flex items-center gap-1" title="聚焦16:9动态视频">
          <span>🎞️</span><span>视频</span>
        </button>
        <button onclick="focusZone('shaders')" class="px-2 py-0.5 rounded-lg hover:bg-white text-slate-700 transition-all flex items-center gap-1" title="聚焦Shader与材质">
          <span>🎨</span><span>材质</span>
        </button>
        <button onclick="focusZone('south')" class="px-2 py-0.5 rounded-lg hover:bg-white text-slate-700 transition-all flex items-center gap-1" title="聚焦工程团队矩阵">
          <span>👥</span><span>人员</span>
        </button>
      </div>

      <!-- Zoom buttons -->
      <div class="flex items-center bg-slate-100/90 p-1 rounded-xl border border-slate-200">
        <button onclick="adjustZoom(0.8)" class="w-7 h-7 rounded-lg hover:bg-white flex items-center justify-center font-mono font-bold text-slate-700" title="缩小">-</button>
        <span id="zoom-level" class="px-1.5 text-[11px] font-mono font-bold text-slate-700 w-11 text-center">100%</span>
        <button onclick="adjustZoom(1.25)" class="w-7 h-7 rounded-lg hover:bg-white flex items-center justify-center font-mono font-bold text-slate-700" title="放大">+</button>
        <button onclick="resetView()" class="px-2 py-0.5 rounded-lg hover:bg-white text-[10px] font-mono font-bold text-slate-700" title="自适应全屏鸟瞰">重置</button>
      </div>
    </div>
  </header>

  <!-- ========================================================================= -->
  <!-- MAIN INFINITE BLUEPRINT VIEWPORT & HARDWARE ACCELERATED STAGE             -->
  <!-- ========================================================================= -->
  <main id="canvas-viewport" class="w-full h-full pt-14 relative overflow-hidden cursor-grab active:cursor-grabbing">
    <!-- Stage: 4800px x 3400px (High-Density Engineering Blueprint) -->
    <div id="canvas-stage" class="absolute pointer-events-auto" style="width: 4800px; height: 3400px;">

      <!-- SVG Dynamic Connector & Assembly Leader Lines -->
      <svg id="svg-leader-lines" class="absolute inset-0 w-full h-full pointer-events-none z-10" xmlns="http://www.w3.org/2000/svg">
        <!-- Lines dynamically computed and injected by drawLeaderLines() -->
      </svg>

      <!-- ===================================================================== -->
      <!-- ZONE NORTH (北部总成 · X: 1550, Y: 80) · 混合容器渲染内核与通信协议总成 -->
      <!-- ===================================================================== -->
      <div id="zone-north" class="absolute z-20 draggable-node blueprint-card p-6 rounded-2xl" style="left: 1550px; top: 80px; width: 1400px;">
        <div class="flex items-center justify-between border-b border-slate-200 pb-3 mb-4 node-drag-handle">
          <div class="flex items-center gap-2.5">
            <span class="w-8 h-8 rounded-xl bg-blue-50 border border-blue-200 flex items-center justify-center text-base">⚙️</span>
            <div>
              <h2 class="text-sm font-black text-slate-900 tracking-tight">端侧智能体系统架构 · 混合容器渲染内核与通信协议总成</h2>
              <span class="text-[10px] font-mono text-blue-600 font-bold">[SYS-CORE-000 · HYBRID CONTAINER & IPC COMMUNICATIONS]</span>
            </div>
          </div>
          <div class="flex items-center gap-2">
            <span class="text-[9px] font-mono text-slate-400">ARCHITECTURAL SPECIFICATION</span>
            <span class="text-[9px] px-2 py-0.5 rounded-full bg-blue-50 text-blue-700 font-mono font-bold border border-blue-200">ACTIVE STABLE</span>
          </div>
        </div>

        <div class="grid grid-cols-4 gap-4 mb-4">
          <div class="p-3.5 rounded-xl bg-slate-50 border border-slate-200">
            <span class="text-[10px] font-mono font-black text-blue-600">LAYER 01 · 核心技术栈</span>
            <h4 class="text-xs font-black text-slate-800 mt-0.5 mb-1.5">高保真混合渲染容器</h4>
            <ul class="text-[10px] text-slate-500 space-y-1 font-mono">
              <li>• 渲染内核: Android WebView 独立进程</li>
              <li>• 样式引擎: Tailwind CSS JIT GPU 加速</li>
              <li>• 物理驱动: React 18 Concurrent Hooks</li>
              <li>• 类型契约: TypeScript 严格数据边界</li>
            </ul>
          </div>

          <div class="p-3.5 rounded-xl bg-slate-50 border border-slate-200 border-l-3 border-l-cyan-600">
            <span class="text-[10px] font-mono font-black text-cyan-600">LAYER 02 · 控制系统</span>
            <h4 class="text-xs font-black text-slate-800 mt-0.5 mb-1.5">FSM 有限状态机与调度</h4>
            <ul class="text-[10px] text-slate-500 space-y-1 font-mono">
              <li>• 状态互斥: Normal / Dirty / Touch 流转</li>
              <li>• 轮询保活: 1000ms 心跳数据上报采样</li>
              <li>• 触发判定: 生理数值加权与滑动滤波</li>
              <li>• 异常拦截: 离线状态安全熔断降级</li>
            </ul>
          </div>

          <div class="p-3.5 rounded-xl bg-slate-50 border border-slate-200 border-l-3 border-l-emerald-600">
            <span class="text-[10px] font-mono font-black text-emerald-600">LAYER 03 · 动画与渲染管线</span>
            <h4 class="text-xs font-black text-slate-800 mt-0.5 mb-1.5">多模态流媒体与动效混合</h4>
            <ul class="text-[10px] text-slate-500 space-y-1 font-mono">
              <li>• 硬件解码: H.264 High Profile 流水线</li>
              <li>• 帧率保障: 60fps 恒定锁帧动态垂直同步</li>
              <li>• 图层合成: Alpha 透明通道与物理背景混色</li>
              <li>• 手势引擎: 240Hz 触控采样与双梯形动力学</li>
            </ul>
          </div>

          <div class="p-3.5 rounded-xl bg-slate-50 border border-slate-200 border-l-3 border-l-indigo-600">
            <span class="text-[10px] font-mono font-black text-indigo-600">LAYER 04 · 硬件协同系统</span>
            <h4 class="text-xs font-black text-slate-800 mt-0.5 mb-1.5">端侧桥接与数据持久化</h4>
            <ul class="text-[10px] text-slate-500 space-y-1 font-mono">
              <li>• 蓝牙广播: BLE 传感器低功耗事件监听</li>
              <li>• 通信协议: JSBridge 双向安全通信总线</li>
              <li>• 数据存储: IndexedDB 异步双写持久化</li>
              <li>• 异常自愈: 状态校验和回滚降级策略</li>
            </ul>
          </div>
        </div>

        <div class="p-3 rounded-xl bg-blue-50/70 border border-blue-200/80 flex items-center justify-between font-mono text-[10px] text-blue-900">
          <div class="flex items-center gap-2">
            <span class="font-black text-blue-700">[HARDWARE TARGET]</span>
            <span>HONOR MAGIC V3 / MAGIC 7 · MAGICOS 9.0 · SNAPDRAGON 8 GEN 3 · DISPLAY 1320 × 2868</span>
          </div>
          <div class="flex items-center gap-3">
            <span>MEM: &lt; 85MB</span>
            <span>GPU: 3.2ms</span>
            <span>IPC: &lt; 4.8ms</span>
          </div>
        </div>
      </div>

      <!-- ===================================================================== -->
      <!-- ZONE NORTHWEST (西北总成 · X: 80, Y: 80) · 实体猫咪真实物理建模基准库   -->
      <!-- ===================================================================== -->
      <div id="zone-reference" class="absolute z-20 draggable-node blueprint-card p-5 rounded-2xl" style="left: 80px; top: 80px; width: 1380px;">
        <div class="flex items-center justify-between border-b border-slate-200 pb-3 mb-3.5 node-drag-handle">
          <div class="flex items-center gap-2.5">
            <span class="w-8 h-8 rounded-xl bg-amber-50 border border-amber-200 flex items-center justify-center text-base">📸</span>
            <div>
              <h3 class="font-black text-slate-900 text-xs">实体猫咪真实物理建模基准库 (严格按 16:9 / 3:4 / 4:3 原始画幅分簇 · 零剪裁)</h3>
              <span class="text-[9px] font-mono text-amber-700 font-bold">[REF-LIB-REAL · MULTI-ASPECT SKELETAL & PHOTOMETRIC BENCHMARK]</span>
            </div>
          </div>
          <span class="text-[9px] px-2 py-0.5 rounded-full bg-amber-50 text-amber-700 font-mono font-bold border border-amber-200">12 UNPROCESSED SAMPLES</span>
        </div>

        <!-- Section A: 16:9 Landscape Wide Photometry -->
        <div class="mb-3.5">
          <div class="flex items-center justify-between mb-1.5">
            <span class="text-[10px] font-black text-slate-700 font-mono flex items-center gap-1">
              <span class="w-1.5 h-1.5 rounded-full bg-amber-500"></span>
              <span>GROUP A · 16:9 宽屏光影环境采样 (1600×900 / 1920×1080 · 宽高比 1.778)</span>
            </span>
            <span class="text-[9px] font-mono text-slate-400">4 SAMPLES</span>
          </div>
          <div class="grid grid-cols-4 gap-2.5">
            <div class="bg-slate-50 p-2 rounded-xl border border-slate-200 cursor-pointer hover:border-amber-400 transition-all" onclick="inspectImage('./assets/real_photos/laoma_real_1.jpg', '物理样张 01 · 蓝眼折射与正坐骨骼 (1600×900)')">
              <div class="w-full aspect-cine-16-9 bg-slate-900/5 rounded-lg overflow-hidden mb-1.5 flex items-center justify-center">
                <img src="./assets/real_photos/laoma_real_1.jpg" class="no-crop-img" alt="样张1">
              </div>
              <div class="text-[9.5px] font-bold text-slate-800 font-mono break-words leading-tight">物理样张 01 · 蓝眼折射与正坐骨骼</div>
              <div class="text-[8px] text-slate-400 font-mono mt-0.5">1600×900 · 16:9 原画幅</div>
            </div>
            <div class="bg-slate-50 p-2 rounded-xl border border-slate-200 cursor-pointer hover:border-amber-400 transition-all" onclick="inspectImage('./assets/real_photos/laoma_real_2.jpg', '物理样张 02 · 伏卧工况与耳廓解剖 (1600×900)')">
              <div class="w-full aspect-cine-16-9 bg-slate-900/5 rounded-lg overflow-hidden mb-1.5 flex items-center justify-center">
                <img src="./assets/real_photos/laoma_real_2.jpg" class="no-crop-img" alt="样张2">
              </div>
              <div class="text-[9.5px] font-bold text-slate-800 font-mono break-words leading-tight">物理样张 02 · 伏卧工况与耳廓解剖</div>
              <div class="text-[8px] text-slate-400 font-mono mt-0.5">1600×900 · 16:9 原画幅</div>
            </div>
            <div class="bg-slate-50 p-2 rounded-xl border border-slate-200 cursor-pointer hover:border-amber-400 transition-all" onclick="inspectImage('./assets/real_photos/laoma_photo_1.jpg', '物理样张 03 · 箱体内空间透视参考 (1920×1080)')">
              <div class="w-full aspect-cine-16-9 bg-slate-900/5 rounded-lg overflow-hidden mb-1.5 flex items-center justify-center">
                <img src="./assets/real_photos/laoma_photo_1.jpg" class="no-crop-img" alt="样张3">
              </div>
              <div class="text-[9.5px] font-bold text-slate-800 font-mono break-words leading-tight">物理样张 03 · 箱内空间透视参考</div>
              <div class="text-[8px] text-slate-400 font-mono mt-0.5">1920×1080 · 16:9 原画幅</div>
            </div>
            <div class="bg-slate-50 p-2 rounded-xl border border-slate-200 cursor-pointer hover:border-amber-400 transition-all" onclick="inspectImage('./assets/real_photos/laoma_photo_2.jpg', '物理样张 04 · 阳光漫反射光影采样 (1920×1080)')">
              <div class="w-full aspect-cine-16-9 bg-slate-900/5 rounded-lg overflow-hidden mb-1.5 flex items-center justify-center">
                <img src="./assets/real_photos/laoma_photo_2.jpg" class="no-crop-img" alt="样张4">
              </div>
              <div class="text-[9.5px] font-bold text-slate-800 font-mono break-words leading-tight">物理样张 04 · 阳光漫反射光影采样</div>
              <div class="text-[8px] text-slate-400 font-mono mt-0.5">1920×1080 · 16:9 原画幅</div>
            </div>
          </div>
        </div>

        <!-- Section B: 3:4 Portrait Bio-Skeletal References -->
        <div class="mb-3.5">
          <div class="flex items-center justify-between mb-1.5">
            <span class="text-[10px] font-black text-slate-700 font-mono flex items-center gap-1">
              <span class="w-1.5 h-1.5 rounded-full bg-cyan-500"></span>
              <span>GROUP B · 3:4 垂直骨骼与脊椎解剖观测 (1200×1600 · 宽高比 0.750)</span>
            </span>
            <span class="text-[9px] font-mono text-slate-400">5 SAMPLES</span>
          </div>
          <div class="grid grid-cols-5 gap-2.5">
            <div class="bg-slate-50 p-2 rounded-xl border border-slate-200 cursor-pointer hover:border-cyan-400 transition-all" onclick="inspectImage('./assets/real_photos/laoma_real_3.jpg', '骨骼样张 01 · 站立侧身脊椎弧度')">
              <div class="w-full aspect-photo-3-4 bg-slate-900/5 rounded-lg overflow-hidden mb-1.5 flex items-center justify-center">
                <img src="./assets/real_photos/laoma_real_3.jpg" class="no-crop-img" alt="骨骼1">
              </div>
              <div class="text-[9.5px] font-bold text-slate-800 font-mono break-words leading-tight">骨骼 01 · 站立脊椎弧度</div>
              <div class="text-[8px] text-slate-400 font-mono mt-0.5">1200×1600 · 3:4 比例</div>
            </div>
            <div class="bg-slate-50 p-2 rounded-xl border border-slate-200 cursor-pointer hover:border-cyan-400 transition-all" onclick="inspectImage('./assets/real_photos/laoma_real_4.jpg', '骨骼样张 02 · 伏地探头警戒形态')">
              <div class="w-full aspect-photo-3-4 bg-slate-900/5 rounded-lg overflow-hidden mb-1.5 flex items-center justify-center">
                <img src="./assets/real_photos/laoma_real_4.jpg" class="no-crop-img" alt="骨骼2">
              </div>
              <div class="text-[9.5px] font-bold text-slate-800 font-mono break-words leading-tight">骨骼 02 · 伏地探头警戒</div>
              <div class="text-[8px] text-slate-400 font-mono mt-0.5">1200×1600 · 3:4 比例</div>
            </div>
            <div class="bg-slate-50 p-2 rounded-xl border border-slate-200 cursor-pointer hover:border-cyan-400 transition-all" onclick="inspectImage('./assets/real_photos/laoma_real_5.jpg', '骨骼样张 03 · 蜷缩入睡放松肌肉群')">
              <div class="w-full aspect-photo-3-4 bg-slate-900/5 rounded-lg overflow-hidden mb-1.5 flex items-center justify-center">
                <img src="./assets/real_photos/laoma_real_5.jpg" class="no-crop-img" alt="骨骼3">
              </div>
              <div class="text-[9.5px] font-bold text-slate-800 font-mono break-words leading-tight">骨骼 03 · 蜷缩放松肌群</div>
              <div class="text-[8px] text-slate-400 font-mono mt-0.5">1200×1600 · 3:4 比例</div>
            </div>
            <div class="bg-slate-50 p-2 rounded-xl border border-slate-200 cursor-pointer hover:border-cyan-400 transition-all" onclick="inspectImage('./assets/real_photos/laoma_real_6.jpg', '骨骼样张 04 · 后腿蹬踏动力学')">
              <div class="w-full aspect-photo-3-4 bg-slate-900/5 rounded-lg overflow-hidden mb-1.5 flex items-center justify-center">
                <img src="./assets/real_photos/laoma_real_6.jpg" class="no-crop-img" alt="骨骼4">
              </div>
              <div class="text-[9.5px] font-bold text-slate-800 font-mono break-words leading-tight">骨骼 04 · 后腿蹬踏动力</div>
              <div class="text-[8px] text-slate-400 font-mono mt-0.5">1200×1600 · 3:4 比例</div>
            </div>
            <div class="bg-slate-50 p-2 rounded-xl border border-slate-200 cursor-pointer hover:border-cyan-400 transition-all" onclick="inspectImage('./assets/real_photos/laoma_real_7.jpg', '骨骼样张 05 · 直立抬头空间视点')">
              <div class="w-full aspect-photo-3-4 bg-slate-900/5 rounded-lg overflow-hidden mb-1.5 flex items-center justify-center">
                <img src="./assets/real_photos/laoma_real_7.jpg" class="no-crop-img" alt="骨骼5">
              </div>
              <div class="text-[9.5px] font-bold text-slate-800 font-mono break-words leading-tight">骨骼 05 · 直立视点解剖</div>
              <div class="text-[8px] text-slate-400 font-mono mt-0.5">1200×1600 · 3:4 比例</div>
            </div>
          </div>
        </div>

        <!-- Section C: 4:3 Macro Lens Photometry -->
        <div>
          <div class="flex items-center justify-between mb-1.5">
            <span class="text-[10px] font-black text-slate-700 font-mono flex items-center gap-1">
              <span class="w-1.5 h-1.5 rounded-full bg-emerald-500"></span>
              <span>GROUP C · 4:3 微距光学测光与毛发高光反射 (5712×4284 · 宽高比 1.333)</span>
            </span>
            <span class="text-[9px] font-mono text-slate-400">3 SAMPLES</span>
          </div>
          <div class="grid grid-cols-3 gap-2.5">
            <div class="bg-slate-50 p-2 rounded-xl border border-slate-200 cursor-pointer hover:border-emerald-400 transition-all" onclick="inspectImage('./assets/real_photos/laoma_photo_3.jpg', '微距光学 01 · 毛发高频法线与次表面散射 (5712×4284)')">
              <div class="w-full aspect-photo-4-3 bg-slate-900/5 rounded-lg overflow-hidden mb-1.5 flex items-center justify-center">
                <img src="./assets/real_photos/laoma_photo_3.jpg" class="no-crop-img" alt="微距1">
              </div>
              <div class="text-[9.5px] font-bold text-slate-800 font-mono break-words leading-tight">微距 01 · 毛发法线次表面散射</div>
              <div class="text-[8px] text-slate-400 font-mono mt-0.5">5712×4284 · 4:3 原图</div>
            </div>
            <div class="bg-slate-50 p-2 rounded-xl border border-slate-200 cursor-pointer hover:border-emerald-400 transition-all" onclick="inspectImage('./assets/real_photos/laoma_photo_4.jpg', '微距光学 02 · 虹膜收缩与瞳孔高动态范围 (5712×4284)')">
              <div class="w-full aspect-photo-4-3 bg-slate-900/5 rounded-lg overflow-hidden mb-1.5 flex items-center justify-center">
                <img src="./assets/real_photos/laoma_photo_4.jpg" class="no-crop-img" alt="微距2">
              </div>
              <div class="text-[9.5px] font-bold text-slate-800 font-mono break-words leading-tight">微距 02 · 虹膜瞳孔高动态反射</div>
              <div class="text-[8px] text-slate-400 font-mono mt-0.5">5712×4284 · 4:3 原图</div>
            </div>
            <div class="bg-slate-50 p-2 rounded-xl border border-slate-200 cursor-pointer hover:border-emerald-400 transition-all" onclick="inspectImage('./assets/real_photos/laoma_photo_5.jpg', '微距光学 03 · 鼻吻部触觉感知物理建模 (5712×4284)')">
              <div class="w-full aspect-photo-4-3 bg-slate-900/5 rounded-lg overflow-hidden mb-1.5 flex items-center justify-center">
                <img src="./assets/real_photos/laoma_photo_5.jpg" class="no-crop-img" alt="微距3">
              </div>
              <div class="text-[9.5px] font-bold text-slate-800 font-mono break-words leading-tight">微距 03 · 鼻吻部触觉感知建模</div>
              <div class="text-[8px] text-slate-400 font-mono mt-0.5">5712×4284 · 4:3 原图</div>
            </div>
          </div>
        </div>
      </div>

      <!-- ===================================================================== -->
      <!-- ZONE NORTHEAST (东北总成 · X: 3050, Y: 80) · 视觉识别与多工况候选机身阵列 -->
      <!-- ===================================================================== -->
      <div id="zone-candidates" class="absolute z-20 draggable-node blueprint-card p-5 rounded-2xl" style="left: 3050px; top: 80px; width: 1650px;">
        <div class="flex items-center justify-between border-b border-slate-200 pb-3 mb-3.5 node-drag-handle">
          <div class="flex items-center gap-2.5">
            <span class="w-8 h-8 rounded-xl bg-rose-50 border border-rose-200 flex items-center justify-center text-base">🧪</span>
            <div>
              <h3 class="font-black text-slate-900 text-xs">视觉与场景识别迭代候选机身阵列 (19.5:9 手机全画幅演进 · 零裁剪)</h3>
              <span class="text-[9px] font-mono text-rose-700 font-bold">[EXP-CANDIDATES · 19.5:9 CV & VIEWPORT ITERATION CANDIDATES]</span>
            </div>
          </div>
          <span class="text-[9px] px-2 py-0.5 rounded-full bg-rose-50 text-rose-700 font-mono font-bold border border-rose-200">17 CANDIDATE STATES</span>
        </div>

        <!-- Section A: 19.5:9 CV Dirty State Candidates -->
        <div class="mb-3.5">
          <div class="flex items-center justify-between mb-1.5">
            <span class="text-[10px] font-black text-slate-700 font-mono flex items-center gap-1">
              <span class="w-1.5 h-1.5 rounded-full bg-rose-500"></span>
              <span>GROUP A · 19.5:9 视觉脏污判定模型候选样张 (851×1848 / 941×1672)</span>
            </span>
            <span class="text-[9px] font-mono text-slate-400">6 SAMPLES</span>
          </div>
          <div class="grid grid-cols-6 gap-2.5">
            <div class="bg-slate-50 p-1.5 rounded-xl border border-slate-200 cursor-pointer hover:border-rose-400 transition-all" onclick="inspectImage('./assets/candidates/dirty_cat_candidate_1.png', 'CV候选01 · 办公工位脏污轻度')">
              <div class="w-full aspect-phone bg-slate-900/5 rounded-lg overflow-hidden mb-1 flex items-center justify-center">
                <img src="./assets/candidates/dirty_cat_candidate_1.png" class="no-crop-img" alt="脏污1">
              </div>
              <div class="text-[9px] font-bold text-slate-800 font-mono break-words leading-tight">工位轻度脏污</div>
              <div class="text-[7.5px] text-slate-400 font-mono mt-0.5">851×1848</div>
            </div>
            <div class="bg-slate-50 p-1.5 rounded-xl border border-slate-200 cursor-pointer hover:border-rose-400 transition-all" onclick="inspectImage('./assets/candidates/dirty_cat_candidate_2.png', 'CV候选02 · 地面泥泞脏污中度')">
              <div class="w-full aspect-phone bg-slate-900/5 rounded-lg overflow-hidden mb-1 flex items-center justify-center">
                <img src="./assets/candidates/dirty_cat_candidate_2.png" class="no-crop-img" alt="脏污2">
              </div>
              <div class="text-[9px] font-bold text-slate-800 font-mono break-words leading-tight">地面泥泞脏污</div>
              <div class="text-[7.5px] text-slate-400 font-mono mt-0.5">851×1848</div>
            </div>
            <div class="bg-slate-50 p-1.5 rounded-xl border border-slate-200 cursor-pointer hover:border-rose-400 transition-all" onclick="inspectImage('./assets/candidates/dirty_cat_candidate_3.png', 'CV候选03 · 户外探险脏污重度')">
              <div class="w-full aspect-phone bg-slate-900/5 rounded-lg overflow-hidden mb-1 flex items-center justify-center">
                <img src="./assets/candidates/dirty_cat_candidate_3.png" class="no-crop-img" alt="脏污3">
              </div>
              <div class="text-[9px] font-bold text-slate-800 font-mono break-words leading-tight">户外重度脏污</div>
              <div class="text-[7.5px] text-slate-400 font-mono mt-0.5">851×1848</div>
            </div>
            <div class="bg-slate-50 p-1.5 rounded-xl border border-slate-200 cursor-pointer hover:border-rose-400 transition-all" onclick="inspectImage('./assets/candidates/dirty_cat_sample_1.png', '姿态样张01 · 侧卧脏污识别')">
              <div class="w-full aspect-phone bg-slate-900/5 rounded-lg overflow-hidden mb-1 flex items-center justify-center">
                <img src="./assets/candidates/dirty_cat_sample_1.png" class="no-crop-img" alt="样张1">
              </div>
              <div class="text-[9px] font-bold text-slate-800 font-mono break-words leading-tight">侧卧脏污采样</div>
              <div class="text-[7.5px] text-slate-400 font-mono mt-0.5">941×1672</div>
            </div>
            <div class="bg-slate-50 p-1.5 rounded-xl border border-slate-200 cursor-pointer hover:border-rose-400 transition-all" onclick="inspectImage('./assets/candidates/dirty_cat_sample_2.png', '姿态样张02 · 伏击脏污识别')">
              <div class="w-full aspect-phone bg-slate-900/5 rounded-lg overflow-hidden mb-1 flex items-center justify-center">
                <img src="./assets/candidates/dirty_cat_sample_2.png" class="no-crop-img" alt="样张2">
              </div>
              <div class="text-[9px] font-bold text-slate-800 font-mono break-words leading-tight">伏击姿态识别</div>
              <div class="text-[7.5px] text-slate-400 font-mono mt-0.5">941×1672</div>
            </div>
            <div class="bg-slate-50 p-1.5 rounded-xl border border-slate-200 cursor-pointer hover:border-rose-400 transition-all" onclick="inspectImage('./assets/candidates/dirty_cat_sample_3.png', '姿态样张03 · 站立脏污识别')">
              <div class="w-full aspect-phone bg-slate-900/5 rounded-lg overflow-hidden mb-1 flex items-center justify-center">
                <img src="./assets/candidates/dirty_cat_sample_3.png" class="no-crop-img" alt="样张3">
              </div>
              <div class="text-[9px] font-bold text-slate-800 font-mono break-words leading-tight">站立脏污识别</div>
              <div class="text-[7.5px] text-slate-400 font-mono mt-0.5">941×1672</div>
            </div>
          </div>
        </div>

        <!-- Section B: 19.5:9 Native Resolution Multi-State Viewport Renders -->
        <div class="mb-3.5">
          <div class="flex items-center justify-between mb-1.5">
            <span class="text-[10px] font-black text-slate-700 font-mono flex items-center gap-1">
              <span class="w-1.5 h-1.5 rounded-full bg-blue-500"></span>
              <span>GROUP B · 19.5:9 原生全分辨率多工况渲染帧 (1320×2868 原生视口 · 零剪裁)</span>
            </span>
            <span class="text-[9px] font-mono text-slate-400">6 FRAMES</span>
          </div>
          <div class="grid grid-cols-6 gap-2.5">
            <div class="bg-slate-50 p-1.5 rounded-xl border border-slate-200 cursor-pointer hover:border-blue-400 transition-all" onclick="inspectImage('./assets/app_assets/app_bg.png', '基线背景 · 1320×2868 纯净居室底图')">
              <div class="w-full aspect-phone bg-slate-900/5 rounded-lg overflow-hidden mb-1 flex items-center justify-center">
                <img src="./assets/app_assets/app_bg.png" class="no-crop-img" alt="app_bg">
              </div>
              <div class="text-[9px] font-bold text-slate-800 font-mono break-words leading-tight">居室基线纯底图</div>
              <div class="text-[7.5px] text-slate-400 font-mono mt-0.5">1320×2868</div>
            </div>
            <div class="bg-slate-50 p-1.5 rounded-xl border border-slate-200 cursor-pointer hover:border-blue-400 transition-all" onclick="inspectImage('./assets/candidates/home_bg_clean_1320x2868.png', '基线渲染 · 1320×2868 纯净居室标准光照')">
              <div class="w-full aspect-phone bg-slate-900/5 rounded-lg overflow-hidden mb-1 flex items-center justify-center">
                <img src="./assets/candidates/home_bg_clean_1320x2868.png" class="no-crop-img" alt="home_bg_clean">
              </div>
              <div class="text-[9px] font-bold text-slate-800 font-mono break-words leading-tight">居室标准光照图</div>
              <div class="text-[7.5px] text-slate-400 font-mono mt-0.5">1320×2868</div>
            </div>
            <div class="bg-slate-50 p-1.5 rounded-xl border border-slate-200 cursor-pointer hover:border-blue-400 transition-all" onclick="inspectImage('./assets/candidates/home_cat_bg_clean_1320x2868.png', '工况合成 · 1320×2868 纯净常态猫咪完整视口')">
              <div class="w-full aspect-phone bg-slate-900/5 rounded-lg overflow-hidden mb-1 flex items-center justify-center">
                <img src="./assets/candidates/home_cat_bg_clean_1320x2868.png" class="no-crop-img" alt="home_cat_bg_clean">
              </div>
              <div class="text-[9px] font-bold text-slate-800 font-mono break-words leading-tight">纯净常态完整视口</div>
              <div class="text-[7.5px] text-slate-400 font-mono mt-0.5">1320×2868</div>
            </div>
            <div class="bg-slate-50 p-1.5 rounded-xl border border-slate-200 cursor-pointer hover:border-blue-400 transition-all" onclick="inspectImage('./assets/candidates/home_cat_dirty_tap_1320x2868.png', '工况合成 · 1320×2868 脏污高灵敏触碰视口')">
              <div class="w-full aspect-phone bg-slate-900/5 rounded-lg overflow-hidden mb-1 flex items-center justify-center">
                <img src="./assets/candidates/home_cat_dirty_tap_1320x2868.png" class="no-crop-img" alt="home_cat_dirty_tap">
              </div>
              <div class="text-[9px] font-bold text-slate-800 font-mono break-words leading-tight">脏污触碰反馈视口</div>
              <div class="text-[7.5px] text-slate-400 font-mono mt-0.5">1320×2868</div>
            </div>
            <div class="bg-slate-50 p-1.5 rounded-xl border border-slate-200 cursor-pointer hover:border-blue-400 transition-all" onclick="inspectImage('./assets/candidates/home_cat_touch_screen_1320x2868.png', '工况合成 · 1320×2868 屏幕互动触碰贴合视口')">
              <div class="w-full aspect-phone bg-slate-900/5 rounded-lg overflow-hidden mb-1 flex items-center justify-center">
                <img src="./assets/candidates/home_cat_touch_screen_1320x2868.png" class="no-crop-img" alt="home_cat_touch">
              </div>
              <div class="text-[9px] font-bold text-slate-800 font-mono break-words leading-tight">屏幕贴合互动视口</div>
              <div class="text-[7.5px] text-slate-400 font-mono mt-0.5">1320×2868</div>
            </div>
            <div class="bg-slate-50 p-1.5 rounded-xl border border-slate-200 cursor-pointer hover:border-blue-400 transition-all" onclick="inspectImage('./assets/candidates/home_bg_clean_exact_ratio.png', '校准基线 · 848×1844 精密等比视口标定图')">
              <div class="w-full aspect-phone bg-slate-900/5 rounded-lg overflow-hidden mb-1 flex items-center justify-center">
                <img src="./assets/candidates/home_bg_clean_exact_ratio.png" class="no-crop-img" alt="exact_ratio">
              </div>
              <div class="text-[9px] font-bold text-slate-800 font-mono break-words leading-tight">等比标定基准图</div>
              <div class="text-[7.5px] text-slate-400 font-mono mt-0.5">848×1844</div>
            </div>
          </div>
        </div>

        <!-- Section C: Office Ambient Dirty Cat Candidates & Mid-Res -->
        <div>
          <div class="flex items-center justify-between mb-1.5">
            <span class="text-[10px] font-black text-slate-700 font-mono flex items-center gap-1">
              <span class="w-1.5 h-1.5 rounded-full bg-amber-500"></span>
              <span>GROUP C · 办公环境光照与手势验证样张 (851×1848 / 650×1414 · 零剪裁)</span>
            </span>
            <span class="text-[9px] font-mono text-slate-400">5 SAMPLES</span>
          </div>
          <div class="grid grid-cols-5 gap-2.5">
            <div class="bg-slate-50 p-1.5 rounded-xl border border-slate-200 cursor-pointer hover:border-amber-400 transition-all" onclick="inspectImage('./assets/candidates/office_dirty_cat_candidate_1.png', '办公光照候选 01 (851×1848)')">
              <div class="w-full aspect-phone bg-slate-900/5 rounded-lg overflow-hidden mb-1 flex items-center justify-center">
                <img src="./assets/candidates/office_dirty_cat_candidate_1.png" class="no-crop-img" alt="办公候选1">
              </div>
              <div class="text-[9px] font-bold text-slate-800 font-mono break-words leading-tight">自然光位脏污</div>
              <div class="text-[7.5px] text-slate-400 font-mono mt-0.5">851×1848</div>
            </div>
            <div class="bg-slate-50 p-1.5 rounded-xl border border-slate-200 cursor-pointer hover:border-amber-400 transition-all" onclick="inspectImage('./assets/candidates/office_dirty_cat_candidate_2.png', '办公光照候选 02 (851×1848)')">
              <div class="w-full aspect-phone bg-slate-900/5 rounded-lg overflow-hidden mb-1 flex items-center justify-center">
                <img src="./assets/candidates/office_dirty_cat_candidate_2.png" class="no-crop-img" alt="办公候选2">
              </div>
              <div class="text-[9px] font-bold text-slate-800 font-mono break-words leading-tight">荧光灯位脏污</div>
              <div class="text-[7.5px] text-slate-400 font-mono mt-0.5">851×1848</div>
            </div>
            <div class="bg-slate-50 p-1.5 rounded-xl border border-slate-200 cursor-pointer hover:border-amber-400 transition-all" onclick="inspectImage('./assets/candidates/office_dirty_cat_candidate_3.png', '办公光照候选 03 (851×1848)')">
              <div class="w-full aspect-phone bg-slate-900/5 rounded-lg overflow-hidden mb-1 flex items-center justify-center">
                <img src="./assets/candidates/office_dirty_cat_candidate_3.png" class="no-crop-img" alt="办公候选3">
              </div>
              <div class="text-[9px] font-bold text-slate-800 font-mono break-words leading-tight">背光阴影脏污</div>
              <div class="text-[7.5px] text-slate-400 font-mono mt-0.5">851×1848</div>
            </div>
            <div class="bg-slate-50 p-1.5 rounded-xl border border-slate-200 cursor-pointer hover:border-indigo-400 transition-all" onclick="inspectImage('./assets/app_assets/scenes/leaderboard_magic_glass.png', '场景探索 01 · 魔法毛玻璃排行榜')">
              <div class="w-full aspect-phone bg-slate-900/5 rounded-lg overflow-hidden mb-1 flex items-center justify-center">
                <img src="./assets/app_assets/scenes/leaderboard_magic_glass.png" class="no-crop-img" alt="毛玻璃">
              </div>
              <div class="text-[9px] font-bold text-slate-800 font-mono break-words leading-tight">毛玻璃排行榜探索</div>
              <div class="text-[7.5px] text-slate-400 font-mono mt-0.5">851×1848</div>
            </div>
            <div class="bg-slate-50 p-1.5 rounded-xl border border-slate-200 cursor-pointer hover:border-indigo-400 transition-all" onclick="inspectImage('./assets/app_assets/scenes/leaderboard_cozy_journal.png', '场景探索 02 · 暖调手账持久化记录')">
              <div class="w-full aspect-phone bg-slate-900/5 rounded-lg overflow-hidden mb-1 flex items-center justify-center">
                <img src="./assets/app_assets/scenes/leaderboard_cozy_journal.png" class="no-crop-img" alt="暖调手账">
              </div>
              <div class="text-[9px] font-bold text-slate-800 font-mono break-words leading-tight">暖调手账卡片探索</div>
              <div class="text-[7.5px] text-slate-400 font-mono mt-0.5">851×1849</div>
            </div>
          </div>
        </div>
      </div>

      <!-- ===================================================================== -->
      <!-- CENTER CORE ASSEMBLY (中心总装 · X: 2050, Y: 1050) · 真实应用界面与四大子系统展开 -->
      <!-- ===================================================================== -->
      <!-- 1. Central Honor Magic Device Frame (搭载真实应用界面截图) -->
      <div id="core-device-frame" class="absolute z-30 draggable-node" style="left: 2050px; top: 1050px; width: 380px; height: 820px;">
        <div class="absolute -top-7 left-0 right-0 flex items-center justify-between font-mono text-[9px] text-blue-600 font-bold px-1 node-drag-handle">
          <span>[HONOR MAGIC NATIVE CHASSIS · 真实应用界面]</span>
          <span>1320 × 2868 · LTPO</span>
        </div>

        <!-- Phone Bezel -->
        <div class="w-full h-full bg-slate-900 rounded-[48px] p-2.5 shadow-2xl border-4 border-slate-700/90 ring-1 ring-white/20 relative flex flex-col justify-between">
          <!-- Dynamic Island / Speaker punch-hole -->
          <div class="absolute top-2 left-1/2 -translate-x-1/2 w-24 h-5 bg-black rounded-full z-50 flex items-center justify-between px-2 text-[9px] text-white">
            <span class="font-mono text-[8px] text-slate-400">17:45</span>
            <div class="w-2 h-2 rounded-full bg-slate-900 border border-slate-700"></div>
            <span class="text-[8px] text-emerald-400 font-mono">5G 100%</span>
          </div>

          <!-- Phone Screen Container (19.5:9 Native Viewport · 搭载真实截图) -->
          <div class="w-full h-full bg-white rounded-[38px] overflow-hidden relative border border-slate-800 flex flex-col justify-between select-none">
            <!-- 真实应用界面截图 (支持交互切换) -->
            <img id="phone-screen-img" src="./assets/screenshots/Screenshot_20260919_174540_com_lyi_laomayoyo_MainActivity.JPG" class="w-full h-full object-contain cursor-pointer" alt="真实应用界面" onclick="inspectImage(this.src, '荣耀真机实时实测应用界面 (1320×2868)')">
            
            <!-- Live Active Indicator -->
            <div class="absolute bottom-2.5 right-2.5 z-20 bg-black/60 backdrop-blur-md px-2 py-0.5 rounded-full text-[9px] text-white font-mono font-bold flex items-center gap-1 pointer-events-none">
              <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-ping"></span>
              <span id="current-screen-tag">STATE: 01 居室常态静止巡航</span>
            </div>
          </div>
        </div>

        <!-- 8 款真机工况截图即时切换控制坞 (Dock underneath chassis) -->
        <div class="absolute -bottom-11 left-1/2 -translate-x-1/2 bg-white/95 backdrop-blur-md p-1 rounded-xl border border-slate-200 shadow-md flex items-center gap-1 z-40">
          <button onclick="switchPhoneScreen(1)" id="btn-scr-1" class="px-2 py-0.5 rounded-lg text-[9px] font-mono font-bold bg-blue-600 text-white transition-all">01常态</button>
          <button onclick="switchPhoneScreen(2)" id="btn-scr-2" class="px-2 py-0.5 rounded-lg text-[9px] font-mono font-bold hover:bg-slate-100 text-slate-700 transition-all">02触控</button>
          <button onclick="switchPhoneScreen(3)" id="btn-scr-3" class="px-2 py-0.5 rounded-lg text-[9px] font-mono font-bold hover:bg-slate-100 text-slate-700 transition-all">03脏污</button>
          <button onclick="switchPhoneScreen(4)" id="btn-scr-4" class="px-2 py-0.5 rounded-lg text-[9px] font-mono font-bold hover:bg-slate-100 text-slate-700 transition-all">04抚触</button>
          <button onclick="switchPhoneScreen(5)" id="btn-scr-5" class="px-2 py-0.5 rounded-lg text-[9px] font-mono font-bold hover:bg-slate-100 text-slate-700 transition-all">05投喂</button>
          <button onclick="switchPhoneScreen(6)" id="btn-scr-6" class="px-2 py-0.5 rounded-lg text-[9px] font-mono font-bold hover:bg-slate-100 text-slate-700 transition-all">06逗猫</button>
          <button onclick="switchPhoneScreen(7)" id="btn-scr-7" class="px-2 py-0.5 rounded-lg text-[9px] font-mono font-bold hover:bg-slate-100 text-slate-700 transition-all">07体检</button>
          <button onclick="switchPhoneScreen(8)" id="btn-scr-8" class="px-2 py-0.5 rounded-lg text-[9px] font-mono font-bold hover:bg-slate-100 text-slate-700 transition-all">08安睡</button>
        </div>
      </div>

      <!-- 2. Exploded Sub-Assembly 01: Top HUD & Gauges System (ASM-01 · SENSORS) -->
      <div id="module-gauges" class="absolute z-20 draggable-node exploded-sub-module blueprint-card p-4 rounded-2xl cursor-pointer hover:border-blue-500" style="left: 1990px; top: 680px; width: 500px;" onclick="inspectComponent('gauges')">
        <div class="flex items-center justify-between border-b border-slate-200 pb-2 mb-2.5 node-drag-handle">
          <div class="flex items-center gap-2">
            <span class="w-6 h-6 rounded-lg bg-blue-50 border border-blue-200 flex items-center justify-center text-xs">📊</span>
            <div>
              <h4 class="text-xs font-black text-slate-900">状态感知与生命指标控制系统</h4>
              <span class="text-[8.5px] font-mono text-blue-600 font-bold">[ASM-01 · SENSORS & HUD GAUGES]</span>
            </div>
          </div>
          <span class="text-[8.5px] font-mono px-2 py-0.5 rounded-full bg-blue-50 text-blue-700 font-bold">DISSECTED</span>
        </div>

        <!-- Gauge Controls Matrix -->
        <div class="grid grid-cols-3 gap-2 text-center">
          <div class="p-2 rounded-xl bg-slate-50 border border-slate-200">
            <div class="w-8 h-8 mx-auto mb-1 flex items-center justify-center">
              <img src="./assets/app_assets/ui_icons/ic_index_catlove.png" class="no-crop-img" alt="爱猫">
            </div>
            <div class="text-[10px] font-black text-slate-800 font-mono">98.6%</div>
            <div class="text-[8px] text-slate-500 font-mono">爱猫指数加权</div>
          </div>
          <div class="p-2 rounded-xl bg-slate-50 border border-slate-200">
            <div class="w-8 h-8 mx-auto mb-1 flex items-center justify-center">
              <img src="./assets/app_assets/ui_icons/ic_index_happiness.png" class="no-crop-img" alt="快乐">
            </div>
            <div class="text-[10px] font-black text-slate-800 font-mono">HEALTHY</div>
            <div class="text-[8px] text-slate-500 font-mono">生理状态监测</div>
          </div>
          <div class="p-2 rounded-xl bg-slate-50 border border-slate-200">
            <div class="w-8 h-8 mx-auto mb-1 flex items-center justify-center">
              <img src="./assets/app_assets/ui_icons/ic_btn_trophy.png" class="no-crop-img" alt="奖杯">
            </div>
            <div class="text-[10px] font-black text-slate-800 font-mono">NO.1 领先</div>
            <div class="text-[8px] text-slate-500 font-mono">荣誉段位同步</div>
          </div>
        </div>
      </div>

      <!-- 3. Exploded Sub-Assembly 02: Media Stream & GPU Render Pipeline (ASM-02 · MEDIA) -->
      <!-- 视频稍微放大，采用 19.5:9 竖屏原生画幅，静音自动循环播放 -->
      <div id="module-media" class="absolute z-20 draggable-node exploded-sub-module blueprint-card p-4 rounded-2xl cursor-pointer hover:border-emerald-500" style="left: 2540px; top: 1050px; width: 580px;" onclick="inspectComponent('media')">
        <div class="flex items-center justify-between border-b border-slate-200 pb-2 mb-2.5 node-drag-handle">
          <div class="flex items-center gap-2">
            <span class="w-6 h-6 rounded-lg bg-emerald-50 border border-emerald-200 flex items-center justify-center text-xs">🎬</span>
            <div>
              <h4 class="text-xs font-black text-slate-900">视觉多媒体流解码管线 (自动循环播放中)</h4>
              <span class="text-[8.5px] font-mono text-emerald-600 font-bold">[ASM-02 · 19.5:9 VERTICAL STREAMS · AUTOPLAY]</span>
            </div>
          </div>
          <span class="text-[8.5px] font-mono px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-700 font-bold">60 FPS LOCKED</span>
        </div>

        <!-- 3 Enhanced Vertical Stream Cards with AUTOPLAYING VIDEOS (High-Contrast White Labels) -->
        <div class="grid grid-cols-3 gap-2.5 mb-2.5">
          <div class="bg-slate-950 rounded-xl p-1.5 border border-slate-800 flex flex-col items-center shadow-md">
            <div class="w-full aspect-phone-sample bg-black rounded-lg overflow-hidden mb-1.5 relative flex items-center justify-center">
              <video src="./assets/app_assets/home_cat_clean.mp4" autoplay loop muted playsinline class="w-full h-full object-contain"></video>
              <span class="absolute top-1 left-1 px-1 py-0.2 rounded bg-emerald-500/90 text-[7.5px] text-white font-mono font-bold">STREAM 01</span>
            </div>
            <div class="text-[10px] font-black text-slate-100 text-center font-mono break-words leading-tight">01 · 正常巡航态</div>
            <div class="text-[7.5px] text-emerald-400 font-mono mt-0.5">650×1414 · 60FPS</div>
          </div>
          <div class="bg-slate-950 rounded-xl p-1.5 border border-slate-800 flex flex-col items-center shadow-md">
            <div class="w-full aspect-phone-sample bg-black rounded-lg overflow-hidden mb-1.5 relative flex items-center justify-center">
              <video src="./assets/app_assets/home_cat_dirty.mp4" autoplay loop muted playsinline class="w-full h-full object-contain"></video>
              <span class="absolute top-1 left-1 px-1 py-0.2 rounded bg-amber-500/90 text-[7.5px] text-white font-mono font-bold">STREAM 02</span>
            </div>
            <div class="text-[10px] font-black text-slate-100 text-center font-mono break-words leading-tight">02 · 脏污告警态</div>
            <div class="text-[7.5px] text-amber-400 font-mono mt-0.5">650×1414 · 60FPS</div>
          </div>
          <div class="bg-slate-950 rounded-xl p-1.5 border border-slate-800 flex flex-col items-center shadow-md">
            <div class="w-full aspect-phone-sample bg-black rounded-lg overflow-hidden mb-1.5 relative flex items-center justify-center">
              <video src="./assets/app_assets/home_cat_touch.mp4" autoplay loop muted playsinline class="w-full h-full object-contain"></video>
              <span class="absolute top-1 left-1 px-1 py-0.2 rounded bg-rose-500/90 text-[7.5px] text-white font-mono font-bold">STREAM 03</span>
            </div>
            <div class="text-[10px] font-black text-slate-100 text-center font-mono break-words leading-tight">03 · 触控互动态</div>
            <div class="text-[7.5px] text-rose-400 font-mono mt-0.5">650×1414 · 60FPS</div>
          </div>
        </div>
        <div class="flex items-center justify-between text-[8.5px] font-mono text-slate-500 bg-slate-100/80 p-1.5 rounded-lg">
          <span>CODEC: H.264 HARDWARE</span>
          <span>AUTOPLAY: CONTINUOUS</span>
        </div>
      </div>

      <!-- 4. Exploded Sub-Assembly 03: 24H Spatial Timeline & ALL 11 Care Props (ASM-03 · TIMELINE) -->
      <!-- 展示完整 11 项事件道具，绝不切除或省略 -->
      <div id="module-timeline" class="absolute z-20 draggable-node exploded-sub-module blueprint-card p-4 rounded-2xl cursor-pointer hover:border-amber-500" style="left: 1320px; top: 1050px; width: 680px;" onclick="inspectComponent('timeline')">
        <div class="flex items-center justify-between border-b border-slate-200 pb-2 mb-2.5 node-drag-handle">
          <div class="flex items-center gap-2">
            <span class="w-6 h-6 rounded-lg bg-amber-50 border border-amber-200 flex items-center justify-center text-xs">⏱️</span>
            <div>
              <h4 class="text-xs font-black text-slate-900">24H 空间感知与事件调度总线 (11 大部件全量展示 · 文字自适应)</h4>
              <span class="text-[8.5px] font-mono text-amber-600 font-bold">[ASM-03 · ALL 11 EVENTS SCHEDULED & UNABRIDGED]</span>
            </div>
          </div>
          <span class="text-[8.5px] font-mono px-2 py-0.5 rounded-full bg-amber-50 text-amber-700 font-bold">11 PROPS</span>
        </div>

        <div id="dissected-timeline-grid" class="grid grid-cols-3 gap-2 mb-2">
          <!-- Dynamically filled via JS with ALL 11 3D Props with FULL TITLES in comfortable horizontal cards -->
        </div>
        <div class="text-[8.5px] font-mono text-slate-500 bg-slate-100/80 p-1.5 rounded-lg flex items-center justify-between">
          <span>24H CIRCADIAN CYCLE</span>
          <span>LOW-POWER BLE SENSORS</span>
        </div>
      </div>

      <!-- 5. Exploded Sub-Assembly 04: Dual Trapezoid Bento Physics & Leaderboard (ASM-04 · BENTO) -->
      <div id="module-bento" class="absolute z-20 draggable-node exploded-sub-module blueprint-card p-4 rounded-2xl cursor-pointer hover:border-indigo-500" style="left: 1990px; top: 1950px; width: 500px;" onclick="inspectComponent('bento')">
        <div class="flex items-center justify-between border-b border-slate-200 pb-2 mb-2.5 node-drag-handle">
          <div class="flex items-center gap-2">
            <span class="w-6 h-6 rounded-lg bg-indigo-50 border border-indigo-200 flex items-center justify-center text-xs">📐</span>
            <div>
              <h4 class="text-xs font-black text-slate-900">双梯形 Bento 几何裁切与动力学矩阵</h4>
              <span class="text-[8.5px] font-mono text-indigo-600 font-bold">[ASM-04 · DUAL TRAPEZOID SHADER & PHYSICS MATRIX]</span>
            </div>
          </div>
          <span class="text-[8.5px] font-mono px-2 py-0.5 rounded-full bg-indigo-50 text-indigo-700 font-bold">DISSECTED</span>
        </div>

        <!-- Correct Scale Bento Preview with True Podium Size -->
        <div class="relative h-18 bg-slate-900/5 rounded-xl p-2 flex items-center justify-around border border-slate-200 mb-2">
          <div class="flex items-center gap-2">
            <div class="w-7 h-7 rounded-lg bg-amber-50 border border-amber-200 flex items-center justify-center p-0.5">
              <img src="./assets/app_assets/ui_icons/ic_btn_trophy.png" class="no-crop-img" alt="奖杯">
            </div>
            <div class="text-left">
              <div class="text-[9.5px] font-black text-slate-800 font-mono break-words leading-tight">实时爱猫守护榜单</div>
              <div class="text-[7.5px] text-slate-400 font-mono mt-0.5">10.3° 倾角矢量切角</div>
            </div>
          </div>
          <div class="h-6 w-px bg-slate-300"></div>
          <!-- Tiny 3D Podium at REALISTIC small scale -->
          <div class="flex items-center gap-1.5">
            <div class="w-12 h-6 flex items-center justify-center">
              <img src="./assets/app_assets/generated/podium_3d.png" class="no-crop-img drop-shadow-2xs" alt="领奖台">
            </div>
            <div class="text-left">
              <div class="text-[9.5px] font-black text-slate-800 font-mono break-words leading-tight">微型 3D 奖励台</div>
              <div class="text-[7.5px] text-slate-400 font-mono mt-0.5">真实 UI 配件比例</div>
            </div>
          </div>
        </div>
        <div class="text-[8.5px] font-mono text-slate-500 bg-slate-100/80 p-1.5 rounded-lg flex items-center justify-between">
          <span>CLIP-PATH: TILT 10.3°</span>
          <span>TOLERANCE: 14.0px</span>
        </div>
      </div>

      <!-- ===================================================================== -->
      <!-- ZONE WEST (西部总成 · X: 80, Y: 980) · 100% 完整披露工程物料清单 (BOM)    -->
      <!-- ===================================================================== -->
      <div id="zone-bom" class="absolute z-20 draggable-node blueprint-card p-5 rounded-2xl" style="left: 80px; top: 980px; width: 1250px;">
        <div class="flex items-center justify-between border-b border-slate-200 pb-3 mb-3.5 node-drag-handle">
          <div class="flex items-center gap-2.5">
            <span class="w-8 h-8 rounded-xl bg-indigo-50 border border-indigo-200 flex items-center justify-center text-base">📦</span>
            <div>
              <h2 class="text-sm font-black text-slate-900 tracking-tight">工程物料清单与数字资产规格墙 (文字完整无省略 · 零裁剪)</h2>
              <span class="text-[9px] font-mono text-indigo-600 font-bold">[ZONE-WEST · 100% DISCLOSED BILL OF MATERIALS]</span>
            </div>
          </div>
          <span class="text-[9px] px-2 py-0.5 rounded-full bg-indigo-50 text-indigo-700 font-mono font-bold border border-indigo-200">TOTAL: 42 ASSETS</span>
        </div>

        <!-- Sub-cluster 1: 11 3D Cat Care Props with Cleanroom Optical Pads -->
        <div class="mb-4">
          <div class="flex items-center justify-between mb-2">
            <span class="text-[10px] font-black text-slate-700 font-mono flex items-center gap-1 uppercase">
              <span class="w-1.5 h-1.5 rounded-full bg-indigo-500"></span>
              <span>SUB-CLUSTER 1 · 11 大 3D 照护事件道具部件 (/assets/app_assets/ic_board_*.png)</span>
            </span>
            <span class="text-[9px] font-mono text-slate-400">3D ALPHA CUTOUTS</span>
          </div>
          <div id="unified-bom-items" class="grid grid-cols-4 gap-2.5">
            <!-- Rendered via JS with FULL titles and text wrapping -->
          </div>
        </div>

        <!-- Sub-cluster 2: UI Icons & Interaction Controls -->
        <div class="mb-4">
          <div class="flex items-center justify-between mb-2">
            <span class="text-[10px] font-black text-slate-700 font-mono flex items-center gap-1 uppercase">
              <span class="w-1.5 h-1.5 rounded-full bg-rose-500"></span>
              <span>SUB-CLUSTER 2 · HUD 状态指标仪表与按键套件 (全色温阶段 · 零剪裁)</span>
            </span>
            <span class="text-[9px] font-mono text-slate-400">12 UI CONTROLS</span>
          </div>
          <div id="unified-bom-icons" class="grid grid-cols-4 gap-2.5">
            <!-- Rendered via JS with FULL text -->
          </div>
        </div>

        <!-- Sub-cluster 2.5: 4 Vital Health Status Badges & Hero Cat Character Cutouts -->
        <div class="mb-4">
          <div class="flex items-center justify-between mb-2">
            <span class="text-[10px] font-black text-slate-700 font-mono flex items-center gap-1 uppercase">
              <span class="w-1.5 h-1.5 rounded-full bg-emerald-500"></span>
              <span>SUB-CLUSTER 2.5 · 四大体征微章与老马立绘无损切图 (1:1 正方体征 · 零剪裁)</span>
            </span>
            <span class="text-[9px] font-mono text-slate-400">9 ASSETS</span>
          </div>
          <div class="grid grid-cols-5 gap-2.5">
            <div class="bg-slate-50 p-2 rounded-xl border border-slate-200 cursor-pointer hover:border-emerald-400 transition-all text-center" onclick="inspectImage('./assets/app_assets/generated/status_food.png', '体征微章 · 饱食度正常指数 (1254×1254 · 1:1)')">
              <div class="w-10 h-10 cleanroom-pad rounded-lg mx-auto mb-1 flex items-center justify-center p-0.5 border border-slate-200">
                <img src="./assets/app_assets/generated/status_food.png" class="no-crop-img" alt="饱食度">
              </div>
              <div class="text-[9.5px] font-bold text-slate-800 font-mono break-words leading-tight">饱食度正常指数</div>
              <div class="text-[8px] text-slate-400 font-mono mt-0.5">1254×1254 · 1:1</div>
            </div>
            <div class="bg-slate-50 p-2 rounded-xl border border-slate-200 cursor-pointer hover:border-emerald-400 transition-all text-center" onclick="inspectImage('./assets/app_assets/generated/status_water.png', '体征微章 · 饮水含水量达标 (1254×1254 · 1:1)')">
              <div class="w-10 h-10 cleanroom-pad rounded-lg mx-auto mb-1 flex items-center justify-center p-0.5 border border-slate-200">
                <img src="./assets/app_assets/generated/status_water.png" class="no-crop-img" alt="饮水">
              </div>
              <div class="text-[9.5px] font-bold text-slate-800 font-mono break-words leading-tight">饮水摄入达标指数</div>
              <div class="text-[8px] text-slate-400 font-mono mt-0.5">1254×1254 · 1:1</div>
            </div>
            <div class="bg-slate-50 p-2 rounded-xl border border-slate-200 cursor-pointer hover:border-emerald-400 transition-all text-center" onclick="inspectImage('./assets/app_assets/generated/status_litter.png', '体征微章 · 猫砂洁净排泄指标 (1254×1254 · 1:1)')">
              <div class="w-10 h-10 cleanroom-pad rounded-lg mx-auto mb-1 flex items-center justify-center p-0.5 border border-slate-200">
                <img src="./assets/app_assets/generated/status_litter.png" class="no-crop-img" alt="猫砂">
              </div>
              <div class="text-[9.5px] font-bold text-slate-800 font-mono break-words leading-tight">猫砂排泄洁净指标</div>
              <div class="text-[8px] text-slate-400 font-mono mt-0.5">1254×1254 · 1:1</div>
            </div>
            <div class="bg-slate-50 p-2 rounded-xl border border-slate-200 cursor-pointer hover:border-emerald-400 transition-all text-center" onclick="inspectImage('./assets/app_assets/generated/status_bath.png', '体征微章 · 毛发清洁洗护指数 (1254×1254 · 1:1)')">
              <div class="w-10 h-10 cleanroom-pad rounded-lg mx-auto mb-1 flex items-center justify-center p-0.5 border border-slate-200">
                <img src="./assets/app_assets/generated/status_bath.png" class="no-crop-img" alt="洗护">
              </div>
              <div class="text-[9.5px] font-bold text-slate-800 font-mono break-words leading-tight">毛发洗护清洁指数</div>
              <div class="text-[8px] text-slate-400 font-mono mt-0.5">1254×1254 · 1:1</div>
            </div>
            <div class="bg-slate-50 p-2 rounded-xl border border-slate-200 cursor-pointer hover:border-indigo-400 transition-all text-center" onclick="inspectImage('./assets/app_assets/hero_cat_sitting_tight.png', '立绘切图 · 老马紧凑正坐形态 (841×1112 · 0.756)')">
              <div class="w-10 h-10 cleanroom-pad rounded-lg mx-auto mb-1 flex items-center justify-center p-0.5 border border-slate-200">
                <img src="./assets/app_assets/hero_cat_sitting_tight.png" class="no-crop-img" alt="正坐立绘">
              </div>
              <div class="text-[9.5px] font-bold text-slate-800 font-mono break-words leading-tight">老马紧凑正坐立绘</div>
              <div class="text-[8px] text-slate-400 font-mono mt-0.5">841×1112 (0.756)</div>
            </div>
            <div class="bg-slate-50 p-2 rounded-xl border border-slate-200 cursor-pointer hover:border-indigo-400 transition-all text-center" onclick="inspectImage('./assets/app_assets/hero_cat_carrier_tight.png', '立绘切图 · 老马外出猫包形态 (1018×1112 · 0.916)')">
              <div class="w-10 h-10 cleanroom-pad rounded-lg mx-auto mb-1 flex items-center justify-center p-0.5 border border-slate-200">
                <img src="./assets/app_assets/hero_cat_carrier_tight.png" class="no-crop-img" alt="猫包立绘">
              </div>
              <div class="text-[9.5px] font-bold text-slate-800 font-mono break-words leading-tight">外出猫包安全形态</div>
              <div class="text-[8px] text-slate-400 font-mono mt-0.5">1018×1112 (0.916)</div>
            </div>
            <div class="bg-slate-50 p-2 rounded-xl border border-slate-200 cursor-pointer hover:border-blue-400 transition-all text-center" onclick="inspectImage('./assets/candidates/app_icon_preview.png', '品牌应用图标 · 660×660 原生矢量渲染 (1:1)')">
              <div class="w-10 h-10 cleanroom-pad rounded-lg mx-auto mb-1 flex items-center justify-center p-0.5 border border-slate-200">
                <img src="./assets/candidates/app_icon_preview.png" class="no-crop-img" alt="应用图标">
              </div>
              <div class="text-[9.5px] font-bold text-slate-800 font-mono break-words leading-tight">品牌应用主图标</div>
              <div class="text-[8px] text-slate-400 font-mono mt-0.5">660×660 · 1:1</div>
            </div>
            <div class="bg-slate-50 p-2 rounded-xl border border-slate-200 cursor-pointer hover:border-blue-400 transition-all text-center" onclick="inspectImage('./assets/candidates/app_icon_preview_orig.png', '品牌应用图标原始母版 · 660×660 原生画幅 (1:1)')">
              <div class="w-10 h-10 cleanroom-pad rounded-lg mx-auto mb-1 flex items-center justify-center p-0.5 border border-slate-200">
                <img src="./assets/candidates/app_icon_preview_orig.png" class="no-crop-img" alt="应用图标母版">
              </div>
              <div class="text-[9.5px] font-bold text-slate-800 font-mono break-words leading-tight">应用图标原始母版</div>
              <div class="text-[8px] text-slate-400 font-mono mt-0.5">660×660 · 1:1</div>
            </div>
            <div class="bg-slate-50 p-2 rounded-xl border border-slate-200 cursor-pointer hover:border-cyan-400 transition-all text-center" onclick="inspectImage('./assets/app_assets/ic_board_feishu_badge.png', '系统配件 · 飞书多维协作角标道具 (224×212)')">
              <div class="w-10 h-10 cleanroom-pad rounded-lg mx-auto mb-1 flex items-center justify-center p-0.5 border border-slate-200">
                <img src="./assets/app_assets/ic_board_feishu_badge.png" class="no-crop-img" alt="飞书角标">
              </div>
              <div class="text-[9.5px] font-bold text-slate-800 font-mono break-words leading-tight">飞书多维协作角标</div>
              <div class="text-[8px] text-slate-400 font-mono mt-0.5">224×212 配件</div>
            </div>
          </div>
        </div>

        <!-- Sub-cluster 3: Quick Launch System Tiles -->
        <div class="mb-4">
          <div class="flex items-center justify-between mb-2">
            <span class="text-[10px] font-black text-slate-700 font-mono flex items-center gap-1 uppercase">
              <span class="w-1.5 h-1.5 rounded-full bg-cyan-500"></span>
              <span>SUB-CLUSTER 3 · 系统级功能快捷磁贴组件 (/assets/app_assets/ic_tile_*.png)</span>
            </span>
            <span class="text-[9px] font-mono text-slate-400">4 SYSTEM TILES</span>
          </div>
          <div class="grid grid-cols-4 gap-2.5">
            <div class="bg-slate-50 p-2.5 rounded-xl border border-slate-200 cursor-pointer hover:border-cyan-400 transition-all flex items-center gap-2.5" onclick="inspectImage('./assets/app_assets/ic_tile_yoyo.png', '系统磁贴 · 荣耀YOYO智能体接入')">
              <div class="w-10 h-10 cleanroom-pad rounded-lg flex-shrink-0 flex items-center justify-center p-0.5 border border-slate-200 shadow-2xs">
                <img src="./assets/app_assets/ic_tile_yoyo.png" class="no-crop-img" alt="YOYO">
              </div>
              <div class="text-left">
                <div class="text-[10px] font-black text-slate-800 font-mono break-words leading-tight">YOYO 专属接入磁贴</div>
                <div class="text-[8px] text-cyan-600 font-mono mt-0.5">ic_tile_yoyo.png</div>
              </div>
            </div>
            <div class="bg-slate-50 p-2.5 rounded-xl border border-slate-200 cursor-pointer hover:border-cyan-400 transition-all flex items-center gap-2.5" onclick="inspectImage('./assets/app_assets/ic_tile_feishu.png', '系统磁贴 · 飞书多维表格与办公协同')">
              <div class="w-10 h-10 cleanroom-pad rounded-lg flex-shrink-0 flex items-center justify-center p-0.5 border border-slate-200 shadow-2xs">
                <img src="./assets/app_assets/ic_tile_feishu.png" class="no-crop-img" alt="飞书">
              </div>
              <div class="text-left">
                <div class="text-[10px] font-black text-slate-800 font-mono break-words leading-tight">飞书多维协作磁贴</div>
                <div class="text-[8px] text-cyan-600 font-mono mt-0.5">ic_tile_feishu.png</div>
              </div>
            </div>
            <div class="bg-slate-50 p-2.5 rounded-xl border border-slate-200 cursor-pointer hover:border-cyan-400 transition-all flex items-center gap-2.5" onclick="inspectImage('./assets/app_assets/ic_tile_health.png', '系统磁贴 · 荣耀健康生理数据通道')">
              <div class="w-10 h-10 cleanroom-pad rounded-lg flex-shrink-0 flex items-center justify-center p-0.5 border border-slate-200 shadow-2xs">
                <img src="./assets/app_assets/ic_tile_health.png" class="no-crop-img" alt="健康">
              </div>
              <div class="text-left">
                <div class="text-[10px] font-black text-slate-800 font-mono break-words leading-tight">荣耀健康生理磁贴</div>
                <div class="text-[8px] text-cyan-600 font-mono mt-0.5">ic_tile_health.png</div>
              </div>
            </div>
            <div class="bg-slate-50 p-2.5 rounded-xl border border-slate-200 cursor-pointer hover:border-cyan-400 transition-all flex items-center gap-2.5" onclick="inspectImage('./assets/app_assets/ic_tile_journal.png', '系统磁贴 · 喵务日常手账入口')">
              <div class="w-10 h-10 cleanroom-pad rounded-lg flex-shrink-0 flex items-center justify-center p-0.5 border border-slate-200 shadow-2xs">
                <img src="./assets/app_assets/ic_tile_journal.png" class="no-crop-img" alt="手账">
              </div>
              <div class="text-left">
                <div class="text-[10px] font-black text-slate-800 font-mono break-words leading-tight">喵务日常手账入口</div>
                <div class="text-[8px] text-cyan-600 font-mono mt-0.5">ic_tile_journal.png</div>
              </div>
            </div>
          </div>
        </div>

        <!-- Sub-cluster 4: 7 Archive Cards -->
        <div>
          <div class="flex items-center justify-between mb-2">
            <span class="text-[10px] font-black text-slate-700 font-mono flex items-center gap-1 uppercase">
              <span class="w-1.5 h-1.5 rounded-full bg-emerald-500"></span>
              <span>SUB-CLUSTER 4 · 结构化持久存储卡片 163-169 全量物料 (保留自然比例 · 零裁剪)</span>
            </span>
            <span class="text-[9px] font-mono text-slate-400">7 ARCHIVE RECORDS</span>
          </div>
          <div id="unified-bom-archives" class="grid grid-cols-7 gap-2.5">
            <!-- Rendered via JS with FULL titles -->
          </div>
        </div>
      </div>

      <!-- ===================================================================== -->
      <!-- ZONE EAST (东部总成 · X: 3150, Y: 980) · 8 大端侧真机全工况全分辨率验证流   -->
      <!-- ===================================================================== -->
      <div id="zone-screens" class="absolute z-20 draggable-node blueprint-card p-5 rounded-2xl" style="left: 3150px; top: 980px; width: 1550px;">
        <div class="flex items-center justify-between border-b border-slate-200 pb-3 mb-3.5 node-drag-handle">
          <div class="flex items-center gap-2.5">
            <span class="w-8 h-8 rounded-xl bg-blue-50 border border-blue-200 flex items-center justify-center text-base">📱</span>
            <div>
              <h2 class="text-sm font-black text-slate-900 tracking-tight">8 大端侧真机全工况全分辨率实测大屏 (文字完整清晰 · 1320 × 2868 · 零剪裁)</h2>
              <span class="text-[9px] font-mono text-blue-600 font-bold">[ZONE-EAST · 8 HARDWARE VERIFICATION CAPTURES · 1320 × 2868]</span>
            </div>
          </div>
          <span class="text-[9px] px-2 py-0.5 rounded-full bg-blue-50 text-blue-700 font-mono font-bold border border-blue-200">19.5:9 NATIVE TELEMETRY</span>
        </div>

        <div class="grid grid-cols-4 gap-4">
          <!-- 8 Native Screen Cards using real Screenshot_20260919_*.JPG in 19.5:9 Aspect Ratio -->
          <div class="bg-slate-50 p-2.5 rounded-xl border border-slate-200 cursor-pointer hover:border-blue-400 transition-all" onclick="inspectImage('./assets/screenshots/Screenshot_20260919_174540_com_lyi_laomayoyo_MainActivity.JPG', '真机工况 01 · 居室常态静止巡航 (1320×2868)')">
            <div class="w-full aspect-phone bg-slate-900 rounded-lg overflow-hidden mb-1.5 flex items-center justify-center shadow-inner">
              <img src="./assets/screenshots/Screenshot_20260919_174540_com_lyi_laomayoyo_MainActivity.JPG" class="no-crop-img" alt="工况1">
            </div>
            <div class="text-[10px] font-black text-slate-800 font-mono break-words leading-tight">工况 01 · 居室常态静止巡航</div>
            <div class="text-[8px] text-slate-400 font-mono mt-0.5">1320×2868 · 17:45:40 实测采集</div>
          </div>

          <div class="bg-slate-50 p-2.5 rounded-xl border border-slate-200 cursor-pointer hover:border-blue-400 transition-all" onclick="inspectImage('./assets/screenshots/Screenshot_20260919_174600_com_lyi_laomayoyo_MainActivity.JPG', '真机工况 02 · 屏幕触碰响应反馈 (1320×2868)')">
            <div class="w-full aspect-phone bg-slate-900 rounded-lg overflow-hidden mb-1.5 flex items-center justify-center shadow-inner">
              <img src="./assets/screenshots/Screenshot_20260919_174600_com_lyi_laomayoyo_MainActivity.JPG" class="no-crop-img" alt="工况2">
            </div>
            <div class="text-[10px] font-black text-slate-800 font-mono break-words leading-tight">工况 02 · 屏幕触碰响应反馈</div>
            <div class="text-[8px] text-slate-400 font-mono mt-0.5">1320×2868 · 17:46:00 实测采集</div>
          </div>

          <div class="bg-slate-50 p-2.5 rounded-xl border border-slate-200 cursor-pointer hover:border-blue-400 transition-all" onclick="inspectImage('./assets/screenshots/Screenshot_20260919_174613_com_lyi_laomayoyo_MainActivity.JPG', '真机工况 03 · 脏污状态视觉告警 (1320×2868)')">
            <div class="w-full aspect-phone bg-slate-900 rounded-lg overflow-hidden mb-1.5 flex items-center justify-center shadow-inner">
              <img src="./assets/screenshots/Screenshot_20260919_174613_com_lyi_laomayoyo_MainActivity.JPG" class="no-crop-img" alt="工况3">
            </div>
            <div class="text-[10px] font-black text-slate-800 font-mono break-words leading-tight">工况 03 · 脏污状态视觉告警</div>
            <div class="text-[8px] text-slate-400 font-mono mt-0.5">1320×2868 · 17:46:13 实测采集</div>
          </div>

          <div class="bg-slate-50 p-2.5 rounded-xl border border-slate-200 cursor-pointer hover:border-blue-400 transition-all" onclick="inspectImage('./assets/screenshots/Screenshot_20260919_174628_com_lyi_laomayoyo_MainActivity.JPG', '真机工况 04 · 抚摸清洁自愈过程 (1320×2868)')">
            <div class="w-full aspect-phone bg-slate-900 rounded-lg overflow-hidden mb-1.5 flex items-center justify-center shadow-inner">
              <img src="./assets/screenshots/Screenshot_20260919_174628_com_lyi_laomayoyo_MainActivity.JPG" class="no-crop-img" alt="工况4">
            </div>
            <div class="text-[10px] font-black text-slate-800 font-mono break-words leading-tight">工况 04 · 抚摸清洁自愈过程</div>
            <div class="text-[8px] text-slate-400 font-mono mt-0.5">1320×2868 · 17:46:28 实测采集</div>
          </div>

          <div class="bg-slate-50 p-2.5 rounded-xl border border-slate-200 cursor-pointer hover:border-blue-400 transition-all" onclick="inspectImage('./assets/screenshots/Screenshot_20260919_174648_com_lyi_laomayoyo_MainActivity.JPG', '真机工况 05 · 定额食物投喂事件 (1320×2868)')">
            <div class="w-full aspect-phone bg-slate-900 rounded-lg overflow-hidden mb-1.5 flex items-center justify-center shadow-inner">
              <img src="./assets/screenshots/Screenshot_20260919_174648_com_lyi_laomayoyo_MainActivity.JPG" class="no-crop-img" alt="工况5">
            </div>
            <div class="text-[10px] font-black text-slate-800 font-mono break-words leading-tight">工况 05 · 定额食物投喂事件</div>
            <div class="text-[8px] text-slate-400 font-mono mt-0.5">1320×2868 · 17:46:48 实测采集</div>
          </div>

          <div class="bg-slate-50 p-2.5 rounded-xl border border-slate-200 cursor-pointer hover:border-blue-400 transition-all" onclick="inspectImage('./assets/screenshots/Screenshot_20260919_174700_com_lyi_laomayoyo_MainActivity.JPG', '真机工况 06 · 逗猫棒动力学捕捉 (1320×2868)')">
            <div class="w-full aspect-phone bg-slate-900 rounded-lg overflow-hidden mb-1.5 flex items-center justify-center shadow-inner">
              <img src="./assets/screenshots/Screenshot_20260919_174700_com_lyi_laomayoyo_MainActivity.JPG" class="no-crop-img" alt="工况6">
            </div>
            <div class="text-[10px] font-black text-slate-800 font-mono break-words leading-tight">工况 06 · 逗猫棒动力学捕捉</div>
            <div class="text-[8px] text-slate-400 font-mono mt-0.5">1320×2868 · 17:47:00 实测采集</div>
          </div>

          <div class="bg-slate-50 p-2.5 rounded-xl border border-slate-200 cursor-pointer hover:border-blue-400 transition-all" onclick="inspectImage('./assets/screenshots/Screenshot_20260919_174713_com_lyi_laomayoyo_MainActivity.JPG', '真机工况 07 · 听诊心率健康体检 (1320×2868)')">
            <div class="w-full aspect-phone bg-slate-900 rounded-lg overflow-hidden mb-1.5 flex items-center justify-center shadow-inner">
              <img src="./assets/screenshots/Screenshot_20260919_174713_com_lyi_laomayoyo_MainActivity.JPG" class="no-crop-img" alt="工况7">
            </div>
            <div class="text-[10px] font-black text-slate-800 font-mono break-words leading-tight">工况 07 · 听诊心率健康体检</div>
            <div class="text-[8px] text-slate-400 font-mono mt-0.5">1320×2868 · 17:47:13 实测采集</div>
          </div>

          <div class="bg-slate-50 p-2.5 rounded-xl border border-slate-200 cursor-pointer hover:border-blue-400 transition-all" onclick="inspectImage('./assets/screenshots/Screenshot_20260919_174724_com_lyi_laomayoyo_MainActivity.JPG', '真机工况 08 · 静音恒温安睡模式 (1320×2868)')">
            <div class="w-full aspect-phone bg-slate-900 rounded-lg overflow-hidden mb-1.5 flex items-center justify-center shadow-inner">
              <img src="./assets/screenshots/Screenshot_20260919_174724_com_lyi_laomayoyo_MainActivity.JPG" class="no-crop-img" alt="工况8">
            </div>
            <div class="text-[10px] font-black text-slate-800 font-mono break-words leading-tight">工况 08 · 静音恒温安睡模式</div>
            <div class="text-[8px] text-slate-400 font-mono mt-0.5">1320×2868 · 17:47:24 实测采集</div>
          </div>
        </div>
      </div>

      <!-- ===================================================================== -->
      <!-- ZONE SOUTHWEST (西南总成 · X: 80, Y: 2200) · 16:9 宽屏动态工况站 (放大且自动播放) -->
      <!-- ===================================================================== -->
      <div id="zone-posters" class="absolute z-20 draggable-node blueprint-card p-6 rounded-2xl" style="left: 80px; top: 2200px; width: 1450px;">
        <div class="flex items-center justify-between border-b border-slate-200 pb-3 mb-4 node-drag-handle">
          <div class="flex items-center gap-2.5">
            <span class="w-8 h-8 rounded-xl bg-indigo-50 border border-indigo-200 flex items-center justify-center text-base">🎞️</span>
            <div>
              <h3 class="font-black text-slate-900 text-xs">16:9 动态工况时空观测站 (大画幅宽屏显示 · 60FPS 自动循环播放 · 无需手动点击)</h3>
              <span class="text-[9px] font-mono text-indigo-700 font-bold">[VID-POSTERS · 16:9 TEMPORAL MOTION CAPTURE · AUTOPLAY ENABLED]</span>
            </div>
          </div>
          <span class="text-[9px] px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-700 font-mono font-bold border border-emerald-200">● 6 STREAMS AUTOPLAYING</span>
        </div>

        <!-- 6 Prominent Widescreen Monitors (2 rows x 3 columns · Large format) -->
        <div class="grid grid-cols-3 gap-4">
          <div class="bg-slate-950 rounded-2xl p-2.5 border border-slate-800 shadow-md">
            <div class="w-full aspect-cine-16-9 bg-black rounded-xl overflow-hidden mb-2 relative flex items-center justify-center">
              <video src="./assets/app_assets/archives/videos/vid_cat_controlled.mp4" poster="./assets/video_posters/vid_cat_controlled_poster.jpg" autoplay loop muted playsinline class="w-full h-full object-contain"></video>
              <span class="absolute top-1.5 left-1.5 px-2 py-0.5 rounded bg-blue-600/90 text-[8px] text-white font-mono font-bold">STREAM 01 · 60FPS</span>
            </div>
            <div class="text-[11px] font-black text-slate-100 font-mono break-words leading-tight">01 · 机械精准受控与环境巡航工况</div>
            <div class="text-[9px] text-slate-400 font-mono mt-1 flex items-center justify-between">
              <span>1280×720 · 16:9 MP4</span>
              <span class="text-emerald-400">● 实时播放中</span>
            </div>
          </div>

          <div class="bg-slate-950 rounded-2xl p-2.5 border border-slate-800 shadow-md">
            <div class="w-full aspect-cine-16-9 bg-black rounded-xl overflow-hidden mb-2 relative flex items-center justify-center">
              <video src="./assets/app_assets/archives/videos/vid_cat_feast.mp4" poster="./assets/video_posters/vid_cat_feast_poster.jpg" autoplay loop muted playsinline class="w-full h-full object-contain"></video>
              <span class="absolute top-1.5 left-1.5 px-2 py-0.5 rounded bg-blue-600/90 text-[8px] text-white font-mono font-bold">STREAM 02 · 60FPS</span>
            </div>
            <div class="text-[11px] font-black text-slate-100 font-mono break-words leading-tight">02 · 享用全价鲜肉盛宴投喂工况</div>
            <div class="text-[9px] text-slate-400 font-mono mt-1 flex items-center justify-between">
              <span>1280×720 · 16:9 MP4</span>
              <span class="text-emerald-400">● 实时播放中</span>
            </div>
          </div>

          <div class="bg-slate-950 rounded-2xl p-2.5 border border-slate-800 shadow-md">
            <div class="w-full aspect-cine-16-9 bg-black rounded-xl overflow-hidden mb-2 relative flex items-center justify-center">
              <video src="./assets/app_assets/archives/videos/vid_cat_taste_after.mp4" poster="./assets/video_posters/vid_cat_taste_after_poster.jpg" autoplay loop muted playsinline class="w-full h-full object-contain"></video>
              <span class="absolute top-1.5 left-1.5 px-2 py-0.5 rounded bg-blue-600/90 text-[8px] text-white font-mono font-bold">STREAM 03 · 60FPS</span>
            </div>
            <div class="text-[11px] font-black text-slate-100 font-mono break-words leading-tight">03 · 餐后舌面毛发深度清洁回味工况</div>
            <div class="text-[9px] text-slate-400 font-mono mt-1 flex items-center justify-between">
              <span>1280×720 · 16:9 MP4</span>
              <span class="text-emerald-400">● 实时播放中</span>
            </div>
          </div>

          <div class="bg-slate-950 rounded-2xl p-2.5 border border-slate-800 shadow-md">
            <div class="w-full aspect-cine-16-9 bg-black rounded-xl overflow-hidden mb-2 relative flex items-center justify-center">
              <video src="./assets/app_assets/archives/videos/vid_cat_charming_belly.mp4" poster="./assets/video_posters/vid_cat_charming_belly_poster.jpg" autoplay loop muted playsinline class="w-full h-full object-contain"></video>
              <span class="absolute top-1.5 left-1.5 px-2 py-0.5 rounded bg-blue-600/90 text-[8px] text-white font-mono font-bold">STREAM 04 · 60FPS</span>
            </div>
            <div class="text-[11px] font-black text-slate-100 font-mono break-words leading-tight">04 · 仰卧露腹高信任度亲密互动工况</div>
            <div class="text-[9px] text-slate-400 font-mono mt-1 flex items-center justify-between">
              <span>1280×720 · 16:9 MP4</span>
              <span class="text-emerald-400">● 实时播放中</span>
            </div>
          </div>

          <div class="bg-slate-950 rounded-2xl p-2.5 border border-slate-800 shadow-md">
            <div class="w-full aspect-cine-16-9 bg-black rounded-xl overflow-hidden mb-2 relative flex items-center justify-center">
              <video src="./assets/app_assets/archives/videos/vid_cat_fire_extinguisher.mp4" poster="./assets/video_posters/vid_cat_fire_extinguisher_poster.jpg" autoplay loop muted playsinline class="w-full h-full object-contain"></video>
              <span class="absolute top-1.5 left-1.5 px-2 py-0.5 rounded bg-blue-600/90 text-[8px] text-white font-mono font-bold">STREAM 05 · 60FPS</span>
            </div>
            <div class="text-[11px] font-black text-slate-100 font-mono break-words leading-tight">05 · 室内灭火器材物理探索避障工况</div>
            <div class="text-[9px] text-slate-400 font-mono mt-1 flex items-center justify-between">
              <span>1280×720 · 16:9 MP4</span>
              <span class="text-emerald-400">● 实时播放中</span>
            </div>
          </div>

          <div class="bg-slate-950 rounded-2xl p-2.5 border border-slate-800 shadow-md">
            <div class="w-full aspect-cine-16-9 bg-black rounded-xl overflow-hidden mb-2 relative flex items-center justify-center">
              <video src="./assets/app_assets/archives/videos/vid_cat_attack_slacker.mp4" poster="./assets/video_posters/vid_cat_attack_slacker_poster.jpg" autoplay loop muted playsinline class="w-full h-full object-contain"></video>
              <span class="absolute top-1.5 left-1.5 px-2 py-0.5 rounded bg-blue-600/90 text-[8px] text-white font-mono font-bold">STREAM 06 · 60FPS</span>
            </div>
            <div class="text-[11px] font-black text-slate-100 font-mono break-words leading-tight">06 · 突击警觉与工作摸鱼反射捕捉工况</div>
            <div class="text-[9px] text-slate-400 font-mono mt-1 flex items-center justify-between">
              <span>1280×720 · 16:9 MP4</span>
              <span class="text-emerald-400">● 实时播放中</span>
            </div>
          </div>
        </div>
      </div>

      <!-- ===================================================================== -->
      <!-- ZONE SOUTHEAST (东南总成 · X: 3150, Y: 2200) · 材质 Shader 与光照微纹理实验台 -->
      <!-- ===================================================================== -->
      <div id="zone-shaders" class="absolute z-20 draggable-node blueprint-card p-5 rounded-2xl" style="left: 3150px; top: 2200px; width: 1550px;">
        <div class="flex items-center justify-between border-b border-slate-200 pb-3 mb-3.5 node-drag-handle">
          <div class="flex items-center gap-2.5">
            <span class="w-8 h-8 rounded-xl bg-rose-50 border border-rose-200 flex items-center justify-center text-base">🎨</span>
            <div>
              <h3 class="font-black text-slate-900 text-xs">材质 Shader 与光照微纹理实验台 (比例校准 · 文本完整 · 零剪裁)</h3>
              <span class="text-[9px] font-mono text-rose-700 font-bold">[SHADER-TEXTURES · MICRO-TEXTURES & SCENIC SHADER ASSETS]</span>
            </div>
          </div>
          <span class="text-[9px] px-2 py-0.5 rounded-full bg-rose-50 text-rose-700 font-mono font-bold border border-rose-200">8 SHADER ASSETS</span>
        </div>

        <div class="grid grid-cols-4 gap-3.5">
          <!-- 1. 3D Podium Panoramic Model (Calibrated Small Token Scale) -->
          <div class="bg-slate-50 p-2.5 rounded-xl border border-slate-200 cursor-pointer hover:border-rose-400 transition-all" onclick="inspectImage('./assets/app_assets/generated/podium_3d.png', 'Shader 贴图 01 · 3D 全景领奖台模型 (1375×548 · 2.5:1)')">
            <div class="w-full aspect-wide-2-5 bg-slate-900/5 rounded-lg overflow-hidden mb-1.5 flex items-center justify-center p-1">
              <img src="./assets/app_assets/generated/podium_3d.png" class="no-crop-img" alt="podium_3d">
            </div>
            <div class="text-[10px] font-bold text-slate-800 font-mono break-words leading-tight">3D 全景领奖台模型</div>
            <div class="text-[8px] text-slate-400 font-mono mt-0.5">1375×548 · 2.5:1 空间网格</div>
          </div>

          <!-- 2. Leaderboard Lighting & Shade Model -->
          <div class="bg-slate-50 p-2.5 rounded-xl border border-slate-200 cursor-pointer hover:border-rose-400 transition-all" onclick="inspectImage('./assets/app_assets/generated/podium_leaderboard.png', 'Shader 贴图 02 · 领奖台空间光影贴图 (1536×1024 · 1.5:1)')">
            <div class="w-full aspect-wide-1-5 bg-slate-900/5 rounded-lg overflow-hidden mb-1.5 flex items-center justify-center p-1">
              <img src="./assets/app_assets/generated/podium_leaderboard.png" class="no-crop-img" alt="podium_leaderboard">
            </div>
            <div class="text-[10px] font-bold text-slate-800 font-mono break-words leading-tight">领奖台空间光影着色图</div>
            <div class="text-[8px] text-slate-400 font-mono mt-0.5">1536×1024 · 1.5:1 漫反射</div>
          </div>

          <!-- 3. Wide Archive Shader Texture -->
          <div class="bg-slate-50 p-2.5 rounded-xl border border-slate-200 cursor-pointer hover:border-rose-400 transition-all" onclick="inspectImage('./assets/app_assets/generated/btn_archive_texture.png', 'Shader 贴图 03 · 档案手账材质着色器贴图 (1774×887 · 2.0:1)')">
            <div class="w-full aspect-wide-2-1 bg-slate-900/5 rounded-lg overflow-hidden mb-1.5 flex items-center justify-center">
              <img src="./assets/app_assets/generated/btn_archive_texture.png" class="no-crop-img" alt="btn_archive_texture">
            </div>
            <div class="text-[10px] font-bold text-slate-800 font-mono break-words leading-tight">双梯形手账按键纹理</div>
            <div class="text-[8px] text-slate-400 font-mono mt-0.5">1774×887 · 2.0:1 倾角着色</div>
          </div>

          <!-- 4. Wide Rank Shader Texture -->
          <div class="bg-slate-50 p-2.5 rounded-xl border border-slate-200 cursor-pointer hover:border-rose-400 transition-all" onclick="inspectImage('./assets/app_assets/generated/btn_rank_texture.png', 'Shader 贴图 04 · 排行榜材质着色器贴图 (1774×887 · 2.0:1)')">
            <div class="w-full aspect-wide-2-1 bg-slate-900/5 rounded-lg overflow-hidden mb-1.5 flex items-center justify-center">
              <img src="./assets/app_assets/generated/btn_rank_texture.png" class="no-crop-img" alt="btn_rank_texture">
            </div>
            <div class="text-[10px] font-bold text-slate-800 font-mono break-words leading-tight">双梯形排行榜按键纹理</div>
            <div class="text-[8px] text-slate-400 font-mono mt-0.5">1774×887 · 2.0:1 金属拉丝</div>
          </div>

          <!-- 5. Ceramic Texture -->
          <div class="bg-slate-50 p-2.5 rounded-xl border border-slate-200 cursor-pointer hover:border-rose-400 transition-all" onclick="inspectImage('./assets/app_assets/generated/btn_white_ceramic_texture.png', 'Shader 贴图 05 · 白色微晶陶瓷质感贴图 (1374×1145 · 1.2:1)')">
            <div class="w-full aspect-tex-1-2 bg-slate-900/5 rounded-lg overflow-hidden mb-1.5 flex items-center justify-center">
              <img src="./assets/app_assets/generated/btn_white_ceramic_texture.png" class="no-crop-img" alt="ceramic">
            </div>
            <div class="text-[10px] font-bold text-slate-800 font-mono break-words leading-tight">白色微晶陶瓷漫反射贴图</div>
            <div class="text-[8px] text-slate-400 font-mono mt-0.5">1374×1145 · 1.2:1 法线微凹凸</div>
          </div>

          <!-- 6. 3D Journal Icon Asset -->
          <div class="bg-slate-50 p-2.5 rounded-xl border border-slate-200 cursor-pointer hover:border-rose-400 transition-all" onclick="inspectImage('./assets/app_assets/generated/ic_archive_journal.png', 'Shader 贴图 06 · 3D 手账立体渲染贴图')">
            <div class="w-full aspect-square-1-1 bg-slate-900/5 rounded-lg overflow-hidden mb-1.5 flex items-center justify-center p-1">
              <img src="./assets/app_assets/generated/ic_archive_journal.png" class="no-crop-img" alt="journal">
            </div>
            <div class="text-[10px] font-bold text-slate-800 font-mono break-words leading-tight">3D 手账立体图标贴图</div>
            <div class="text-[8px] text-slate-400 font-mono mt-0.5">手账三维渲染投影通道</div>
          </div>

          <!-- 7. Archive Art Shader Texture -->
          <div class="bg-slate-50 p-2.5 rounded-xl border border-slate-200 cursor-pointer hover:border-rose-400 transition-all" onclick="inspectImage('./assets/app_assets/generated/btn_archive_art.png', 'Shader 贴图 07 · 手账艺术光影着色图 (1536×1024 · 1.5:1)')">
            <div class="w-full aspect-wide-1-5 bg-slate-900/5 rounded-lg overflow-hidden mb-1.5 flex items-center justify-center">
              <img src="./assets/app_assets/generated/btn_archive_art.png" class="no-crop-img" alt="btn_archive_art">
            </div>
            <div class="text-[10px] font-bold text-slate-800 font-mono break-words leading-tight">手账艺术光影着色图</div>
            <div class="text-[8px] text-slate-400 font-mono mt-0.5">1536×1024 · 1.5:1 渐变贴图</div>
          </div>

          <!-- 8. Rank Art Shader Texture -->
          <div class="bg-slate-50 p-2.5 rounded-xl border border-slate-200 cursor-pointer hover:border-rose-400 transition-all" onclick="inspectImage('./assets/app_assets/generated/btn_rank_art.png', 'Shader 贴图 08 · 排行榜艺术高光着色图 (1536×1024 · 1.5:1)')">
            <div class="w-full aspect-wide-1-5 bg-slate-900/5 rounded-lg overflow-hidden mb-1.5 flex items-center justify-center">
              <img src="./assets/app_assets/generated/btn_rank_art.png" class="no-crop-img" alt="btn_rank_art">
            </div>
            <div class="text-[10px] font-bold text-slate-800 font-mono break-words leading-tight">排行榜高光艺术着色图</div>
            <div class="text-[8px] text-slate-400 font-mono mt-0.5">1536×1024 · 1.5:1 高光贴图</div>
          </div>
        </div>
      </div>

      <!-- ===================================================================== -->
      <!-- ZONE SOUTH (南部总成 · X: 1600, Y: 2450) · 15 位工程贡献者矩阵 (完整文字自适应) -->
      <!-- ===================================================================== -->
      <div id="zone-team" class="absolute z-20 draggable-node blueprint-card p-6 rounded-2xl" style="left: 1600px; top: 2450px; width: 1450px;">
        <div class="flex items-center justify-between border-b border-slate-200 pb-3 mb-4 node-drag-handle">
          <div class="flex items-center gap-2.5">
            <span class="w-8 h-8 rounded-xl bg-blue-50 border border-blue-200 flex items-center justify-center text-base">👥</span>
            <div>
              <h2 class="text-sm font-black text-slate-900 tracking-tight">工程核心贡献者与系统总线责任人架构图 (1:1 正方原生画幅 · 文字完整无省略)</h2>
              <span class="text-[9px] font-mono text-blue-600 font-bold">[ZONE-SOUTH · 15 REAL CONTRIBUTORS · FULL RESPONSIBILITY DESCRIPTIONS]</span>
            </div>
          </div>
          <div class="flex items-center gap-2">
            <span class="text-[8.5px] font-mono text-slate-400">ENGINEERING PERSONNEL</span>
            <span class="text-[8.5px] px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-700 font-mono font-bold border border-emerald-200">15 MODULE OWNERS</span>
          </div>
        </div>

        <!-- Aligned Grid of 15 Contributors with FULL descriptions and titles -->
        <div id="unified-team-grid" class="grid grid-cols-3 gap-3.5">
          <!-- Rendered via JS -->
        </div>
      </div>

    </div>
  </main>

  <!-- ========================================================================= -->
  <!-- SIDE INSPECTOR DRAWER (高密度技术物料探针抽屉)                              -->
  <!-- ========================================================================= -->
  <aside id="inspector-drawer" class="fixed top-14 right-0 bottom-0 w-[440px] bg-white/95 backdrop-blur-2xl border-l border-slate-200 shadow-2xl z-50 p-5 flex flex-col justify-between transform translate-x-[440px] transition-transform duration-300 ease-out">
    <div>
      <div class="flex items-center justify-between border-b border-slate-200 pb-3 mb-4">
        <div>
          <span id="insp-tag" class="text-[9px] font-mono font-bold px-2 py-0.5 rounded-full bg-blue-50 text-blue-700 border border-blue-200">[TELEMETRY PROBE]</span>
          <h3 id="insp-title" class="text-sm font-black text-slate-900 mt-0.5">部件工程探针与参数</h3>
        </div>
        <button onclick="closeInspector()" class="w-7 h-7 rounded-full bg-slate-100 hover:bg-slate-200 flex items-center justify-center font-bold text-slate-500">×</button>
      </div>

      <!-- Large Preview Box (Strictly Zero Crop with Cleanroom Pad) -->
      <div class="w-full h-56 cleanroom-pad rounded-xl overflow-hidden border border-slate-200 mb-4 flex items-center justify-center p-2.5 relative">
        <img id="insp-img" src="" class="no-crop-img" alt="检视预览">
        <div class="absolute bottom-2 right-2 bg-black/60 backdrop-blur-md px-1.5 py-0.5 rounded text-[8px] text-white font-mono">ZERO CROP · 100% NATIVE</div>
      </div>

      <!-- Technical Telemetry Data -->
      <div class="space-y-2.5 font-mono text-[11px]">
        <div class="flex justify-between border-b border-slate-100 pb-1.5">
          <span class="text-slate-400">组件标识 / NAME</span>
          <span id="insp-name" class="font-bold text-slate-800 break-words text-right max-w-[260px]">-</span>
        </div>
        <div class="flex justify-between border-b border-slate-100 pb-1.5">
          <span class="text-slate-400">物理路径 / PATH</span>
          <span id="insp-path" class="font-bold text-blue-600 break-all text-right max-w-[260px]">-</span>
        </div>
        <div class="flex justify-between border-b border-slate-100 pb-1.5">
          <span class="text-slate-400">画幅比 / RATIO</span>
          <span id="insp-ratio" class="font-bold text-slate-800">-</span>
        </div>
        <div class="flex justify-between border-b border-slate-100 pb-1.5">
          <span class="text-slate-400">模块责任人 / OWNER</span>
          <span id="insp-author" class="font-bold text-emerald-600">-</span>
        </div>
        <div class="pt-1">
          <span class="text-slate-400 block mb-1">工程功能与状态机说明:</span>
          <p id="insp-desc" class="text-slate-600 font-sans text-xs leading-relaxed bg-slate-50 p-2.5 rounded-lg border border-slate-200">-</p>
        </div>
      </div>
    </div>

    <div class="pt-3 border-t border-slate-200 flex items-center justify-between text-[10px] font-mono text-slate-400">
      <span>HONOR YOYO INSPECTOR v3.0</span>
      <button onclick="closeInspector()" class="px-3 py-1.5 rounded-lg bg-slate-900 text-white font-bold hover:bg-slate-800 transition-all font-sans text-xs">收起面板</button>
    </div>
  </aside>

  <!-- ========================================================================= -->
  <!-- JAVASCRIPT: PAN, ZOOM, FIGMA-LIKE DRAGGING & BULLETPROOF AUTOPLAY         -->
  <!-- ========================================================================= -->
  <script>
    // -------------------------------------------------------------------------
    // 1. Core Data Models (All 11 items and 15 contributors fully written)
    // -------------------------------------------------------------------------
    const SCHEDULE_DATA = [
      { id: 0, time: '07:30', title: '清晨体温与心率无感监测', person: '传鹏', icon: './assets/app_assets/ic_board_stethoscope.png', desc: 'BLE 智能项圈传感器心跳上报，采集静息心率与皮温，同步至荣耀健康总线。' },
      { id: 1, time: '08:15', title: '渴望全价鲜肉猫粮定量补给', person: '小六', icon: './assets/app_assets/ic_board_bowl.png', desc: '高精度重力传感器校验余粮，执行早间定额投喂事件，记录卡路里摄入曲线。' },
      { id: 2, time: '10:00', title: '多层剑麻猫爬架高空巡视', person: 'Adam', icon: './assets/app_assets/ic_board_cat_tree.png', desc: '室内 UWB 厘米级定位确认老马登顶，记录攀爬骨骼伸展与四肢运动量。' },
      { id: 3, time: '11:45', title: '羽毛逗猫棒互动敏捷度测试', person: '阿杰', icon: './assets/app_assets/ic_board_wand.png', desc: 'CV 视觉姿态捕捉系统记录跳跃腾空弧度与捕猎反射时间，写入活跃度模型。' },
      { id: 4, time: '13:30', title: '加厚软垫猫包户外安全转运', person: 'Howwoy', icon: './assets/app_assets/ic_board_crate.png', desc: '环境气压与温湿度传感校验，确保转运箱内部空气流通与声学降噪隔绝。' },
      { id: 5, time: '15:00', title: '活水循环过滤饮水机补水', person: '木子', icon: './assets/app_assets/ic_board_fountain.png', desc: 'TDS 水质传感器实时监测浊度与电导率，自动脉冲紫外除菌并推送补水日志。' },
      { id: 6, time: '16:45', title: '深层除浮毛气囊顺毛护理', person: 'LinYi', icon: './assets/app_assets/ic_board_brush.png', desc: '抗静电硅胶齿梳护理，清理脱落浮毛并按摩表皮微循环，舒缓紧张神经。' },
      { id: 7, time: '18:10', title: '天然冻干零食奖励正向强化', person: 'Bingo', icon: './assets/app_assets/ic_board_treat.png', desc: '声学指令响应判定，下发小红花荣誉积分并更新爱猫加权积分排行榜。' },
      { id: 8, time: '20:26', title: '膨润土猫砂深度清理', person: 'Adam', icon: './assets/app_assets/ic_board_litter_box.png', desc: '铲除今日结团，补充新鲜无尘矿砂至 8cm 刻度线，开启除臭杀菌喷雾循环。' },
      { id: 9, time: '21:44', title: '渴望全价鲜肉猫粮夜间投喂', person: '小六', icon: './assets/app_assets/ic_board_bowl.png', desc: '清洗陶瓷浅食碗，称量定额干粮投放，记录当日总进食量无异常并记录留档。' },
      { id: 10, time: '23:18', title: '静音恒温猫窝安睡准备', person: '方晟', icon: './assets/app_assets/ic_board_cat_bed.png', desc: '巡视门窗关闭，将走廊夜灯调至暖光睡眠模式，确认老马回到休息垫安静入睡。' }
    ];

    const TEAM_MEMBERS = [
      { name: '柯子杰', alias: '阿杰', role: '视觉工程总监', avatar: './assets/app_assets/avatars/avatar_ajie.png', desc: '全套 3D 物品图标建模、设计规范 Token 系统与高光 Shader 渲染管线。' },
      { name: '琮宇', alias: 'Howwoy', role: '原生交互系统', avatar: './assets/app_assets/avatars/avatar_congyu.png', desc: 'Android WebView 混合容器架设，手势触控与物理惯性回弹动力学引擎。' },
      { name: '方晟', alias: 'farest', role: '系统架构师', avatar: './assets/app_assets/avatars/avatar_fangsheng.png', desc: '有限状态机 (FSM) 架构定义、多媒体工况流转协议与系统事件总线。' },
      { name: '传鹏', alias: '阿鹏', role: '硬件协同工程', avatar: './assets/app_assets/avatars/avatar_bingo.png', desc: '智能传感器硬件对接、端侧多通道信号采集与低功耗监听模块。' },
      { name: '张桂滨', alias: 'Gbin', role: '外设集成工程', avatar: './assets/app_assets/avatars/avatar_congyu.png', desc: '外设蓝牙广播与低功耗监听，端侧多模态协同实现。' },
      { name: '木子', alias: 'Muzi', role: '产品架构工程', avatar: './assets/app_assets/avatars/avatar_muzi.png', desc: '端侧业务流程梳理、BOM 物料规格设计与 24H 空间时间线编排。' },
      { name: '小六', alias: '66', role: '动效渲染管线', avatar: './assets/app_assets/avatars/avatar_xiaoliu.png', desc: '1080P 60FPS 硬解流混流合成、Alpha 透明通道叠加与动效管线。' },
      { name: 'Adam', alias: 'Adam', role: '交互设计系统', avatar: './assets/app_assets/avatars/avatar_adam.png', desc: '双梯形 Bento 几何裁切算法、响应式排版引擎与触控交互规范。' },
      { name: 'Bingo', alias: 'Bingo', role: '全栈架构总监', avatar: './assets/app_assets/avatars/avatar_bingo.png', desc: '端侧 Native Rebuild 全局技术架构重构、混合容器与传感器桥接。' },
      { name: '小白', alias: 'Xiaobai', role: '多模态模型算法', avatar: './assets/app_assets/avatars/avatar_xiaobai.png', desc: '端侧 CV 视觉脏污检测模型、轻量化网络量化部署与多模态感知。' },
      { name: '林一', alias: 'LinYi', role: '端侧体验工程', avatar: './assets/app_assets/avatars/avatar_linyi.png', desc: '全工况设备兼容性调优、触摸屏采样率校准与低延迟触控优化。' },
      { name: '佳豪', alias: 'Jiahao', role: '品质验证工程', avatar: './assets/app_assets/avatars/avatar_jiahao.png', desc: '端侧性能极限压测、内存泄漏拦截与长时间运行稳定性监测。' },
      { name: '黑黑', alias: 'Heihei', role: '系统稳定性工程', avatar: './assets/app_assets/avatars/avatar_heihei.png', desc: '自动化测试流水线构建、网络异常离线熔断与本地缓存策略。' },
      { name: 'Lex', alias: 'Lex', role: '数据服务架构', avatar: './assets/app_assets/avatars/avatar_lex.png', desc: '端侧 IndexedDB 双写持久化机制、数据加密与离线状态恢复。' },
      { name: '易明', alias: 'imyrs', role: '视觉算法系统', avatar: './assets/app_assets/avatars/avatar_imyrs.png', desc: '端侧视觉特征提取、图像比例矫正与零剪裁自适应渲染管线。' }
    ];

    const REAL_SCREENSHOTS = [
      { id: 1, file: 'Screenshot_20260919_174540_com_lyi_laomayoyo_MainActivity.JPG', title: 'STATE: 01 居室常态静止巡航' },
      { id: 2, file: 'Screenshot_20260919_174600_com_lyi_laomayoyo_MainActivity.JPG', title: 'STATE: 02 屏幕触碰响应反馈' },
      { id: 3, file: 'Screenshot_20260919_174613_com_lyi_laomayoyo_MainActivity.JPG', title: 'STATE: 03 脏污状态视觉告警' },
      { id: 4, file: 'Screenshot_20260919_174628_com_lyi_laomayoyo_MainActivity.JPG', title: 'STATE: 04 抚摸清洁动作自愈' },
      { id: 5, file: 'Screenshot_20260919_174648_com_lyi_laomayoyo_MainActivity.JPG', title: 'STATE: 05 定额食物投喂事件' },
      { id: 6, file: 'Screenshot_20260919_174700_com_lyi_laomayoyo_MainActivity.JPG', title: 'STATE: 06 逗猫棒动力学捕捉' },
      { id: 7, file: 'Screenshot_20260919_174713_com_lyi_laomayoyo_MainActivity.JPG', title: 'STATE: 07 生理体检听诊状态' },
      { id: 8, file: 'Screenshot_20260919_174724_com_lyi_laomayoyo_MainActivity.JPG', title: 'STATE: 08 静音恒温安睡模式' }
    ];

    function switchPhoneScreen(id) {
      const scr = REAL_SCREENSHOTS.find(s => s.id === id);
      if (!scr) return;
      document.getElementById('phone-screen-img').src = `./assets/screenshots/${scr.file}`;
      document.getElementById('current-screen-tag').textContent = scr.title;

      for (let i = 1; i <= 8; i++) {
        const btn = document.getElementById(`btn-scr-${i}`);
        if (btn) {
          if (i === id) {
            btn.className = 'px-2 py-0.5 rounded-lg text-[9px] font-mono font-bold bg-blue-600 text-white transition-all';
          } else {
            btn.className = 'px-2 py-0.5 rounded-lg text-[9px] font-mono font-bold hover:bg-slate-100 text-slate-700 transition-all';
          }
        }
      }
    }

    // -------------------------------------------------------------------------
    // 2. Pan & Zoom Engine with Mac Trackpad Smooth Gestures
    // -------------------------------------------------------------------------
    let panX = -950;
    let panY = -600;
    let zoomScale = 0.60;

    const viewport = document.getElementById('canvas-viewport');
    const stage = document.getElementById('canvas-stage');
    const zoomLevelEl = document.getElementById('zoom-level');

    function applyTransform() {
      stage.style.transform = `translate(${panX}px, ${panY}px) scale(${zoomScale})`;
      zoomLevelEl.textContent = `${Math.round(zoomScale * 100)}%`;
      drawLeaderLines();
    }

    function adjustZoom(factor) {
      const rect = viewport.getBoundingClientRect();
      const wCenter = rect.width / 2;
      const hCenter = rect.height / 2;
      const prevScale = zoomScale;
      const nextScale = Math.min(Math.max(0.18, prevScale * factor), 2.8);
      panX = wCenter - (wCenter - panX) * (nextScale / prevScale);
      panY = hCenter - (hCenter - panY) * (nextScale / prevScale);
      zoomScale = nextScale;
      applyTransform();
    }

    // --- Mac Trackpad Wheel Event Listener ---
    viewport.addEventListener('wheel', (e) => {
      e.preventDefault();

      if (e.ctrlKey) {
        const rect = viewport.getBoundingClientRect();
        const cursorX = e.clientX - rect.left;
        const cursorY = e.clientY - rect.top;
        const prevScale = zoomScale;
        const zoomDelta = -e.deltaY * 0.015;
        const newScale = Math.min(Math.max(0.18, prevScale * Math.exp(zoomDelta)), 2.8);

        panX = cursorX - (cursorX - panX) * (newScale / prevScale);
        panY = cursorY - (cursorY - panY) * (newScale / prevScale);
        zoomScale = newScale;
      } else {
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
      const newScale = Math.min(Math.max(0.18, gestureStartScale * e.scale), 2.8);

      panX = cursorX - (cursorX - panX) * (newScale / prevScale);
      panY = cursorY - (cursorY - panY) * (newScale / prevScale);
      zoomScale = newScale;
      applyTransform();
    }, { passive: false });

    // -------------------------------------------------------------------------
    // 3. FIGMA-LIKE DRAGGABLE NODE SYSTEM (按住自由拖动任意组件)
    // -------------------------------------------------------------------------
    let activeDraggedNode = null;
    let nodeStartX = 0;
    let nodeStartY = 0;
    let mouseStartClientX = 0;
    let mouseStartClientY = 0;
    let isCanvasPanning = false;
    let canvasStartMouseX = 0;
    let canvasStartMouseY = 0;
    let hasDraggedNode = false;

    viewport.addEventListener('mousedown', (e) => {
      if (e.target.closest('input') || e.target.closest('button') || e.target.closest('video') || e.target.closest('aside')) {
        return;
      }

      const draggableNode = e.target.closest('.draggable-node');
      if (draggableNode) {
        activeDraggedNode = draggableNode;
        mouseStartClientX = e.clientX;
        mouseStartClientY = e.clientY;
        nodeStartX = parseFloat(draggableNode.style.left) || draggableNode.offsetLeft;
        nodeStartY = parseFloat(draggableNode.style.top) || draggableNode.offsetTop;
        draggableNode.style.zIndex = '45';
        e.stopPropagation();
      } else {
        isCanvasPanning = true;
        canvasStartMouseX = e.clientX - panX;
        canvasStartMouseY = e.clientY - panY;
      }
    });

    window.addEventListener('mousemove', (e) => {
      if (activeDraggedNode) {
        if (Math.hypot(e.clientX - mouseStartClientX, e.clientY - mouseStartClientY) > 6) {
          hasDraggedNode = true;
        }
        const deltaX = (e.clientX - mouseStartClientX) / zoomScale;
        const deltaY = (e.clientY - mouseStartClientY) / zoomScale;
        activeDraggedNode.style.left = `${nodeStartX + deltaX}px`;
        activeDraggedNode.style.top = `${nodeStartY + deltaY}px`;
        drawLeaderLines();
      } else if (isCanvasPanning) {
        panX = e.clientX - canvasStartMouseX;
        panY = e.clientY - canvasStartMouseY;
        applyTransform();
      }
    });

    window.addEventListener('mouseup', () => {
      if (activeDraggedNode) {
        activeDraggedNode.style.zIndex = '20';
        activeDraggedNode = null;
      }
      isCanvasPanning = false;
      setTimeout(() => { hasDraggedNode = false; }, 50);
    });

    window.addEventListener('click', (e) => {
      if (hasDraggedNode) {
        e.stopPropagation();
        e.preventDefault();
      }
    }, true);

    // -------------------------------------------------------------------------
    // 4. Quick Zone Focus Logic
    // -------------------------------------------------------------------------
    function focusZone(zoneId) {
      const vW = viewport.clientWidth;
      const vH = viewport.clientHeight;

      let targetX = 2240;
      let targetY = 1460;
      let targetScale = 0.65;

      if (zoneId === 'center') {
        targetX = 2240;
        targetY = 1460;
        targetScale = 0.70;
      } else if (zoneId === 'north') {
        targetX = 2250;
        targetY = 320;
        targetScale = 0.68;
      } else if (zoneId === 'ref') {
        targetX = 770;
        targetY = 480;
        targetScale = 0.65;
      } else if (zoneId === 'candidates') {
        targetX = 3880;
        targetY = 480;
        targetScale = 0.62;
      } else if (zoneId === 'west') {
        targetX = 700;
        targetY = 1480;
        targetScale = 0.62;
      } else if (zoneId === 'east') {
        targetX = 3920;
        targetY = 1480;
        targetScale = 0.60;
      } else if (zoneId === 'posters') {
        targetX = 800;
        targetY = 2500;
        targetScale = 0.65;
      } else if (zoneId === 'shaders') {
        targetX = 3920;
        targetY = 2500;
        targetScale = 0.65;
      } else if (zoneId === 'south') {
        targetX = 2320;
        targetY = 2700;
        targetScale = 0.65;
      }

      panX = (vW / 2) - (targetX * targetScale);
      panY = (vH / 2) - (targetY * targetScale);
      zoomScale = targetScale;
      applyTransform();
    }

    function resetView() {
      const vW = viewport.clientWidth;
      const vH = viewport.clientHeight;
      const fitScale = Math.min(vW / 4800, vH / 3400) * 0.95;
      zoomScale = Math.max(0.18, fitScale);
      panX = (vW - 4800 * zoomScale) / 2;
      panY = (vH - 3400 * zoomScale) / 2;
      applyTransform();
    }

    // -------------------------------------------------------------------------
    // 5. Dynamic Exploded View Separation & Leader Lines Engine
    // -------------------------------------------------------------------------
    let currentExplosion = 70;

    function setExplosion(val) {
      document.getElementById('explosion-slider').value = val;
      updateExplosion(val);
    }

    function updateExplosion(val) {
      currentExplosion = val;
      document.getElementById('explosion-val').textContent = `${val}%`;
      const factor = val / 100;

      const gaugesEl = document.getElementById('module-gauges');
      const mediaEl = document.getElementById('module-media');
      const timelineEl = document.getElementById('module-timeline');
      const bentoEl = document.getElementById('module-bento');

      gaugesEl.style.transform = `translateY(${-140 * factor}px)`;
      mediaEl.style.transform = `translateX(${180 * factor}px)`;
      timelineEl.style.transform = `translateX(${-180 * factor}px)`;
      bentoEl.style.transform = `translateY(${140 * factor}px)`;

      setTimeout(drawLeaderLines, 40);
    }

    document.getElementById('explosion-slider').addEventListener('input', (e) => {
      updateExplosion(parseInt(e.target.value, 10));
    });

    function drawLeaderLines() {
      const svg = document.getElementById('svg-leader-lines');
      if (!svg) return;
      svg.innerHTML = '';

      function getCenter(el) {
        if (!el) return { x: 0, y: 0 };
        const left = parseFloat(el.style.left) || el.offsetLeft;
        const top = parseFloat(el.style.top) || el.offsetTop;
        const width = el.offsetWidth || parseFloat(el.style.width) || 0;
        const height = el.offsetHeight || parseFloat(el.style.height) || 0;
        
        let tx = 0, ty = 0;
        const transform = el.style.transform;
        if (transform) {
          const matchX = transform.match(/translateX\(([-\d.]+)px\)/);
          const matchY = transform.match(/translateY\(([-\d.]+)px\)/);
          if (matchX) tx = parseFloat(matchX[1]);
          if (matchY) ty = parseFloat(matchY[1]);
        }
        return { x: left + width / 2 + tx, y: top + height / 2 + ty, left: left + tx, right: left + width + tx, top: top + ty, bottom: top + height + ty };
      }

      function addLine(x1, y1, x2, y2, color = '#2563EB') {
        const line = document.createElementNS('http://www.w3.org/2000/svg', 'line');
        line.setAttribute('x1', x1);
        line.setAttribute('y1', y1);
        line.setAttribute('x2', x2);
        line.setAttribute('y2', y2);
        line.setAttribute('class', 'tech-leader-line');
        line.style.stroke = color;
        svg.appendChild(line);

        const circle1 = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
        circle1.setAttribute('cx', x1);
        circle1.setAttribute('cy', y1);
        circle1.setAttribute('r', 3.5);
        circle1.setAttribute('class', 'tech-leader-joint');
        circle1.style.fill = color;
        svg.appendChild(circle1);

        const circle2 = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
        circle2.setAttribute('cx', x2);
        circle2.setAttribute('cy', y2);
        circle2.setAttribute('r', 3.5);
        circle2.setAttribute('class', 'tech-leader-joint');
        circle2.style.fill = color;
        svg.appendChild(circle2);
      }

      const frame = getCenter(document.getElementById('core-device-frame'));
      const gauges = getCenter(document.getElementById('module-gauges'));
      const media = getCenter(document.getElementById('module-media'));
      const timeline = getCenter(document.getElementById('module-timeline'));
      const bento = getCenter(document.getElementById('module-bento'));

      addLine(frame.x, frame.top + 40, gauges.x, gauges.bottom, '#2563EB');
      addLine(frame.right - 20, frame.y - 120, media.left, media.y, '#059669');
      addLine(frame.left + 20, frame.y + 120, timeline.right, timeline.y, '#D97706');
      addLine(frame.x, frame.bottom - 40, bento.x, bento.top, '#4F46E5');

      const north = getCenter(document.getElementById('zone-north'));
      const ref = getCenter(document.getElementById('zone-reference'));
      const cand = getCenter(document.getElementById('zone-candidates'));
      const bom = getCenter(document.getElementById('zone-bom'));
      const screens = getCenter(document.getElementById('zone-screens'));
      const team = getCenter(document.getElementById('zone-team'));

      addLine(ref.right, ref.y, north.left, ref.y, '#CBD5E1');
      addLine(north.right, cand.y, cand.left, cand.y, '#CBD5E1');
      addLine(bom.right, timeline.y, timeline.left, timeline.y, '#CBD5E1');
      addLine(media.right, screens.y, screens.left, screens.y, '#CBD5E1');
      addLine(bento.x, bento.bottom, team.x, team.top, '#CBD5E1');

      const posters = getCenter(document.getElementById('zone-posters'));
      const shaders = getCenter(document.getElementById('zone-shaders'));
      addLine(bom.x, bom.bottom, posters.x, posters.top, '#CBD5E1');
      addLine(screens.x, screens.bottom, shaders.x, shaders.top, '#CBD5E1');
      addLine(posters.right, posters.y, team.left, team.y, '#CBD5E1');
      addLine(team.right, team.y, shaders.left, shaders.y, '#CBD5E1');
    }

    // -------------------------------------------------------------------------
    // 6. Dynamic Content Population (All titles unabridged, text wraps cleanly)
    // -------------------------------------------------------------------------
    function populateTimeline() {
      const container = document.getElementById('dissected-timeline-grid');
      let html = '';
      SCHEDULE_DATA.forEach(it => {
        html += `
          <div class="bg-slate-50 p-2 rounded-xl border border-slate-200 flex items-center gap-2.5 cursor-pointer hover:border-amber-400 hover:bg-white transition-all shadow-2xs" onclick="inspectItem(${it.id})">
            <div class="w-8 h-8 rounded-lg bg-white border border-slate-200 flex items-center justify-center p-0.5 flex-shrink-0 shadow-2xs">
              <img src="${it.icon}" class="no-crop-img" alt="${it.title}">
            </div>
            <div class="min-w-0 flex-1 text-left">
              <div class="text-[9.5px] font-bold text-slate-800 font-mono break-words leading-snug">${it.title}</div>
              <div class="text-[8px] text-amber-600 font-mono mt-0.5">${it.time} · ${it.person}</div>
            </div>
          </div>
        `;
      });
      container.innerHTML = html;
    }

    function populateBOM() {
      // 1. 11 Care Props with full unabridged titles
      const bContainer = document.getElementById('unified-bom-items');
      let bHtml = '';
      SCHEDULE_DATA.forEach(it => {
        bHtml += `
          <div class="bg-slate-50 p-2.5 rounded-xl border border-slate-200 hover:border-indigo-400 transition-all flex flex-col items-center text-center cursor-pointer" onclick="inspectItem(${it.id})">
            <div class="w-12 h-12 cleanroom-pad rounded-lg flex items-center justify-center mb-1.5 p-1 border border-slate-200 shadow-2xs">
              <img src="${it.icon}" class="no-crop-img drop-shadow-2xs" alt="${it.title}">
            </div>
            <span class="text-[10px] font-bold text-slate-800 font-mono break-words leading-tight w-full">${it.title}</span>
            <span class="text-[8px] text-slate-400 font-mono mt-1">${it.time} · ${it.person} (责任人)</span>
          </div>
        `;
      });
      bContainer.innerHTML = bHtml;

      // 2. HUD Gauges & Action Controls with full unabridged names
      const uContainer = document.getElementById('unified-bom-icons');
      const uiControls = [
        { name: 'ic_index_catlove.png', title: '爱猫加权徽标仪表', path: './assets/app_assets/ui_icons/ic_index_catlove.png' },
        { name: 'ic_index_happiness.png', title: '快乐值基础指标仪表', path: './assets/app_assets/ui_icons/ic_index_happiness.png' },
        { name: 'ic_index_happiness_blue.png', title: '清爽低饱和状态仪表', path: './assets/app_assets/ui_icons/ic_index_happiness_blue.png' },
        { name: 'ic_index_happiness_green.png', title: '活力健康态状态仪表', path: './assets/app_assets/ui_icons/ic_index_happiness_green.png' },
        { name: 'ic_index_happiness_orange.png', title: '疲惫警戒态状态仪表', path: './assets/app_assets/ui_icons/ic_index_happiness_orange.png' },
        { name: 'ic_index_happiness_red.png', title: '脏污高急迫告警仪表', path: './assets/app_assets/ui_icons/ic_index_happiness_red.png' },
        { name: 'ic_index_happiness_tight.png', title: '紧凑版指标无损切图', path: './assets/app_assets/ui_icons/ic_index_happiness_tight.png' },
        { name: 'ic_btn_like.png', title: '日常互动点赞默认状态', path: './assets/app_assets/ui_icons/ic_btn_like.png' },
        { name: 'ic_btn_like_active.png', title: '点赞高亮激活态图标', path: './assets/app_assets/ui_icons/ic_btn_like_active.png' },
        { name: 'ic_btn_comment.png', title: '手账评论留言互动手柄', path: './assets/app_assets/ui_icons/ic_btn_comment.png' },
        { name: 'ic_btn_expand.png', title: '手账卡片展开激活手柄', path: './assets/app_assets/ui_icons/ic_btn_expand.png' },
        { name: 'ic_btn_collapse.png', title: '手账卡片收起复位手柄', path: './assets/app_assets/ui_icons/ic_btn_collapse.png' }
      ];
      let uHtml = '';
      uiControls.forEach(ui => {
        uHtml += `
          <div class="bg-slate-50 p-2.5 rounded-xl border border-slate-200 hover:border-rose-400 transition-all flex flex-col items-center text-center cursor-pointer" onclick="inspectImage('${ui.path}', '${ui.title}')">
            <div class="w-10 h-10 cleanroom-pad rounded-lg flex items-center justify-center mb-1 p-0.5 border border-slate-200 shadow-2xs">
              <img src="${ui.path}" class="no-crop-img drop-shadow-2xs" alt="${ui.title}">
            </div>
            <span class="text-[10px] font-bold text-slate-800 font-mono break-words leading-tight w-full">${ui.title}</span>
            <span class="text-[8px] text-slate-400 font-mono mt-1 break-all w-full">${ui.name}</span>
          </div>
        `;
      });
      uContainer.innerHTML = uHtml;

      // 3. 7 Archive Cards with full unabridged record labels
      const aContainer = document.getElementById('unified-bom-archives');
      let aHtml = '';
      [163, 164, 165, 166, 167, 168, 169].forEach(id => {
        aHtml += `
          <div class="bg-slate-50 p-2 rounded-xl border border-slate-200 hover:border-indigo-400 transition-all">
            <div class="w-full h-24 bg-slate-900/5 rounded-lg overflow-hidden mb-1.5 flex items-center justify-center p-1 cursor-pointer hover:scale-105 transition-transform" onclick="inspectImage('./assets/app_assets/archives/archive_${id}.png', '持久化结构记录 #${id}')">
              <img src="./assets/app_assets/archives/archive_${id}.png" class="no-crop-img" alt="手账${id}">
            </div>
            <div class="text-[9px] font-bold text-slate-800 text-center font-mono break-words">结构化记录 #${id}</div>
            <div class="text-[7.5px] text-slate-400 text-center font-mono mt-0.5">自然尺寸 · 零裁剪</div>
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
          <div class="p-3.5 rounded-xl bg-slate-50 border border-slate-200 hover:border-blue-500 hover:bg-white transition-all flex items-start gap-3.5 cursor-pointer" onclick="inspectMember('${m.alias}')">
            <!-- Strictly Aligned 48x48 Square Avatar Token -->
            <div class="engineer-avatar-box shadow-xs ring-1 ring-slate-200 flex-shrink-0 flex items-center justify-center p-0.5 mt-0.5">
              <img src="${m.avatar}" class="no-crop-img" alt="${m.alias}">
            </div>
            <div class="min-w-0 text-left flex-1">
              <div class="flex items-center justify-between">
                <span class="text-xs font-black text-slate-900 font-mono break-words">${m.alias} <span class="font-normal text-slate-400">(${m.name})</span></span>
                <span class="text-[8px] font-mono px-1.5 py-0.2 rounded bg-blue-50 text-blue-700 font-bold border border-blue-200">OWNER</span>
              </div>
              <div class="text-[10.5px] font-bold text-blue-600 font-mono mt-0.5 break-words">${m.role}</div>
              <div class="text-[9.5px] text-slate-500 mt-1 leading-snug break-words">${m.desc}</div>
            </div>
          </div>
        `;
      });
      container.innerHTML = html;
    }

    // -------------------------------------------------------------------------
    // 7. Component & Asset Inspector Drawer
    // -------------------------------------------------------------------------
    function inspectComponent(type) {
      const drawer = document.getElementById('inspector-drawer');
      const titleEl = document.getElementById('insp-title');
      const tagEl = document.getElementById('insp-tag');
      const imgEl = document.getElementById('insp-img');
      const nameEl = document.getElementById('insp-name');
      const pathEl = document.getElementById('insp-path');
      const ratioEl = document.getElementById('insp-ratio');
      const authorEl = document.getElementById('insp-author');
      const descEl = document.getElementById('insp-desc');

      if (type === 'gauges') {
        titleEl.textContent = '状态感知与生命指标控制系统';
        tagEl.textContent = '[ASM-01 · SENSORS]';
        imgEl.src = './assets/app_assets/ui_icons/ic_index_catlove.png';
        nameEl.textContent = 'HUD 生命力与加权爱猫指数计算模型';
        pathEl.textContent = '/assets/app_assets/ui_icons/ic_index_*.png';
        ratioEl.textContent = 'Vector SVG / Alpha PNG 采样流 · 零剪裁';
        authorEl.textContent = '阿杰 (视觉工程) / Lex (数据服务)';
        descEl.textContent = '端侧 1000ms 心跳轮询驱动。包含快乐指数滤波方程、脏污预警阈值判定算法与加权爱猫积分模型。';
      } else if (type === 'media') {
        titleEl.textContent = '视觉多媒体硬件解码与动效管线';
        tagEl.textContent = '[ASM-02 · MEDIA PIPELINE]';
        imgEl.src = './assets/app_assets/hero_cat_sitting_tight.png';
        nameEl.textContent = '1080P 60FPS 硬解多媒体流';
        pathEl.textContent = '/assets/app_assets/home_cat_*.mp4';
        ratioEl.textContent = 'H.264 High Profile 硬件解码流 · 零剪裁';
        authorEl.textContent = '小六 (动效工程) / Bingo (系统架构)';
        descEl.textContent = '三组无缝切换硬解短视频流水线，Alpha 通道图层混合技术与 60fps 恒定锁帧保障。视频正在卡片中正常自动播放。';
      } else if (type === 'timeline') {
        titleEl.textContent = '24H 空间感知与事件调度总线';
        tagEl.textContent = '[ASM-03 · TIMELINE 11 ITEMS]';
        imgEl.src = './assets/app_assets/ic_board_brush.png';
        nameEl.textContent = '11 大 3D 照护事件道具部件';
        pathEl.textContent = '/assets/app_assets/ic_board_*.png';
        ratioEl.textContent = '3D 拟物渲染无损 Alpha 通道 · 零剪裁';
        authorEl.textContent = '阿杰 (视觉工程) / 木子 (产品架构)';
        descEl.textContent = '24 小时事件调度总线，支持时间触发、地理围栏触发与端侧设备低功耗轮询监听。';
      } else if (type === 'bento') {
        titleEl.textContent = '双梯形 Bento 几何裁切与动力学矩阵';
        tagEl.textContent = '[ASM-04 · TRAPEZOID SHADER]';
        imgEl.src = './assets/app_assets/ui_icons/ic_btn_trophy.png';
        nameEl.textContent = '10.3° 倾角圆角直角双梯形着色器';
        pathEl.textContent = 'SVG ClipPath + DropShadow 硬件加速';
        ratioEl.textContent = '硬件级矢量边缘裁切与混合模式 · 零剪裁';
        authorEl.textContent = 'Adam (交互设计) / Howwoy (原生交互)';
        descEl.textContent = '左梯形承载实时加权排行榜，右梯形承载持久化日记系统；边缘 14.0px 精密贴合公差。';
      }

      drawer.classList.remove('translate-x-[440px]');
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
      document.getElementById('insp-ratio').textContent = '3D 拟物透明 Alpha · 原生尺寸零剪裁';
      document.getElementById('insp-author').textContent = `${it.person} (模块责任人)`;
      document.getElementById('insp-desc').textContent = it.desc;
      drawer.classList.remove('translate-x-[440px]');
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
      document.getElementById('insp-ratio').textContent = '1:1 正方形原生免冠画幅 · 零剪裁';
      document.getElementById('insp-author').textContent = `${mem.name} · ${mem.alias}`;
      document.getElementById('insp-desc').textContent = mem.desc;
      drawer.classList.remove('translate-x-[440px]');
    }

    function inspectImage(src, title) {
      const drawer = document.getElementById('inspector-drawer');
      document.getElementById('insp-title').textContent = title;
      document.getElementById('insp-tag').textContent = '[ASSET TELEMETRY]';
      document.getElementById('insp-img').src = src;
      document.getElementById('insp-name').textContent = title;
      document.getElementById('insp-path').textContent = src;
      document.getElementById('insp-ratio').textContent = '100% 原始长宽比完整呈现 · 零剪裁';
      document.getElementById('insp-author').textContent = '工程资产归档库';
      document.getElementById('insp-desc').textContent = '系统全量素材与选型实验样张，严格尊重其原始拍摄或渲染画幅，作为视觉建模、多模态采样及状态机触发判定的真实工程依据。';
      drawer.classList.remove('translate-x-[440px]');
    }

    function closeInspector() {
      document.getElementById('inspector-drawer').classList.add('translate-x-[440px]');
    }

    // -------------------------------------------------------------------------
    // 8. Bulletproof Video Autoplay Engine
    // -------------------------------------------------------------------------
    function ensureAllVideosAutoplay() {
      const vids = document.querySelectorAll('video');
      vids.forEach(v => {
        v.muted = true;
        v.defaultMuted = true;
        v.playsInline = true;
        v.setAttribute('playsinline', '');
        v.setAttribute('webkit-playsinline', '');
        v.setAttribute('muted', '');
        v.setAttribute('autoplay', '');
        v.setAttribute('loop', '');
        const p = v.play();
        if (p && typeof p.catch === 'function') {
          p.catch(() => {});
        }
      });
    }

    // -------------------------------------------------------------------------
    // 9. Boot Initialization
    // -------------------------------------------------------------------------
    window.addEventListener('DOMContentLoaded', () => {
      populateTimeline();
      populateBOM();
      populateTeam();
      updateExplosion(70);
      focusZone('center');
      ensureAllVideosAutoplay();
    });

    window.addEventListener('load', ensureAllVideosAutoplay);
    document.addEventListener('visibilitychange', () => {
      if (!document.hidden) ensureAllVideosAutoplay();
    });
    window.addEventListener('pointerdown', ensureAllVideosAutoplay, { once: true });
    setInterval(ensureAllVideosAutoplay, 3500);

    window.addEventListener('resize', () => {
      drawLeaderLines();
    });
  </script>
</body>
</html>
"""

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(html_code)

print("Perfect Showcase with zero truncation, enlarged videos, and bulletproof autoplay built successfully!")
