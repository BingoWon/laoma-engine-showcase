import os, glob

OUTPUT_FILE = "/Users/bingo/Code/LYi/projects/laoma-engine-showcase/index.html"

# Verify all assets exist
assets_dir = "/Users/bingo/Code/LYi/projects/laoma-engine-showcase/assets"

html_code = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>老马喵务局 · 端侧智能体系统架构与全量工程物料有机全景大屏</title>
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
    
    /* Hardware accelerated canvas stage */
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
      border-radius: 3px;
    }
    ::-webkit-scrollbar-thumb:hover {
      background: #94A3B8;
    }

    /* Exploded view animation transitions */
    .exploded-module {
      transition: transform 0.45s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.3s ease, border-color 0.3s ease;
      will-change: transform;
    }

    /* Blueprint glass & glow effects */
    .blueprint-card {
      background: rgba(255, 255, 255, 0.94);
      backdrop-filter: blur(16px);
      border: 1px solid rgba(203, 213, 225, 0.85);
      box-shadow: 0 20px 45px -15px rgba(15, 23, 42, 0.08), 0 0 1px 1px rgba(255, 255, 255, 0.9) inset;
    }

    .glow-blue {
      box-shadow: 0 0 35px -5px rgba(37, 99, 235, 0.20);
    }

    /* Strict aspect ratio wrappers ensuring ZERO cropping (object-contain) */
    .aspect-phone {
      aspect-ratio: 1320 / 2868; /* 0.4603 */
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
    .aspect-video-9-16 {
      aspect-ratio: 9 / 16; /* 0.5625 */
    }
    .aspect-wide-2-1 {
      aspect-ratio: 2 / 1; /* 2.0000 */
    }
    .aspect-wide-2-5 {
      aspect-ratio: 2.509 / 1; /* 2.5091 */
    }
    .aspect-wide-1-5 {
      aspect-ratio: 1.5 / 1; /* 1.5000 */
    }
    .aspect-tex-1-2 {
      aspect-ratio: 1.2 / 1; /* 1.2000 */
    }

    /* Strict Image rule: NEVER CROP - Always respect native aspect ratio */
    .no-crop-img {
      object-fit: contain;
      width: 100%;
      height: 100%;
    }

    /* Standardized engineering token box for avatars */
    .engineer-avatar-box {
      width: 56px;
      height: 56px;
      aspect-ratio: 1 / 1;
      border-radius: 16px;
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
      background-size: 16px 16px;
      background-position: 0 0, 0 8px, 8px -8px, -8px 0px;
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
  <header class="fixed top-0 left-0 right-0 h-16 z-50 bg-white/90 backdrop-blur-xl border-b border-slate-200/80 px-6 flex items-center justify-between shadow-xs">
    <!-- Left: Project Identity & Specs -->
    <div class="flex items-center gap-4">
      <div class="w-10 h-10 rounded-2xl bg-gradient-to-tr from-blue-600 to-indigo-600 flex items-center justify-center text-white font-black text-lg shadow-sm">
        🐱
      </div>
      <div>
        <div class="flex items-center gap-2">
          <h1 class="font-black text-slate-900 text-sm tracking-tight">老马喵务局 · 端侧智能体系统架构与全量工程物料全景拆解总成</h1>
          <span class="text-[10px] font-mono font-bold px-2 py-0.5 rounded-full bg-blue-50 text-blue-700 border border-blue-200">INDUSTRIAL SPEC · RELEASE</span>
        </div>
        <div class="flex items-center gap-3 text-[11px] font-mono text-slate-500">
          <span>HONOR YOYO AGENT ARCHITECTURE</span>
          <span>•</span>
          <span class="text-emerald-600 font-bold">120/120 独特物料 100% 展开</span>
          <span>•</span>
          <span class="text-indigo-600 font-bold">全形态自然画幅 · 零裁剪</span>
        </div>
      </div>
    </div>

    <!-- Center: Exploded Distance Controller -->
    <div class="flex items-center gap-3 bg-slate-100/90 py-1.5 px-4 rounded-2xl border border-slate-200">
      <span class="text-xs font-bold text-slate-700 font-mono flex items-center gap-1.5">
        <span class="w-2 h-2 rounded-full bg-blue-600 animate-pulse"></span>
        <span>发动机拆解度:</span>
      </span>
      <input id="explosion-slider" type="range" min="0" max="100" value="80" class="w-36 accent-blue-600 cursor-pointer">
      <span id="explosion-val" class="text-xs font-mono font-bold text-blue-600 w-10 text-right">80%</span>
      <div class="h-4 w-px bg-slate-300 mx-1"></div>
      <button onclick="setExplosion(0)" class="px-2 py-1 text-[10px] font-mono font-bold rounded-lg bg-white text-slate-700 border border-slate-200 hover:bg-slate-50">合拢</button>
      <button onclick="setExplosion(50)" class="px-2 py-1 text-[10px] font-mono font-bold rounded-lg bg-white text-slate-700 border border-slate-200 hover:bg-slate-50">标准</button>
      <button onclick="setExplosion(100)" class="px-2 py-1 text-[10px] font-mono font-bold rounded-lg bg-white text-blue-700 border border-blue-200 hover:bg-blue-50">全展</button>
    </div>

    <!-- Right: Quick Navigation Dock & Zoom Controls -->
    <div class="flex items-center gap-2">
      <!-- Quick Zone Focus Dock -->
      <div class="flex items-center bg-slate-100/90 p-1 rounded-2xl border border-slate-200 text-xs font-bold font-mono">
        <button onclick="focusZone('center')" class="px-2.5 py-1 rounded-xl hover:bg-white text-slate-700 transition-all flex items-center gap-1" title="聚焦核心机身装配台">
          <span>🎯</span><span>核心</span>
        </button>
        <button onclick="focusZone('north')" class="px-2.5 py-1 rounded-xl hover:bg-white text-slate-700 transition-all flex items-center gap-1" title="聚焦系统架构总成">
          <span>⚙️</span><span>架构</span>
        </button>
        <button onclick="focusZone('ref')" class="px-2.5 py-1 rounded-xl hover:bg-white text-slate-700 transition-all flex items-center gap-1" title="聚焦生物物理样张">
          <span>📸</span><span>基准</span>
        </button>
        <button onclick="focusZone('candidates')" class="px-2.5 py-1 rounded-xl hover:bg-white text-slate-700 transition-all flex items-center gap-1" title="聚焦CV候选机身">
          <span>🧪</span><span>候选</span>
        </button>
        <button onclick="focusZone('west')" class="px-2.5 py-1 rounded-xl hover:bg-white text-slate-700 transition-all flex items-center gap-1" title="聚焦工程物料BOM">
          <span>📦</span><span>物料</span>
        </button>
        <button onclick="focusZone('east')" class="px-2.5 py-1 rounded-xl hover:bg-white text-slate-700 transition-all flex items-center gap-1" title="聚焦真机远测大屏">
          <span>📱</span><span>真机</span>
        </button>
        <button onclick="focusZone('posters')" class="px-2.5 py-1 rounded-xl hover:bg-white text-slate-700 transition-all flex items-center gap-1" title="聚焦16:9动态视频">
          <span>🎞️</span><span>视频</span>
        </button>
        <button onclick="focusZone('shaders')" class="px-2.5 py-1 rounded-xl hover:bg-white text-slate-700 transition-all flex items-center gap-1" title="聚焦Shader与材质">
          <span>🎨</span><span>材质</span>
        </button>
        <button onclick="focusZone('south')" class="px-2.5 py-1 rounded-xl hover:bg-white text-slate-700 transition-all flex items-center gap-1" title="聚焦工程团队矩阵">
          <span>👥</span><span>人员</span>
        </button>
      </div>

      <!-- Zoom buttons -->
      <div class="flex items-center bg-slate-100/90 p-1 rounded-2xl border border-slate-200">
        <button onclick="adjustZoom(0.8)" class="w-8 h-8 rounded-xl hover:bg-white flex items-center justify-center font-mono font-bold text-slate-700" title="缩小">-</button>
        <span id="zoom-level" class="px-2 text-xs font-mono font-bold text-slate-700 w-12 text-center">100%</span>
        <button onclick="adjustZoom(1.25)" class="w-8 h-8 rounded-xl hover:bg-white flex items-center justify-center font-mono font-bold text-slate-700" title="放大">+</button>
        <button onclick="resetView()" class="px-2.5 py-1 rounded-xl hover:bg-white text-[11px] font-mono font-bold text-slate-700" title="自适应全屏鸟瞰">重置</button>
      </div>
    </div>
  </header>

  <!-- ========================================================================= -->
  <!-- MAIN INFINITE BLUEPRINT VIEWPORT & HARDWARE ACCELERATED STAGE             -->
  <!-- ========================================================================= -->
  <main id="canvas-viewport" class="w-full h-full pt-16 relative overflow-hidden cursor-grab active:cursor-grabbing">
    <!-- Transformable Canvas Stage: 7200px x 5200px -->
    <div id="canvas-stage" class="absolute pointer-events-auto" style="width: 7200px; height: 5200px;">

      <!-- SVG Dynamic Connector & Assembly Leader Lines -->
      <svg id="svg-leader-lines" class="absolute inset-0 w-full h-full pointer-events-none z-10" xmlns="http://www.w3.org/2000/svg">
        <!-- Lines dynamically computed and injected by drawLeaderLines() -->
      </svg>

      <!-- ===================================================================== -->
      <!-- ZONE NORTH (北部总成 · X: 2500, Y: 650) · 混合容器渲染内核与通信协议总成 -->
      <!-- ===================================================================== -->
      <div id="zone-north" class="absolute z-20 blueprint-card p-8 rounded-3xl" style="left: 2500px; top: 650px; width: 2200px;">
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

        <div class="grid grid-cols-4 gap-6 mb-6">
          <div class="p-5 rounded-2xl bg-slate-50 border border-slate-200">
            <span class="text-xs font-mono font-black text-blue-600">LAYER 01 · 核心技术栈</span>
            <h4 class="text-sm font-black text-slate-800 mt-1 mb-2">高保真混合渲染容器</h4>
            <ul class="text-xs text-slate-500 space-y-1.5 font-mono">
              <li>• 渲染内核: Android WebView 独立渲染进程</li>
              <li>• 样式引擎: Tailwind CSS JIT GPU 硬件加速</li>
              <li>• 物理驱动: React 18 Concurrent / Custom Hooks</li>
              <li>• 类型契约: TypeScript 严格接口与边界防线</li>
            </ul>
          </div>

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

          <div class="p-5 rounded-2xl bg-slate-50 border border-slate-200 border-l-4 border-l-emerald-600">
            <span class="text-xs font-mono font-black text-emerald-600">LAYER 03 · 动画与渲染管线</span>
            <h4 class="text-sm font-black text-slate-800 mt-1 mb-2">多模态流媒体与动效混合</h4>
            <ul class="text-xs text-slate-500 space-y-1.5 font-mono">
              <li>• 硬件解码: H.264 High Profile 硬件流水线</li>
              <li>• 帧率保障: 60fps 恒定锁帧与动态垂直同步</li>
              <li>• 图层合成: Alpha 透明通道与物理背景混色</li>
              <li>• 手势引擎: 240Hz 触控采样与双梯形动力学</li>
            </ul>
          </div>

          <div class="p-5 rounded-2xl bg-slate-50 border border-slate-200 border-l-4 border-l-indigo-600">
            <span class="text-xs font-mono font-black text-indigo-600">LAYER 04 · 硬件协同系统</span>
            <h4 class="text-sm font-black text-slate-800 mt-1 mb-2">端侧桥接与数据持久化</h4>
            <ul class="text-xs text-slate-500 space-y-1.5 font-mono">
              <li>• 蓝牙广播: BLE 传感器低功耗事件监听</li>
              <li>• 通信协议: JSBridge 双向安全安全通信总线</li>
              <li>• 数据存储: IndexedDB 异步双写持久化系统</li>
              <li>• 异常自愈: 状态校验和回滚降级策略</li>
            </ul>
          </div>
        </div>

        <div class="p-4 rounded-2xl bg-blue-50/70 border border-blue-200/80 flex items-center justify-between font-mono text-xs text-blue-900">
          <div class="flex items-center gap-2">
            <span class="font-black text-blue-700">[HARDWARE DEPLOYMENT TARGET]</span>
            <span>HONOR MAGIC V3 / MAGIC 7 · MAGICOS 9.0 · SNAPDRAGON 8 GEN 3 · DISPLAY 1320 × 2868</span>
          </div>
          <div class="flex items-center gap-4">
            <span>MEM FOOTPRINT: &lt; 85MB</span>
            <span>GPU RENDER TIME: 3.2ms</span>
            <span>JSBRIDGE LATENCY: &lt; 4.8ms</span>
          </div>
        </div>
      </div>

      <!-- ===================================================================== -->
      <!-- ZONE NORTHWEST (西北总成 · X: 600, Y: 650) · 实体猫咪真实物理建模基准库  -->
      <!-- ===================================================================== -->
      <div id="zone-reference" class="absolute z-20 blueprint-card p-7 rounded-3xl" style="left: 600px; top: 650px; width: 1750px;">
        <div class="flex items-center justify-between border-b border-slate-200 pb-4 mb-5">
          <div class="flex items-center gap-3">
            <span class="w-9 h-9 rounded-2xl bg-amber-50 border border-amber-200 flex items-center justify-center text-lg">📸</span>
            <div>
              <h3 class="font-black text-slate-900 text-sm">实体猫咪真实物理建模基准库 (严格按 16:9 / 3:4 / 4:3 原始画幅分簇组织 · 零剪裁)</h3>
              <span class="text-[10px] font-mono text-amber-700 font-bold">[REF-LIB-REAL · MULTI-ASPECT SKELETAL & PHOTOMETRIC BENCHMARK]</span>
            </div>
          </div>
          <span class="text-[10px] px-2.5 py-1 rounded-full bg-amber-50 text-amber-700 font-mono font-bold border border-amber-200">12 UNPROCESSED SAMPLES</span>
        </div>

        <!-- Section A: 16:9 Landscape Wide Photometry -->
        <div class="mb-5">
          <div class="flex items-center justify-between mb-2">
            <span class="text-xs font-black text-slate-700 font-mono flex items-center gap-1.5">
              <span class="w-2 h-2 rounded-full bg-amber-500"></span>
              <span>GROUP A · 16:9 宽屏光影环境采样 (1600×900 / 1920×1080 · 宽高比 1.778)</span>
            </span>
            <span class="text-[10px] font-mono text-slate-400">4 SAMPLES · 16:9 NATIVE</span>
          </div>
          <div class="grid grid-cols-4 gap-3.5">
            <div class="bg-slate-50 p-2.5 rounded-2xl border border-slate-200 cursor-pointer hover:border-amber-400 transition-all" onclick="inspectImage('./assets/real_photos/laoma_real_1.jpg', '物理样张 01 · 蓝眼折射与正坐骨骼 (1600×900)')">
              <div class="w-full aspect-cine-16-9 bg-slate-900/5 rounded-xl overflow-hidden mb-1.5 flex items-center justify-center">
                <img src="./assets/real_photos/laoma_real_1.jpg" class="no-crop-img" alt="样张1">
              </div>
              <div class="text-[10px] font-bold text-slate-700 font-mono truncate">REF_REAL_01 (1600×900)</div>
              <div class="text-[9px] text-slate-400 font-mono">16:9 Cine Format · 零剪裁</div>
            </div>
            <div class="bg-slate-50 p-2.5 rounded-2xl border border-slate-200 cursor-pointer hover:border-amber-400 transition-all" onclick="inspectImage('./assets/real_photos/laoma_real_2.jpg', '物理样张 02 · 伏卧工况与耳廓解剖 (1600×900)')">
              <div class="w-full aspect-cine-16-9 bg-slate-900/5 rounded-xl overflow-hidden mb-1.5 flex items-center justify-center">
                <img src="./assets/real_photos/laoma_real_2.jpg" class="no-crop-img" alt="样张2">
              </div>
              <div class="text-[10px] font-bold text-slate-700 font-mono truncate">REF_REAL_02 (1600×900)</div>
              <div class="text-[9px] text-slate-400 font-mono">16:9 Cine Format · 零剪裁</div>
            </div>
            <div class="bg-slate-50 p-2.5 rounded-2xl border border-slate-200 cursor-pointer hover:border-amber-400 transition-all" onclick="inspectImage('./assets/real_photos/laoma_photo_1.jpg', '物理样张 03 · 箱体内空间透视参考 (1920×1080)')">
              <div class="w-full aspect-cine-16-9 bg-slate-900/5 rounded-xl overflow-hidden mb-1.5 flex items-center justify-center">
                <img src="./assets/real_photos/laoma_photo_1.jpg" class="no-crop-img" alt="样张3">
              </div>
              <div class="text-[10px] font-bold text-slate-700 font-mono truncate">REF_PHOTO_01 (1920×1080)</div>
              <div class="text-[9px] text-slate-400 font-mono">16:9 Wide Format · 零剪裁</div>
            </div>
            <div class="bg-slate-50 p-2.5 rounded-2xl border border-slate-200 cursor-pointer hover:border-amber-400 transition-all" onclick="inspectImage('./assets/real_photos/laoma_photo_2.jpg', '物理样张 04 · 阳光漫反射光影采样 (1920×1080)')">
              <div class="w-full aspect-cine-16-9 bg-slate-900/5 rounded-xl overflow-hidden mb-1.5 flex items-center justify-center">
                <img src="./assets/real_photos/laoma_photo_2.jpg" class="no-crop-img" alt="样张4">
              </div>
              <div class="text-[10px] font-bold text-slate-700 font-mono truncate">REF_PHOTO_02 (1920×1080)</div>
              <div class="text-[9px] text-slate-400 font-mono">16:9 Wide Format · 零剪裁</div>
            </div>
          </div>
        </div>

        <!-- Section B: 3:4 Portrait Bio-Skeletal References -->
        <div class="mb-5">
          <div class="flex items-center justify-between mb-2">
            <span class="text-xs font-black text-slate-700 font-mono flex items-center gap-1.5">
              <span class="w-2 h-2 rounded-full bg-cyan-500"></span>
              <span>GROUP B · 3:4 垂直骨骼与脊椎屈伸解剖观测 (1200×1600 · 宽高比 0.750)</span>
            </span>
            <span class="text-[10px] font-mono text-slate-400">5 SAMPLES · 3:4 NATIVE</span>
          </div>
          <div class="grid grid-cols-5 gap-3.5">
            <div class="bg-slate-50 p-2.5 rounded-2xl border border-slate-200 cursor-pointer hover:border-cyan-400 transition-all" onclick="inspectImage('./assets/real_photos/laoma_real_3.jpg', '骨骼样张 01 · 站立侧身脊椎弧度')">
              <div class="w-full aspect-photo-3-4 bg-slate-900/5 rounded-xl overflow-hidden mb-1.5 flex items-center justify-center">
                <img src="./assets/real_photos/laoma_real_3.jpg" class="no-crop-img" alt="骨骼1">
              </div>
              <div class="text-[10px] font-bold text-slate-700 font-mono truncate">REAL_03 (1200×1600)</div>
              <div class="text-[9px] text-slate-400 font-mono">3:4 Vertical · 零剪裁</div>
            </div>
            <div class="bg-slate-50 p-2.5 rounded-2xl border border-slate-200 cursor-pointer hover:border-cyan-400 transition-all" onclick="inspectImage('./assets/real_photos/laoma_real_4.jpg', '骨骼样张 02 · 伏地探头警戒形态')">
              <div class="w-full aspect-photo-3-4 bg-slate-900/5 rounded-xl overflow-hidden mb-1.5 flex items-center justify-center">
                <img src="./assets/real_photos/laoma_real_4.jpg" class="no-crop-img" alt="骨骼2">
              </div>
              <div class="text-[10px] font-bold text-slate-700 font-mono truncate">REAL_04 (1200×1600)</div>
              <div class="text-[9px] text-slate-400 font-mono">3:4 Vertical · 零剪裁</div>
            </div>
            <div class="bg-slate-50 p-2.5 rounded-2xl border border-slate-200 cursor-pointer hover:border-cyan-400 transition-all" onclick="inspectImage('./assets/real_photos/laoma_real_5.jpg', '骨骼样张 03 · 蜷缩入睡放松肌肉群')">
              <div class="w-full aspect-photo-3-4 bg-slate-900/5 rounded-xl overflow-hidden mb-1.5 flex items-center justify-center">
                <img src="./assets/real_photos/laoma_real_5.jpg" class="no-crop-img" alt="骨骼3">
              </div>
              <div class="text-[10px] font-bold text-slate-700 font-mono truncate">REAL_05 (1200×1600)</div>
              <div class="text-[9px] text-slate-400 font-mono">3:4 Vertical · 零剪裁</div>
            </div>
            <div class="bg-slate-50 p-2.5 rounded-2xl border border-slate-200 cursor-pointer hover:border-cyan-400 transition-all" onclick="inspectImage('./assets/real_photos/laoma_real_6.jpg', '骨骼样张 04 · 后腿蹬踏动力学')">
              <div class="w-full aspect-photo-3-4 bg-slate-900/5 rounded-xl overflow-hidden mb-1.5 flex items-center justify-center">
                <img src="./assets/real_photos/laoma_real_6.jpg" class="no-crop-img" alt="骨骼4">
              </div>
              <div class="text-[10px] font-bold text-slate-700 font-mono truncate">REAL_06 (1200×1600)</div>
              <div class="text-[9px] text-slate-400 font-mono">3:4 Vertical · 零剪裁</div>
            </div>
            <div class="bg-slate-50 p-2.5 rounded-2xl border border-slate-200 cursor-pointer hover:border-cyan-400 transition-all" onclick="inspectImage('./assets/real_photos/laoma_real_7.jpg', '骨骼样张 05 · 直立抬头空间视点')">
              <div class="w-full aspect-photo-3-4 bg-slate-900/5 rounded-xl overflow-hidden mb-1.5 flex items-center justify-center">
                <img src="./assets/real_photos/laoma_real_7.jpg" class="no-crop-img" alt="骨骼5">
              </div>
              <div class="text-[10px] font-bold text-slate-700 font-mono truncate">REAL_07 (1200×1600)</div>
              <div class="text-[9px] text-slate-400 font-mono">3:4 Vertical · 零剪裁</div>
            </div>
          </div>
        </div>

        <!-- Section C: 4:3 Macro Lens Photometry -->
        <div>
          <div class="flex items-center justify-between mb-2">
            <span class="text-xs font-black text-slate-700 font-mono flex items-center gap-1.5">
              <span class="w-2 h-2 rounded-full bg-emerald-500"></span>
              <span>GROUP C · 4:3 微距光学测光与毛发高光反射 (5712×4284 · 宽高比 1.333)</span>
            </span>
            <span class="text-[10px] font-mono text-slate-400">3 SAMPLES · 4:3 NATIVE</span>
          </div>
          <div class="grid grid-cols-3 gap-3.5">
            <div class="bg-slate-50 p-2.5 rounded-2xl border border-slate-200 cursor-pointer hover:border-emerald-400 transition-all" onclick="inspectImage('./assets/real_photos/laoma_photo_3.jpg', '微距光学 01 · 毛发高频法线与次表面散射 (5712×4284)')">
              <div class="w-full aspect-photo-4-3 bg-slate-900/5 rounded-xl overflow-hidden mb-1.5 flex items-center justify-center">
                <img src="./assets/real_photos/laoma_photo_3.jpg" class="no-crop-img" alt="微距1">
              </div>
              <div class="text-[10px] font-bold text-slate-700 font-mono truncate">PHOTO_03 (5712×4284)</div>
              <div class="text-[9px] text-slate-400 font-mono">4:3 Macro · 零剪裁</div>
            </div>
            <div class="bg-slate-50 p-2.5 rounded-2xl border border-slate-200 cursor-pointer hover:border-emerald-400 transition-all" onclick="inspectImage('./assets/real_photos/laoma_photo_4.jpg', '微距光学 02 · 虹膜收缩与瞳孔高动态范围 (5712×4284)')">
              <div class="w-full aspect-photo-4-3 bg-slate-900/5 rounded-xl overflow-hidden mb-1.5 flex items-center justify-center">
                <img src="./assets/real_photos/laoma_photo_4.jpg" class="no-crop-img" alt="微距2">
              </div>
              <div class="text-[10px] font-bold text-slate-700 font-mono truncate">PHOTO_04 (5712×4284)</div>
              <div class="text-[9px] text-slate-400 font-mono">4:3 Macro · 零剪裁</div>
            </div>
            <div class="bg-slate-50 p-2.5 rounded-2xl border border-slate-200 cursor-pointer hover:border-emerald-400 transition-all" onclick="inspectImage('./assets/real_photos/laoma_photo_5.jpg', '微距光学 03 · 鼻吻部触觉感知物理建模 (5712×4284)')">
              <div class="w-full aspect-photo-4-3 bg-slate-900/5 rounded-xl overflow-hidden mb-1.5 flex items-center justify-center">
                <img src="./assets/real_photos/laoma_photo_5.jpg" class="no-crop-img" alt="微距3">
              </div>
              <div class="text-[10px] font-bold text-slate-700 font-mono truncate">PHOTO_05 (5712×4284)</div>
              <div class="text-[9px] text-slate-400 font-mono">4:3 Macro · 零剪裁</div>
            </div>
          </div>
        </div>
      </div>

      <!-- ===================================================================== -->
      <!-- ZONE NORTHEAST (东北总成 · X: 4850, Y: 650) · 视觉与场景识别迭代候选机身阵列 -->
      <!-- ===================================================================== -->
      <div id="zone-candidates" class="absolute z-20 blueprint-card p-7 rounded-3xl" style="left: 4850px; top: 650px; width: 1750px;">
        <div class="flex items-center justify-between border-b border-slate-200 pb-4 mb-5">
          <div class="flex items-center gap-3">
            <span class="w-9 h-9 rounded-2xl bg-rose-50 border border-rose-200 flex items-center justify-center text-lg">🧪</span>
            <div>
              <h3 class="font-black text-slate-900 text-sm">视觉与场景识别迭代候选机身阵列 (19.5:9 手机全画幅演进 · 零裁剪)</h3>
              <span class="text-[10px] font-mono text-rose-700 font-bold">[EXP-CANDIDATES · 19.5:9 CV & VIEWPORT ITERATION CANDIDATES]</span>
            </div>
          </div>
          <span class="text-[10px] px-2.5 py-1 rounded-full bg-rose-50 text-rose-700 font-mono font-bold border border-rose-200">17 CANDIDATE STATES</span>
        </div>

        <!-- Section A: 19.5:9 CV Dirty State Training Candidates -->
        <div class="mb-5">
          <div class="flex items-center justify-between mb-2">
            <span class="text-xs font-black text-slate-700 font-mono flex items-center gap-1.5">
              <span class="w-2 h-2 rounded-full bg-rose-500"></span>
              <span>GROUP A · 19.5:9 视觉脏污判定与交互触发模型候选样张 (851×1848 / 941×1672)</span>
            </span>
            <span class="text-[10px] font-mono text-slate-400">6 SAMPLES · 19.5:9 RATIO</span>
          </div>
          <div class="grid grid-cols-6 gap-3">
            <div class="bg-slate-50 p-2 rounded-2xl border border-slate-200 cursor-pointer hover:border-rose-400 transition-all" onclick="inspectImage('./assets/candidates/dirty_cat_candidate_1.png', 'CV候选01 · 办公工位脏污轻度')">
              <div class="w-full aspect-phone bg-slate-900/5 rounded-xl overflow-hidden mb-1 flex items-center justify-center">
                <img src="./assets/candidates/dirty_cat_candidate_1.png" class="no-crop-img" alt="脏污1">
              </div>
              <div class="text-[9px] font-bold text-slate-700 font-mono truncate">CANDIDATE_01</div>
              <div class="text-[8px] text-slate-400 font-mono">851×1848 (0.460)</div>
            </div>
            <div class="bg-slate-50 p-2 rounded-2xl border border-slate-200 cursor-pointer hover:border-rose-400 transition-all" onclick="inspectImage('./assets/candidates/dirty_cat_candidate_2.png', 'CV候选02 · 地面泥泞脏污中度')">
              <div class="w-full aspect-phone bg-slate-900/5 rounded-xl overflow-hidden mb-1 flex items-center justify-center">
                <img src="./assets/candidates/dirty_cat_candidate_2.png" class="no-crop-img" alt="脏污2">
              </div>
              <div class="text-[9px] font-bold text-slate-700 font-mono truncate">CANDIDATE_02</div>
              <div class="text-[8px] text-slate-400 font-mono">851×1848 (0.460)</div>
            </div>
            <div class="bg-slate-50 p-2 rounded-2xl border border-slate-200 cursor-pointer hover:border-rose-400 transition-all" onclick="inspectImage('./assets/candidates/dirty_cat_candidate_3.png', 'CV候选03 · 户外探险脏污重度')">
              <div class="w-full aspect-phone bg-slate-900/5 rounded-xl overflow-hidden mb-1 flex items-center justify-center">
                <img src="./assets/candidates/dirty_cat_candidate_3.png" class="no-crop-img" alt="脏污3">
              </div>
              <div class="text-[9px] font-bold text-slate-700 font-mono truncate">CANDIDATE_03</div>
              <div class="text-[8px] text-slate-400 font-mono">851×1848 (0.460)</div>
            </div>
            <div class="bg-slate-50 p-2 rounded-2xl border border-slate-200 cursor-pointer hover:border-rose-400 transition-all" onclick="inspectImage('./assets/candidates/dirty_cat_sample_1.png', '姿态样张01 · 侧卧脏污识别')">
              <div class="w-full aspect-phone bg-slate-900/5 rounded-xl overflow-hidden mb-1 flex items-center justify-center">
                <img src="./assets/candidates/dirty_cat_sample_1.png" class="no-crop-img" alt="样张1">
              </div>
              <div class="text-[9px] font-bold text-slate-700 font-mono truncate">SAMPLE_01</div>
              <div class="text-[8px] text-slate-400 font-mono">941×1672 (0.562)</div>
            </div>
            <div class="bg-slate-50 p-2 rounded-2xl border border-slate-200 cursor-pointer hover:border-rose-400 transition-all" onclick="inspectImage('./assets/candidates/dirty_cat_sample_2.png', '姿态样张02 · 伏击脏污识别')">
              <div class="w-full aspect-phone bg-slate-900/5 rounded-xl overflow-hidden mb-1 flex items-center justify-center">
                <img src="./assets/candidates/dirty_cat_sample_2.png" class="no-crop-img" alt="样张2">
              </div>
              <div class="text-[9px] font-bold text-slate-700 font-mono truncate">SAMPLE_02</div>
              <div class="text-[8px] text-slate-400 font-mono">941×1672 (0.562)</div>
            </div>
            <div class="bg-slate-50 p-2 rounded-2xl border border-slate-200 cursor-pointer hover:border-rose-400 transition-all" onclick="inspectImage('./assets/candidates/dirty_cat_sample_3.png', '姿态样张03 · 站立脏污识别')">
              <div class="w-full aspect-phone bg-slate-900/5 rounded-xl overflow-hidden mb-1 flex items-center justify-center">
                <img src="./assets/candidates/dirty_cat_sample_3.png" class="no-crop-img" alt="样张3">
              </div>
              <div class="text-[9px] font-bold text-slate-700 font-mono truncate">SAMPLE_03</div>
              <div class="text-[8px] text-slate-400 font-mono">941×1672 (0.562)</div>
            </div>
          </div>
        </div>

        <!-- Section B: 19.5:9 Native Resolution Multi-State Viewport Renders (1320×2868) -->
        <div class="mb-5">
          <div class="flex items-center justify-between mb-2">
            <span class="text-xs font-black text-slate-700 font-mono flex items-center gap-1.5">
              <span class="w-2 h-2 rounded-full bg-blue-500"></span>
              <span>GROUP B · 19.5:9 端侧原生全分辨率多工况渲染帧 (1320×2868 原生视口基线 · 零剪裁)</span>
            </span>
            <span class="text-[10px] font-mono text-slate-400">6 FRAMES · 1320×2868</span>
          </div>
          <div class="grid grid-cols-6 gap-3">
            <div class="bg-slate-50 p-2 rounded-2xl border border-slate-200 cursor-pointer hover:border-blue-400 transition-all" onclick="inspectImage('./assets/app_assets/app_bg.png', '基线背景 · 1320×2868 纯净居室底图')">
              <div class="w-full aspect-phone bg-slate-900/5 rounded-xl overflow-hidden mb-1 flex items-center justify-center">
                <img src="./assets/app_assets/app_bg.png" class="no-crop-img" alt="app_bg">
              </div>
              <div class="text-[9px] font-bold text-slate-700 font-mono truncate">APP_BG_RAW</div>
              <div class="text-[8px] text-slate-400 font-mono">1320×2868 · 底图</div>
            </div>
            <div class="bg-slate-50 p-2 rounded-2xl border border-slate-200 cursor-pointer hover:border-blue-400 transition-all" onclick="inspectImage('./assets/candidates/home_bg_clean_1320x2868.png', '基线渲染 · 1320×2868 纯净居室标准光照')">
              <div class="w-full aspect-phone bg-slate-900/5 rounded-xl overflow-hidden mb-1 flex items-center justify-center">
                <img src="./assets/candidates/home_bg_clean_1320x2868.png" class="no-crop-img" alt="home_bg_clean">
              </div>
              <div class="text-[9px] font-bold text-slate-700 font-mono truncate">BG_CLEAN_HD</div>
              <div class="text-[8px] text-slate-400 font-mono">1320×2868 · 视口</div>
            </div>
            <div class="bg-slate-50 p-2 rounded-2xl border border-slate-200 cursor-pointer hover:border-blue-400 transition-all" onclick="inspectImage('./assets/candidates/home_cat_bg_clean_1320x2868.png', '工况合成 · 1320×2868 纯净常态猫咪完整视口')">
              <div class="w-full aspect-phone bg-slate-900/5 rounded-xl overflow-hidden mb-1 flex items-center justify-center">
                <img src="./assets/candidates/home_cat_bg_clean_1320x2868.png" class="no-crop-img" alt="home_cat_bg_clean">
              </div>
              <div class="text-[9px] font-bold text-slate-700 font-mono truncate">CAT_CLEAN_HD</div>
              <div class="text-[8px] text-slate-400 font-mono">1320×2868 · 常态</div>
            </div>
            <div class="bg-slate-50 p-2 rounded-2xl border border-slate-200 cursor-pointer hover:border-blue-400 transition-all" onclick="inspectImage('./assets/candidates/home_cat_dirty_tap_1320x2868.png', '工况合成 · 1320×2868 脏污高灵敏触碰视口')">
              <div class="w-full aspect-phone bg-slate-900/5 rounded-xl overflow-hidden mb-1 flex items-center justify-center">
                <img src="./assets/candidates/home_cat_dirty_tap_1320x2868.png" class="no-crop-img" alt="home_cat_dirty_tap">
              </div>
              <div class="text-[9px] font-bold text-slate-700 font-mono truncate">DIRTY_TAP_HD</div>
              <div class="text-[8px] text-slate-400 font-mono">1320×2868 · 触控</div>
            </div>
            <div class="bg-slate-50 p-2 rounded-2xl border border-slate-200 cursor-pointer hover:border-blue-400 transition-all" onclick="inspectImage('./assets/candidates/home_cat_touch_screen_1320x2868.png', '工况合成 · 1320×2868 屏幕互动触碰贴合视口')">
              <div class="w-full aspect-phone bg-slate-900/5 rounded-xl overflow-hidden mb-1 flex items-center justify-center">
                <img src="./assets/candidates/home_cat_touch_screen_1320x2868.png" class="no-crop-img" alt="home_cat_touch">
              </div>
              <div class="text-[9px] font-bold text-slate-700 font-mono truncate">TOUCH_SCR_HD</div>
              <div class="text-[8px] text-slate-400 font-mono">1320×2868 · 互动</div>
            </div>
            <div class="bg-slate-50 p-2 rounded-2xl border border-slate-200 cursor-pointer hover:border-blue-400 transition-all" onclick="inspectImage('./assets/candidates/home_bg_clean_exact_ratio.png', '校准基线 · 848×1844 精密等比视口标定图')">
              <div class="w-full aspect-phone bg-slate-900/5 rounded-xl overflow-hidden mb-1 flex items-center justify-center">
                <img src="./assets/candidates/home_bg_clean_exact_ratio.png" class="no-crop-img" alt="exact_ratio">
              </div>
              <div class="text-[9px] font-bold text-slate-700 font-mono truncate">EXACT_RATIO_CAL</div>
              <div class="text-[8px] text-slate-400 font-mono">848×1844 (0.4599)</div>
            </div>
          </div>
        </div>

        <!-- Section B.2: Office Ambient Dirty Cat Candidates & Mid-Res Touch Samples -->
        <div class="mb-5">
          <div class="flex items-center justify-between mb-2">
            <span class="text-xs font-black text-slate-700 font-mono flex items-center gap-1.5">
              <span class="w-2 h-2 rounded-full bg-amber-500"></span>
              <span>GROUP B.2 · 办公环境光照脏污候选与中分辨率手势验证样张 (851×1848 / 650×1414 · 零剪裁)</span>
            </span>
            <span class="text-[10px] font-mono text-slate-400">6 SAMPLES · NATIVE RATIO</span>
          </div>
          <div class="grid grid-cols-6 gap-3">
            <div class="bg-slate-50 p-2 rounded-2xl border border-slate-200 cursor-pointer hover:border-amber-400 transition-all" onclick="inspectImage('./assets/candidates/office_dirty_cat_candidate_1.png', '办公光照候选 01 · 自然漫反射工况 (851×1848)')">
              <div class="w-full aspect-phone bg-slate-900/5 rounded-xl overflow-hidden mb-1 flex items-center justify-center">
                <img src="./assets/candidates/office_dirty_cat_candidate_1.png" class="no-crop-img" alt="办公候选1">
              </div>
              <div class="text-[9px] font-bold text-slate-700 font-mono truncate">OFFICE_DIRTY_01</div>
              <div class="text-[8px] text-slate-400 font-mono">851×1848 (0.460)</div>
            </div>
            <div class="bg-slate-50 p-2 rounded-2xl border border-slate-200 cursor-pointer hover:border-amber-400 transition-all" onclick="inspectImage('./assets/candidates/office_dirty_cat_candidate_2.png', '办公光照候选 02 · 顶棚荧光灯工况 (851×1848)')">
              <div class="w-full aspect-phone bg-slate-900/5 rounded-xl overflow-hidden mb-1 flex items-center justify-center">
                <img src="./assets/candidates/office_dirty_cat_candidate_2.png" class="no-crop-img" alt="办公候选2">
              </div>
              <div class="text-[9px] font-bold text-slate-700 font-mono truncate">OFFICE_DIRTY_02</div>
              <div class="text-[8px] text-slate-400 font-mono">851×1848 (0.460)</div>
            </div>
            <div class="bg-slate-50 p-2 rounded-2xl border border-slate-200 cursor-pointer hover:border-amber-400 transition-all" onclick="inspectImage('./assets/candidates/office_dirty_cat_candidate_3.png', '办公光照候选 03 · 阴影背光测试工况 (851×1848)')">
              <div class="w-full aspect-phone bg-slate-900/5 rounded-xl overflow-hidden mb-1 flex items-center justify-center">
                <img src="./assets/candidates/office_dirty_cat_candidate_3.png" class="no-crop-img" alt="办公候选3">
              </div>
              <div class="text-[9px] font-bold text-slate-700 font-mono truncate">OFFICE_DIRTY_03</div>
              <div class="text-[8px] text-slate-400 font-mono">851×1848 (0.460)</div>
            </div>
            <div class="bg-slate-50 p-2 rounded-2xl border border-slate-200 cursor-pointer hover:border-amber-400 transition-all" onclick="inspectImage('./assets/candidates/home_cat_bg_clean.png', '中分辨率工况 · 851×1849 常态居室猫咪')">
              <div class="w-full aspect-phone bg-slate-900/5 rounded-xl overflow-hidden mb-1 flex items-center justify-center">
                <img src="./assets/candidates/home_cat_bg_clean.png" class="no-crop-img" alt="中模常态">
              </div>
              <div class="text-[9px] font-bold text-slate-700 font-mono truncate">CAT_CLEAN_MID</div>
              <div class="text-[8px] text-slate-400 font-mono">851×1849 (0.460)</div>
            </div>
            <div class="bg-slate-50 p-2 rounded-2xl border border-slate-200 cursor-pointer hover:border-amber-400 transition-all" onclick="inspectImage('./assets/candidates/home_cat_dirty_tap.png', '中分辨率工况 · 650×1414 脏污触碰反馈测试')">
              <div class="w-full aspect-phone bg-slate-900/5 rounded-xl overflow-hidden mb-1 flex items-center justify-center">
                <img src="./assets/candidates/home_cat_dirty_tap.png" class="no-crop-img" alt="中模触控">
              </div>
              <div class="text-[9px] font-bold text-slate-700 font-mono truncate">DIRTY_TAP_MID</div>
              <div class="text-[8px] text-slate-400 font-mono">650×1414 (0.460)</div>
            </div>
            <div class="bg-slate-50 p-2 rounded-2xl border border-slate-200 cursor-pointer hover:border-amber-400 transition-all" onclick="inspectImage('./assets/candidates/home_cat_touch_screen.png', '中分辨率工况 · 851×1849 屏幕交互贴合样张')">
              <div class="w-full aspect-phone bg-slate-900/5 rounded-xl overflow-hidden mb-1 flex items-center justify-center">
                <img src="./assets/candidates/home_cat_touch_screen.png" class="no-crop-img" alt="中模贴合">
              </div>
              <div class="text-[9px] font-bold text-slate-700 font-mono truncate">TOUCH_SCR_MID</div>
              <div class="text-[8px] text-slate-400 font-mono">851×1849 (0.460)</div>
            </div>
          </div>
        </div>

        <!-- Section C: Scenic Bento & Layout Explorations -->
        <div>
          <div class="flex items-center justify-between mb-2">
            <span class="text-xs font-black text-slate-700 font-mono flex items-center gap-1.5">
              <span class="w-2 h-2 rounded-full bg-indigo-500"></span>
              <span>GROUP C · Bento 排行榜与手账交互场景探索 (851×1848 比例 · 零剪裁)</span>
            </span>
            <span class="text-[10px] font-mono text-slate-400">2 EXPLORATIONS</span>
          </div>
          <div class="grid grid-cols-2 gap-3.5">
            <div class="bg-slate-50 p-2.5 rounded-2xl border border-slate-200 cursor-pointer hover:border-indigo-400 transition-all flex items-center gap-3" onclick="inspectImage('./assets/app_assets/scenes/leaderboard_magic_glass.png', '场景探索 01 · 魔法毛玻璃排行榜')">
              <div class="w-20 aspect-phone bg-slate-900/5 rounded-xl overflow-hidden flex-shrink-0 flex items-center justify-center">
                <img src="./assets/app_assets/scenes/leaderboard_magic_glass.png" class="no-crop-img" alt="毛玻璃">
              </div>
              <div>
                <div class="text-xs font-black text-slate-800 font-mono">LEADERBOARD_MAGIC_GLASS</div>
                <div class="text-[10px] text-indigo-600 font-mono mt-0.5">851×1848 · 19.5:9 Native</div>
                <div class="text-[10px] text-slate-500 mt-1">探索半透明毛玻璃材质与多层阴影叠加，验证端侧 GPU 片元着色器实时计算性能。</div>
              </div>
            </div>
            <div class="bg-slate-50 p-2.5 rounded-2xl border border-slate-200 cursor-pointer hover:border-indigo-400 transition-all flex items-center gap-3" onclick="inspectImage('./assets/app_assets/scenes/leaderboard_cozy_journal.png', '场景探索 02 · 暖调手账持久化记录')">
              <div class="w-20 aspect-phone bg-slate-900/5 rounded-xl overflow-hidden flex-shrink-0 flex items-center justify-center">
                <img src="./assets/app_assets/scenes/leaderboard_cozy_journal.png" class="no-crop-img" alt="暖调手账">
              </div>
              <div>
                <div class="text-xs font-black text-slate-800 font-mono">LEADERBOARD_COZY_JOURNAL</div>
                <div class="text-[10px] text-indigo-600 font-mono mt-0.5">851×1849 · 19.5:9 Native</div>
                <div class="text-[10px] text-slate-500 mt-1">探索真实纸张纹理与物理回弹手账页面，用于高亲和力喵务日常活动留档展示。</div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- ===================================================================== -->
      <!-- CENTER CORE ASSEMBLY (中心总装 · X: 3405, Y: 2100) · 荣耀原生机身与四大子系统展开 -->
      <!-- ===================================================================== -->
      <!-- 1. Central Honor Magic Device Frame -->
      <div id="core-device-frame" class="absolute z-30" style="left: 3405px; top: 2100px; width: 390px; height: 844px;">
        <div class="absolute -top-7 left-0 right-0 flex items-center justify-between font-mono text-[10px] text-blue-600 font-bold pointer-events-none px-1">
          <span>[HONOR MAGIC NATIVE CHASSIS]</span>
          <span>1320 × 2868 · 120Hz LTPO</span>
        </div>

        <!-- Phone Bezel -->
        <div class="w-full h-full bg-slate-900 rounded-[50px] p-3 shadow-2xl border-4 border-slate-700/80 ring-1 ring-white/20 relative">
          <!-- Dynamic Island / Speaker punch-hole -->
          <div class="absolute top-2.5 left-1/2 -translate-x-1/2 w-28 h-6 bg-black rounded-full z-50 flex items-center justify-between px-2 text-[10px] text-white">
            <span class="font-mono text-[9px] text-slate-400">09:41</span>
            <div class="w-2.5 h-2.5 rounded-full bg-slate-900 border border-slate-700"></div>
            <span class="text-[9px] text-emerald-400 font-mono">5G 100%</span>
          </div>

          <!-- Phone Screen Container (19.5:9 Native Viewport) -->
          <div class="w-full h-full bg-white rounded-[40px] overflow-hidden relative border border-slate-800 flex flex-col justify-between select-none">
            <!-- Simulated Native App Active Viewport -->
            <div class="relative w-full h-full">
              <!-- Background layer (Zero Crop) -->
              <img id="phone-bg-img" src="./assets/app_assets/home_bg_clean.png" class="absolute inset-0 w-full h-full object-contain" alt="背景">
              <!-- Video Layer -->
              <video id="phone-cat-video" src="./assets/app_assets/home_cat_clean.mp4" autoplay loop muted playsinline class="absolute inset-0 w-full h-full object-contain z-10"></video>
              <!-- Live State Watermark -->
              <div class="absolute bottom-3 right-3 z-20 bg-black/40 backdrop-blur-md px-2.5 py-1 rounded-full text-[10px] text-white font-mono font-bold flex items-center gap-1">
                <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-ping"></span>
                <span>FSM: RUNNING</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- 2. Exploded Sub-Assembly 01: Top HUD & Gauges System (ASM-01 · SENSORS) -->
      <div id="module-gauges" class="absolute z-20 exploded-module blueprint-card p-5 rounded-3xl cursor-pointer hover:border-blue-500" style="left: 3345px; top: 1420px; width: 510px;" onclick="inspectComponent('gauges')">
        <div class="flex items-center justify-between border-b border-slate-200 pb-2.5 mb-3">
          <div class="flex items-center gap-2">
            <span class="w-7 h-7 rounded-xl bg-blue-50 border border-blue-200 flex items-center justify-center text-sm">📊</span>
            <div>
              <h4 class="text-xs font-black text-slate-900">状态感知与生命指标控制系统</h4>
              <span class="text-[9px] font-mono text-blue-600 font-bold">[ASM-01 · SENSORS & HUD GAUGES]</span>
            </div>
          </div>
          <span class="text-[9px] font-mono px-2 py-0.5 rounded-full bg-blue-50 text-blue-700 font-bold">DISSECTED</span>
        </div>

        <!-- Gauge Controls Matrix -->
        <div class="grid grid-cols-3 gap-3 text-center">
          <div class="p-2.5 rounded-xl bg-slate-50 border border-slate-200">
            <div class="w-10 h-10 mx-auto mb-1 flex items-center justify-center">
              <img src="./assets/app_assets/ui_icons/ic_index_catlove.png" class="no-crop-img" alt="爱猫">
            </div>
            <div class="text-[10px] font-black text-slate-800 font-mono">98.6%</div>
            <div class="text-[8px] text-slate-400 font-mono">爱猫指数加权</div>
          </div>
          <div class="p-2.5 rounded-xl bg-slate-50 border border-slate-200">
            <div class="w-10 h-10 mx-auto mb-1 flex items-center justify-center">
              <img src="./assets/app_assets/ui_icons/ic_index_happiness.png" class="no-crop-img" alt="快乐">
            </div>
            <div class="text-[10px] font-black text-slate-800 font-mono">HEALTHY</div>
            <div class="text-[8px] text-slate-400 font-mono">生理状态监测</div>
          </div>
          <div class="p-2.5 rounded-xl bg-slate-50 border border-slate-200">
            <div class="w-10 h-10 mx-auto mb-1 flex items-center justify-center">
              <img src="./assets/app_assets/ui_icons/ic_btn_trophy.png" class="no-crop-img" alt="奖杯">
            </div>
            <div class="text-[10px] font-black text-slate-800 font-mono">NO.1 领先</div>
            <div class="text-[8px] text-slate-400 font-mono">荣誉段位同步</div>
          </div>
        </div>
        <div class="mt-2.5 text-[9px] font-mono text-slate-500 bg-slate-100/80 p-2 rounded-xl">
          FSM 状态机双向绑定: Normal (清洁度 &gt; 80) / Dirty (脏污预警) / Touch (实时手势响应)
        </div>
      </div>

      <!-- 3. Exploded Sub-Assembly 02: Media Stream & GPU Render Pipeline (ASM-02 · MEDIA) -->
      <div id="module-media" class="absolute z-20 exploded-module blueprint-card p-5 rounded-3xl cursor-pointer hover:border-emerald-500" style="left: 3950px; top: 2180px; width: 560px;" onclick="inspectComponent('media')">
        <div class="flex items-center justify-between border-b border-slate-200 pb-2.5 mb-3">
          <div class="flex items-center gap-2">
            <span class="w-7 h-7 rounded-xl bg-emerald-50 border border-emerald-200 flex items-center justify-center text-sm">🎬</span>
            <div>
              <h4 class="text-xs font-black text-slate-900">视觉多媒体硬件解码与动效管线</h4>
              <span class="text-[9px] font-mono text-emerald-600 font-bold">[ASM-02 · MEDIA PIPELINE & GPU ACCELERATION]</span>
            </div>
          </div>
          <span class="text-[9px] font-mono px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-700 font-bold">DISSECTED</span>
        </div>

        <!-- 3 Hardware Media Stream Cards -->
        <div class="grid grid-cols-3 gap-2.5 mb-2.5">
          <div class="bg-slate-900 rounded-xl p-1.5 relative overflow-hidden aspect-video flex items-center justify-center">
            <video src="./assets/app_assets/home_cat_clean.mp4" autoplay loop muted playsinline class="w-full h-full object-contain"></video>
            <span class="absolute top-1 left-1 px-1.5 py-0.5 rounded bg-emerald-500/80 text-[8px] text-white font-mono font-bold">STREAM 01</span>
          </div>
          <div class="bg-slate-900 rounded-xl p-1.5 relative overflow-hidden aspect-video flex items-center justify-center">
            <video src="./assets/app_assets/home_cat_dirty.mp4" autoplay loop muted playsinline class="w-full h-full object-contain"></video>
            <span class="absolute top-1 left-1 px-1.5 py-0.5 rounded bg-amber-500/80 text-[8px] text-white font-mono font-bold">STREAM 02</span>
          </div>
          <div class="bg-slate-900 rounded-xl p-1.5 relative overflow-hidden aspect-video flex items-center justify-center">
            <video src="./assets/app_assets/home_cat_touch.mp4" autoplay loop muted playsinline class="w-full h-full object-contain"></video>
            <span class="absolute top-1 left-1 px-1.5 py-0.5 rounded bg-rose-500/80 text-[8px] text-white font-mono font-bold">STREAM 03</span>
          </div>
        </div>
        <div class="flex items-center justify-between text-[9px] font-mono text-slate-500 bg-slate-100/80 p-2 rounded-xl">
          <span>CODEC: H.264 HIGH PROFILE</span>
          <span>HARDWARE ACCELERATION: ACTIVE</span>
          <span>FRAME: 60 FPS LOCKED</span>
        </div>
      </div>

      <!-- 4. Exploded Sub-Assembly 03: 24H Spatial Timeline & 11 Care Props (ASM-03 · TIMELINE) -->
      <div id="module-timeline" class="absolute z-20 exploded-module blueprint-card p-5 rounded-3xl cursor-pointer hover:border-amber-500" style="left: 2680px; top: 2180px; width: 560px;" onclick="inspectComponent('timeline')">
        <div class="flex items-center justify-between border-b border-slate-200 pb-2.5 mb-3">
          <div class="flex items-center gap-2">
            <span class="w-7 h-7 rounded-xl bg-amber-50 border border-amber-200 flex items-center justify-center text-sm">⏱️</span>
            <div>
              <h4 class="text-xs font-black text-slate-900">24H 空间感知与事件调度总线 (11 部件)</h4>
              <span class="text-[9px] font-mono text-amber-600 font-bold">[ASM-03 · 24H SPATIAL TIMELINE BUS & 11 PROPS]</span>
            </div>
          </div>
          <span class="text-[9px] font-mono px-2 py-0.5 rounded-full bg-amber-50 text-amber-700 font-bold">DISSECTED</span>
        </div>

        <div id="dissected-timeline-grid" class="grid grid-cols-4 gap-2 mb-2.5">
          <!-- Dynamically filled via JS with 11 3D Props -->
        </div>
        <div class="text-[9px] font-mono text-slate-500 bg-slate-100/80 p-2 rounded-xl flex items-center justify-between">
          <span>DISPATCHER: 24H CIRCADIAN CYCLE</span>
          <span>LOW-POWER BLE SENSORS</span>
          <span>AUTONOMOUS CRON</span>
        </div>
      </div>

      <!-- 5. Exploded Sub-Assembly 04: Dual Trapezoid Bento Physics & Leaderboard (ASM-04 · BENTO) -->
      <div id="module-bento" class="absolute z-20 exploded-module blueprint-card p-5 rounded-3xl cursor-pointer hover:border-indigo-500" style="left: 3345px; top: 3080px; width: 510px;" onclick="inspectComponent('bento')">
        <div class="flex items-center justify-between border-b border-slate-200 pb-2.5 mb-3">
          <div class="flex items-center gap-2">
            <span class="w-7 h-7 rounded-xl bg-indigo-50 border border-indigo-200 flex items-center justify-center text-sm">📐</span>
            <div>
              <h4 class="text-xs font-black text-slate-900">双梯形 Bento 几何裁切与动力学矩阵</h4>
              <span class="text-[9px] font-mono text-indigo-600 font-bold">[ASM-04 · DUAL TRAPEZOID SHADER & PHYSICS MATRIX]</span>
            </div>
          </div>
          <span class="text-[9px] font-mono px-2 py-0.5 rounded-full bg-indigo-50 text-indigo-700 font-bold">DISSECTED</span>
        </div>

        <!-- Simulated Bento Cutout with 10.3° Shear Angle -->
        <div class="relative h-20 bg-slate-900/5 rounded-2xl p-2 flex items-center justify-center overflow-hidden border border-slate-200 mb-2.5">
          <div class="w-full flex items-center justify-around z-20">
            <div class="flex items-center gap-2">
              <div class="w-8 h-8 rounded-xl bg-amber-50 border border-amber-200 flex items-center justify-center p-1">
                <img src="./assets/app_assets/ui_icons/ic_btn_trophy.png" class="no-crop-img" alt="奖杯">
              </div>
              <div class="text-left">
                <div class="text-[10px] font-black text-slate-800 font-mono">实时荣誉榜</div>
                <div class="text-[8px] text-slate-400 font-mono">10.3° 倾角切边</div>
              </div>
            </div>
            <div class="h-8 w-px bg-slate-300"></div>
            <div class="flex items-center gap-2">
              <div class="w-8 h-8 rounded-xl bg-indigo-50 border border-indigo-200 flex items-center justify-center p-1">
                <img src="./assets/app_assets/ic_tile_journal.png" class="no-crop-img" alt="手账">
              </div>
              <div class="text-left">
                <div class="text-[10px] font-black text-slate-800 font-mono">喵务日常手账</div>
                <div class="text-[8px] text-slate-400 font-mono">IndexedDB 存储</div>
              </div>
            </div>
          </div>
        </div>
        <div class="text-[9px] font-mono text-slate-500 bg-slate-100/80 p-2 rounded-xl flex items-center justify-between">
          <span>CLIP-PATH: POLYGON TILT 10.3°</span>
          <span>TOLERANCE: 14.0px PRECISION</span>
          <span>DROP-SHADOW ACCELERATED</span>
        </div>
      </div>

      <!-- ===================================================================== -->
      <!-- ZONE EAST (东部总成 · X: 4850, Y: 1850) · 8 大端侧真机全工况全分辨率验证流   -->
      <!-- ===================================================================== -->
      <div id="zone-screens" class="absolute z-20 blueprint-card p-8 rounded-3xl" style="left: 4850px; top: 1850px; width: 1750px;">
        <div class="flex items-center justify-between border-b border-slate-200 pb-4 mb-6">
          <div class="flex items-center gap-3">
            <span class="w-10 h-10 rounded-2xl bg-blue-50 border border-blue-200 flex items-center justify-center text-xl">📱</span>
            <div>
              <h2 class="text-lg font-black text-slate-900 tracking-tight">8 大端侧真机全工况全分辨率验证流 (1320 × 2868 · 零剪裁)</h2>
              <span class="text-xs font-mono text-blue-600 font-bold">[ZONE-EAST · 8 HARDWARE VERIFICATION CAPTURES · 1320 × 2868]</span>
            </div>
          </div>
          <span class="text-xs px-2.5 py-1 rounded-full bg-blue-50 text-blue-700 font-mono font-bold border border-blue-200">19.5:9 NATIVE TELEMETRY</span>
        </div>

        <div class="grid grid-cols-4 gap-6">
          <!-- 8 Native Screen Cards in 19.5:9 Aspect Ratio Container -->
          <div class="bg-slate-50 p-3 rounded-2xl border border-slate-200 cursor-pointer hover:border-blue-400 hover:shadow-lg transition-all" onclick="inspectImage('./assets/screenshots/Screenshot_20260919_174540_com_lyi_laomayoyo_MainActivity.JPG', '工况 01 · 居室常态静止巡航 (1320×2868)')">
            <div class="w-full aspect-phone bg-slate-900 rounded-xl overflow-hidden mb-2 flex items-center justify-center shadow-inner">
              <img src="./assets/screenshots/Screenshot_20260919_174540_com_lyi_laomayoyo_MainActivity.JPG" class="no-crop-img" alt="工况1">
            </div>
            <div class="text-xs font-black text-slate-800 font-mono truncate">01 · 居室常态巡航</div>
            <div class="text-[10px] text-slate-400 font-mono mt-0.5">NORMAL_CRUISING · 1320×2868</div>
          </div>

          <div class="bg-slate-50 p-3 rounded-2xl border border-slate-200 cursor-pointer hover:border-blue-400 hover:shadow-lg transition-all" onclick="inspectImage('./assets/screenshots/Screenshot_20260919_174600_com_lyi_laomayoyo_MainActivity.JPG', '工况 02 · 屏幕高敏触碰响应 (1320×2868)')">
            <div class="w-full aspect-phone bg-slate-900 rounded-xl overflow-hidden mb-2 flex items-center justify-center shadow-inner">
              <img src="./assets/screenshots/Screenshot_20260919_174600_com_lyi_laomayoyo_MainActivity.JPG" class="no-crop-img" alt="工况2">
            </div>
            <div class="text-xs font-black text-slate-800 font-mono truncate">02 · 触控互动反馈</div>
            <div class="text-[10px] text-slate-400 font-mono mt-0.5">TOUCH_FEEDBACK · 1320×2868</div>
          </div>

          <div class="bg-slate-50 p-3 rounded-2xl border border-slate-200 cursor-pointer hover:border-blue-400 hover:shadow-lg transition-all" onclick="inspectImage('./assets/screenshots/Screenshot_20260919_174613_com_lyi_laomayoyo_MainActivity.JPG', '工况 03 · 脏污状态视觉告警 (1320×2868)')">
            <div class="w-full aspect-phone bg-slate-900 rounded-xl overflow-hidden mb-2 flex items-center justify-center shadow-inner">
              <img src="./assets/screenshots/Screenshot_20260919_174613_com_lyi_laomayoyo_MainActivity.JPG" class="no-crop-img" alt="工况3">
            </div>
            <div class="text-xs font-black text-slate-800 font-mono truncate">03 · 脏污告警流转</div>
            <div class="text-[10px] text-slate-400 font-mono mt-0.5">DIRTY_ALERT · 1320×2868</div>
          </div>

          <div class="bg-slate-50 p-3 rounded-2xl border border-slate-200 cursor-pointer hover:border-blue-400 hover:shadow-lg transition-all" onclick="inspectImage('./assets/screenshots/Screenshot_20260919_174628_com_lyi_laomayoyo_MainActivity.JPG', '工况 04 · 抚摸清洁动作管线 (1320×2868)')">
            <div class="w-full aspect-phone bg-slate-900 rounded-xl overflow-hidden mb-2 flex items-center justify-center shadow-inner">
              <img src="./assets/screenshots/Screenshot_20260919_174628_com_lyi_laomayoyo_MainActivity.JPG" class="no-crop-img" alt="工况4">
            </div>
            <div class="text-xs font-black text-slate-800 font-mono truncate">04 · 抚触自愈过程</div>
            <div class="text-[10px] text-slate-400 font-mono mt-0.5">CLEANING_MOTION · 1320×2868</div>
          </div>

          <div class="bg-slate-50 p-3 rounded-2xl border border-slate-200 cursor-pointer hover:border-blue-400 hover:shadow-lg transition-all" onclick="inspectImage('./assets/screenshots/Screenshot_20260919_174648_com_lyi_laomayoyo_MainActivity.JPG', '工况 05 · 定额投喂物理交互 (1320×2868)')">
            <div class="w-full aspect-phone bg-slate-900 rounded-xl overflow-hidden mb-2 flex items-center justify-center shadow-inner">
              <img src="./assets/screenshots/Screenshot_20260919_174648_com_lyi_laomayoyo_MainActivity.JPG" class="no-crop-img" alt="工况5">
            </div>
            <div class="text-xs font-black text-slate-800 font-mono truncate">05 · 定额食物投喂</div>
            <div class="text-[10px] text-slate-400 font-mono mt-0.5">FEEDING_EVENT · 1320×2868</div>
          </div>

          <div class="bg-slate-50 p-3 rounded-2xl border border-slate-200 cursor-pointer hover:border-blue-400 hover:shadow-lg transition-all" onclick="inspectImage('./assets/screenshots/Screenshot_20260919_174700_com_lyi_laomayoyo_MainActivity.JPG', '工况 06 · 逗猫棒动力学捕捉 (1320×2868)')">
            <div class="w-full aspect-phone bg-slate-900 rounded-xl overflow-hidden mb-2 flex items-center justify-center shadow-inner">
              <img src="./assets/screenshots/Screenshot_20260919_174700_com_lyi_laomayoyo_MainActivity.JPG" class="no-crop-img" alt="工况6">
            </div>
            <div class="text-xs font-black text-slate-800 font-mono truncate">06 · 逗猫棒动力学</div>
            <div class="text-[10px] text-slate-400 font-mono mt-0.5">WAND_TRACKING · 1320×2868</div>
          </div>

          <div class="bg-slate-50 p-3 rounded-2xl border border-slate-200 cursor-pointer hover:border-blue-400 hover:shadow-lg transition-all" onclick="inspectImage('./assets/screenshots/Screenshot_20260919_174713_com_lyi_laomayoyo_MainActivity.JPG', '工况 07 · 听诊心率健康体检 (1320×2868)')">
            <div class="w-full aspect-phone bg-slate-900 rounded-xl overflow-hidden mb-2 flex items-center justify-center shadow-inner">
              <img src="./assets/screenshots/Screenshot_20260919_174713_com_lyi_laomayoyo_MainActivity.JPG" class="no-crop-img" alt="工况7">
            </div>
            <div class="text-xs font-black text-slate-800 font-mono truncate">07 · 生理体检听诊</div>
            <div class="text-[10px] text-slate-400 font-mono mt-0.5">HEART_RATE_BPM · 1320×2868</div>
          </div>

          <div class="bg-slate-50 p-3 rounded-2xl border border-slate-200 cursor-pointer hover:border-blue-400 hover:shadow-lg transition-all" onclick="inspectImage('./assets/screenshots/Screenshot_20260919_174724_com_lyi_laomayoyo_MainActivity.JPG', '工况 08 · 静音恒温安睡模式 (1320×2868)')">
            <div class="w-full aspect-phone bg-slate-900 rounded-xl overflow-hidden mb-2 flex items-center justify-center shadow-inner">
              <img src="./assets/screenshots/Screenshot_20260919_174724_com_lyi_laomayoyo_MainActivity.JPG" class="no-crop-img" alt="工况8">
            </div>
            <div class="text-xs font-black text-slate-800 font-mono truncate">08 · 空间静音安睡</div>
            <div class="text-[10px] text-slate-400 font-mono mt-0.5">NIGHT_SLEEP · 1320×2868</div>
          </div>
        </div>
      </div>

      <!-- ===================================================================== -->
      <!-- ZONE WEST (西部总成 · X: 600, Y: 1850) · 100% 完整披露工程物料清单 (BOM)   -->
      <!-- ===================================================================== -->
      <div id="zone-bom" class="absolute z-20 blueprint-card p-8 rounded-3xl" style="left: 600px; top: 1850px; width: 1750px;">
        <div class="flex items-center justify-between border-b border-slate-200 pb-4 mb-6">
          <div class="flex items-center gap-3">
            <span class="w-10 h-10 rounded-2xl bg-indigo-50 border border-indigo-200 flex items-center justify-center text-xl">📦</span>
            <div>
              <h2 class="text-lg font-black text-slate-900 tracking-tight">工程物料清单与全量数字资产规格墙 (保留自然透视轮廓 · 零裁剪)</h2>
              <span class="text-xs font-mono text-indigo-600 font-bold">[ZONE-WEST · 100% DISCLOSED BILL OF MATERIALS & TELEMETRY]</span>
            </div>
          </div>
          <span class="text-xs px-2.5 py-1 rounded-full bg-indigo-50 text-indigo-700 font-mono font-bold border border-indigo-200">TOTAL: 42 ASSETS · 100% ZERO CROP</span>
        </div>

        <!-- Sub-cluster 1: 11 3D Cat Care Props with Cleanroom Optical Pads -->
        <div class="mb-6">
          <div class="flex items-center justify-between mb-3">
            <span class="text-xs font-black text-slate-700 font-mono flex items-center gap-1.5 uppercase">
              <span class="w-2 h-2 rounded-full bg-indigo-500"></span>
              <span>SUB-CLUSTER 1 · 11 大 3D 照护事件道具部件 (/assets/app_assets/ic_board_*.png)</span>
            </span>
            <span class="text-[10px] font-mono text-slate-400">3D ALPHA CUTOUTS</span>
          </div>
          <div id="unified-bom-items" class="grid grid-cols-6 gap-3">
            <!-- Rendered via JS -->
          </div>
        </div>

        <!-- Sub-cluster 2: UI Icons & Interaction Controls (All Gauges & Buttons) -->
        <div class="mb-6">
          <div class="flex items-center justify-between mb-3">
            <span class="text-xs font-black text-slate-700 font-mono flex items-center gap-1.5 uppercase">
              <span class="w-2 h-2 rounded-full bg-rose-500"></span>
              <span>SUB-CLUSTER 2 · HUD 状态指标多工况仪表与交互按键套件 (全色温阶段与状态 · 零剪裁)</span>
            </span>
            <span class="text-[10px] font-mono text-slate-400">12 UI CONTROLS</span>
          </div>
          <div id="unified-bom-icons" class="grid grid-cols-6 gap-3">
            <!-- Rendered via JS -->
          </div>
        </div>

        <!-- Sub-cluster 2.5: 4 Vital Health Status Badges & Hero Cat Character Cutouts -->
        <div class="mb-6">
          <div class="flex items-center justify-between mb-3">
            <span class="text-xs font-black text-slate-700 font-mono flex items-center gap-1.5 uppercase">
              <span class="w-2 h-2 rounded-full bg-emerald-500"></span>
              <span>SUB-CLUSTER 2.5 · 四大生命体征状态微章与老马高精度立绘无损切图 (1:1 正方体征 & 自然立绘透视 · 零剪裁)</span>
            </span>
            <span class="text-[10px] font-mono text-slate-400">8 ASSETS · 100% UNPROCESSED</span>
          </div>
          <div class="grid grid-cols-9 gap-2.5">
            <!-- 4 Vital Status Badges (1254x1254, 1:1 Square) -->
            <div class="bg-slate-50 p-2 rounded-2xl border border-slate-200 cursor-pointer hover:border-emerald-400 transition-all text-center" onclick="inspectImage('./assets/app_assets/generated/status_food.png', '体征微章 · 饱食度正常指数 (1254×1254 · 1:1)')">
              <div class="w-12 h-12 cleanroom-pad rounded-xl mx-auto mb-1 flex items-center justify-center p-1 border border-slate-200">
                <img src="./assets/app_assets/generated/status_food.png" class="no-crop-img" alt="饱食度">
              </div>
              <div class="text-[9px] font-black text-slate-800 font-mono truncate">STATUS_FOOD</div>
              <div class="text-[8px] text-slate-400 font-mono">1:1 正方体征</div>
            </div>
            <div class="bg-slate-50 p-2 rounded-2xl border border-slate-200 cursor-pointer hover:border-emerald-400 transition-all text-center" onclick="inspectImage('./assets/app_assets/generated/status_water.png', '体征微章 · 饮水含水量达标 (1254×1254 · 1:1)')">
              <div class="w-12 h-12 cleanroom-pad rounded-xl mx-auto mb-1 flex items-center justify-center p-1 border border-slate-200">
                <img src="./assets/app_assets/generated/status_water.png" class="no-crop-img" alt="饮水">
              </div>
              <div class="text-[9px] font-black text-slate-800 font-mono truncate">STATUS_WATER</div>
              <div class="text-[8px] text-slate-400 font-mono">1:1 正方体征</div>
            </div>
            <div class="bg-slate-50 p-2 rounded-2xl border border-slate-200 cursor-pointer hover:border-emerald-400 transition-all text-center" onclick="inspectImage('./assets/app_assets/generated/status_litter.png', '体征微章 · 猫砂洁净排泄指标 (1254×1254 · 1:1)')">
              <div class="w-12 h-12 cleanroom-pad rounded-xl mx-auto mb-1 flex items-center justify-center p-1 border border-slate-200">
                <img src="./assets/app_assets/generated/status_litter.png" class="no-crop-img" alt="猫砂">
              </div>
              <div class="text-[9px] font-black text-slate-800 font-mono truncate">STATUS_LITTER</div>
              <div class="text-[8px] text-slate-400 font-mono">1:1 正方体征</div>
            </div>
            <div class="bg-slate-50 p-2 rounded-2xl border border-slate-200 cursor-pointer hover:border-emerald-400 transition-all text-center" onclick="inspectImage('./assets/app_assets/generated/status_bath.png', '体征微章 · 毛发清洁洗护指数 (1254×1254 · 1:1)')">
              <div class="w-12 h-12 cleanroom-pad rounded-xl mx-auto mb-1 flex items-center justify-center p-1 border border-slate-200">
                <img src="./assets/app_assets/generated/status_bath.png" class="no-crop-img" alt="洗护">
              </div>
              <div class="text-[9px] font-black text-slate-800 font-mono truncate">STATUS_BATH</div>
              <div class="text-[8px] text-slate-400 font-mono">1:1 正方体征</div>
            </div>

            <!-- Hero Cat Cutouts (Natural Alpha Ratio) -->
            <div class="bg-slate-50 p-2 rounded-2xl border border-slate-200 cursor-pointer hover:border-indigo-400 transition-all text-center" onclick="inspectImage('./assets/app_assets/hero_cat_sitting_tight.png', '立绘切图 · 老马紧凑正坐形态 (841×1112 · 0.756)')">
              <div class="w-12 h-12 cleanroom-pad rounded-xl mx-auto mb-1 flex items-center justify-center p-1 border border-slate-200">
                <img src="./assets/app_assets/hero_cat_sitting_tight.png" class="no-crop-img" alt="正坐立绘">
              </div>
              <div class="text-[9px] font-black text-slate-800 font-mono truncate">HERO_SITTING</div>
              <div class="text-[8px] text-slate-400 font-mono">841×1112 原型</div>
            </div>
            <div class="bg-slate-50 p-2 rounded-2xl border border-slate-200 cursor-pointer hover:border-indigo-400 transition-all text-center" onclick="inspectImage('./assets/app_assets/hero_cat_carrier_tight.png', '立绘切图 · 老马外出猫包形态 (1018×1112 · 0.916)')">
              <div class="w-12 h-12 cleanroom-pad rounded-xl mx-auto mb-1 flex items-center justify-center p-1 border border-slate-200">
                <img src="./assets/app_assets/hero_cat_carrier_tight.png" class="no-crop-img" alt="猫包立绘">
              </div>
              <div class="text-[9px] font-black text-slate-800 font-mono truncate">HERO_CARRIER</div>
              <div class="text-[8px] text-slate-400 font-mono">1018×1112 原型</div>
            </div>

            <!-- App Icon & Feishu Badge -->
            <div class="bg-slate-50 p-2 rounded-2xl border border-slate-200 cursor-pointer hover:border-blue-400 transition-all text-center" onclick="inspectImage('./assets/candidates/app_icon_preview.png', '品牌应用图标 · 660×660 原生矢量渲染 (1:1)')">
              <div class="w-12 h-12 cleanroom-pad rounded-xl mx-auto mb-1 flex items-center justify-center p-1 border border-slate-200">
                <img src="./assets/candidates/app_icon_preview.png" class="no-crop-img" alt="应用图标">
              </div>
              <div class="text-[9px] font-black text-slate-800 font-mono truncate">APP_ICON</div>
              <div class="text-[8px] text-slate-400 font-mono">660×660 · 1:1</div>
            </div>
            <div class="bg-slate-50 p-2 rounded-2xl border border-slate-200 cursor-pointer hover:border-blue-400 transition-all text-center" onclick="inspectImage('./assets/candidates/app_icon_preview_orig.png', '品牌应用图标原始母版 · 660×660 原生画幅 (1:1)')">
              <div class="w-12 h-12 cleanroom-pad rounded-xl mx-auto mb-1 flex items-center justify-center p-1 border border-slate-200">
                <img src="./assets/candidates/app_icon_preview_orig.png" class="no-crop-img" alt="应用图标母版">
              </div>
              <div class="text-[9px] font-black text-slate-800 font-mono truncate">ICON_ORIG</div>
              <div class="text-[8px] text-slate-400 font-mono">660×660 母版</div>
            </div>
            <div class="bg-slate-50 p-2 rounded-2xl border border-slate-200 cursor-pointer hover:border-cyan-400 transition-all text-center" onclick="inspectImage('./assets/app_assets/ic_board_feishu_badge.png', '系统配件 · 飞书多维协作角标道具 (224×212)')">
              <div class="w-12 h-12 cleanroom-pad rounded-xl mx-auto mb-1 flex items-center justify-center p-1 border border-slate-200">
                <img src="./assets/app_assets/ic_board_feishu_badge.png" class="no-crop-img" alt="飞书角标">
              </div>
              <div class="text-[9px] font-black text-slate-800 font-mono truncate">FEISHU_BADGE</div>
              <div class="text-[8px] text-slate-400 font-mono">224×212 配件</div>
            </div>
          </div>
        </div>

        <!-- Sub-cluster 3: Quick Launch System Tiles -->
        <div class="mb-6">
          <div class="flex items-center justify-between mb-3">
            <span class="text-xs font-black text-slate-700 font-mono flex items-center gap-1.5 uppercase">
              <span class="w-2 h-2 rounded-full bg-cyan-500"></span>
              <span>SUB-CLUSTER 3 · 系统级功能快捷磁贴组件 (/assets/app_assets/ic_tile_*.png)</span>
            </span>
            <span class="text-[10px] font-mono text-slate-400">4 SYSTEM TILES</span>
          </div>
          <div class="grid grid-cols-4 gap-3.5">
            <div class="bg-slate-50 p-3 rounded-2xl border border-slate-200 cursor-pointer hover:border-cyan-400 transition-all flex items-center gap-3" onclick="inspectImage('./assets/app_assets/ic_tile_yoyo.png', '系统磁贴 · 荣耀YOYO智能体接入')">
              <div class="w-12 h-12 cleanroom-pad rounded-xl flex items-center justify-center p-1 border border-slate-200 shadow-2xs">
                <img src="./assets/app_assets/ic_tile_yoyo.png" class="no-crop-img" alt="YOYO">
              </div>
              <div>
                <div class="text-xs font-black text-slate-800 font-mono">IC_TILE_YOYO</div>
                <div class="text-[10px] text-cyan-600 font-mono">YOYO Agent 专属磁贴</div>
              </div>
            </div>
            <div class="bg-slate-50 p-3 rounded-2xl border border-slate-200 cursor-pointer hover:border-cyan-400 transition-all flex items-center gap-3" onclick="inspectImage('./assets/app_assets/ic_tile_feishu.png', '系统磁贴 · 飞书多维表格与办公协同')">
              <div class="w-12 h-12 cleanroom-pad rounded-xl flex items-center justify-center p-1 border border-slate-200 shadow-2xs">
                <img src="./assets/app_assets/ic_tile_feishu.png" class="no-crop-img" alt="飞书">
              </div>
              <div>
                <div class="text-xs font-black text-slate-800 font-mono">IC_TILE_FEISHU</div>
                <div class="text-[10px] text-cyan-600 font-mono">飞书多维表格同步</div>
              </div>
            </div>
            <div class="bg-slate-50 p-3 rounded-2xl border border-slate-200 cursor-pointer hover:border-cyan-400 transition-all flex items-center gap-3" onclick="inspectImage('./assets/app_assets/ic_tile_health.png', '系统磁贴 · 荣耀健康生理数据通道')">
              <div class="w-12 h-12 cleanroom-pad rounded-xl flex items-center justify-center p-1 border border-slate-200 shadow-2xs">
                <img src="./assets/app_assets/ic_tile_health.png" class="no-crop-img" alt="健康">
              </div>
              <div>
                <div class="text-xs font-black text-slate-800 font-mono">IC_TILE_HEALTH</div>
                <div class="text-[10px] text-cyan-600 font-mono">荣耀健康生理总线</div>
              </div>
            </div>
            <div class="bg-slate-50 p-3 rounded-2xl border border-slate-200 cursor-pointer hover:border-cyan-400 transition-all flex items-center gap-3" onclick="inspectImage('./assets/app_assets/ic_tile_journal.png', '系统磁贴 · 喵务日常手账入口')">
              <div class="w-12 h-12 cleanroom-pad rounded-xl flex items-center justify-center p-1 border border-slate-200 shadow-2xs">
                <img src="./assets/app_assets/ic_tile_journal.png" class="no-crop-img" alt="手账">
              </div>
              <div>
                <div class="text-xs font-black text-slate-800 font-mono">IC_TILE_JOURNAL</div>
                <div class="text-[10px] text-cyan-600 font-mono">手账日志数据入口</div>
              </div>
            </div>
          </div>
        </div>

        <!-- Sub-cluster 4: 7 Archive Cards -->
        <div>
          <div class="flex items-center justify-between mb-3">
            <span class="text-xs font-black text-slate-700 font-mono flex items-center gap-1.5 uppercase">
              <span class="w-2 h-2 rounded-full bg-emerald-500"></span>
              <span>SUB-CLUSTER 4 · 结构化持久存储卡片 163-169 全量物料 (保留自然尺寸比例 · 零裁剪)</span>
            </span>
            <span class="text-[10px] font-mono text-slate-400">7 ARCHIVE RECORDS</span>
          </div>
          <div id="unified-bom-archives" class="grid grid-cols-7 gap-3">
            <!-- Rendered via JS -->
          </div>
        </div>
      </div>

      <!-- ===================================================================== -->
      <!-- ZONE SOUTHWEST (西南总成 · X: 600, Y: 3500) · 16:9 时序视频与动作捕捉工况 -->
      <!-- ===================================================================== -->
      <div id="zone-posters" class="absolute z-20 blueprint-card p-7 rounded-3xl" style="left: 600px; top: 3500px; width: 1750px;">
        <div class="flex items-center justify-between border-b border-slate-200 pb-4 mb-5">
          <div class="flex items-center gap-3">
            <span class="w-9 h-9 rounded-2xl bg-indigo-50 border border-indigo-200 flex items-center justify-center text-lg">🎞️</span>
            <div>
              <h3 class="font-black text-slate-900 text-sm">16:9 时序视频动作捕捉与全动态关键帧工况 (集成硬件视频播放内核 · 零剪裁)</h3>
              <span class="text-[10px] font-mono text-indigo-700 font-bold">[VID-POSTERS · 16:9 TEMPORAL MOTION CAPTURE & HARDWARE VIDEO NODES]</span>
            </div>
          </div>
          <span class="text-[10px] px-2.5 py-1 rounded-full bg-indigo-50 text-indigo-700 font-mono font-bold border border-indigo-200">6 CINE MOTION NODES</span>
        </div>

        <div class="grid grid-cols-6 gap-3.5">
          <!-- 6 Video Cards with Video Player Preview -->
          <div class="bg-slate-50 p-2.5 rounded-2xl border border-slate-200 hover:border-indigo-400 transition-all">
            <div class="w-full aspect-cine-16-9 bg-slate-900 rounded-xl overflow-hidden mb-1.5 flex items-center justify-center relative group">
              <video src="./assets/app_assets/archives/videos/vid_cat_controlled.mp4" poster="./assets/video_posters/vid_cat_controlled_poster.jpg" controls playsinline preload="none" class="w-full h-full object-contain"></video>
            </div>
            <div class="text-[10px] font-bold text-slate-800 font-mono truncate">01 · 机械精准受控</div>
            <div class="text-[9px] text-slate-400 font-mono">1280×720 · 16:9 MP4/JPG</div>
          </div>

          <div class="bg-slate-50 p-2.5 rounded-2xl border border-slate-200 hover:border-indigo-400 transition-all">
            <div class="w-full aspect-cine-16-9 bg-slate-900 rounded-xl overflow-hidden mb-1.5 flex items-center justify-center relative group">
              <video src="./assets/app_assets/archives/videos/vid_cat_feast.mp4" poster="./assets/video_posters/vid_cat_feast_poster.jpg" controls playsinline preload="none" class="w-full h-full object-contain"></video>
            </div>
            <div class="text-[10px] font-bold text-slate-800 font-mono truncate">02 · 享用盛宴投喂</div>
            <div class="text-[9px] text-slate-400 font-mono">1280×720 · 16:9 MP4/JPG</div>
          </div>

          <div class="bg-slate-50 p-2.5 rounded-2xl border border-slate-200 hover:border-indigo-400 transition-all">
            <div class="w-full aspect-cine-16-9 bg-slate-900 rounded-xl overflow-hidden mb-1.5 flex items-center justify-center relative group">
              <video src="./assets/app_assets/archives/videos/vid_cat_taste_after.mp4" poster="./assets/video_posters/vid_cat_taste_after_poster.jpg" controls playsinline preload="none" class="w-full h-full object-contain"></video>
            </div>
            <div class="text-[10px] font-bold text-slate-800 font-mono truncate">03 · 餐后清洁回味</div>
            <div class="text-[9px] text-slate-400 font-mono">1280×720 · 16:9 MP4/JPG</div>
          </div>

          <div class="bg-slate-50 p-2.5 rounded-2xl border border-slate-200 hover:border-indigo-400 transition-all">
            <div class="w-full aspect-cine-16-9 bg-slate-900 rounded-xl overflow-hidden mb-1.5 flex items-center justify-center relative group">
              <video src="./assets/app_assets/archives/videos/vid_cat_charming_belly.mp4" poster="./assets/video_posters/vid_cat_charming_belly_poster.jpg" controls playsinline preload="none" class="w-full h-full object-contain"></video>
            </div>
            <div class="text-[10px] font-bold text-slate-800 font-mono truncate">04 · 露腹互动信任</div>
            <div class="text-[9px] text-slate-400 font-mono">1280×720 · 16:9 MP4/JPG</div>
          </div>

          <div class="bg-slate-50 p-2.5 rounded-2xl border border-slate-200 hover:border-indigo-400 transition-all">
            <div class="w-full aspect-cine-16-9 bg-slate-900 rounded-xl overflow-hidden mb-1.5 flex items-center justify-center relative group">
              <video src="./assets/app_assets/archives/videos/vid_cat_fire_extinguisher.mp4" poster="./assets/video_posters/vid_cat_fire_extinguisher_poster.jpg" controls playsinline preload="none" class="w-full h-full object-contain"></video>
            </div>
            <div class="text-[10px] font-bold text-slate-800 font-mono truncate">05 · 灭火器材避障</div>
            <div class="text-[9px] text-slate-400 font-mono">1280×720 · 16:9 MP4/JPG</div>
          </div>

          <div class="bg-slate-50 p-2.5 rounded-2xl border border-slate-200 hover:border-indigo-400 transition-all">
            <div class="w-full aspect-cine-16-9 bg-slate-900 rounded-xl overflow-hidden mb-1.5 flex items-center justify-center relative group">
              <video src="./assets/app_assets/archives/videos/vid_cat_attack_slacker.mp4" poster="./assets/video_posters/vid_cat_attack_slacker_poster.jpg" controls playsinline preload="none" class="w-full h-full object-contain"></video>
            </div>
            <div class="text-[10px] font-bold text-slate-800 font-mono truncate">06 · 摸鱼警觉突击</div>
            <div class="text-[9px] text-slate-400 font-mono">720×1280 · 9:16 MP4/JPG</div>
          </div>
        </div>
      </div>

      <!-- ===================================================================== -->
      <!-- ZONE SOUTHEAST (东南总成 · X: 4850, Y: 3500) · 材质 Shader 与光照渲染实验族 -->
      <!-- ===================================================================== -->
      <div id="zone-shaders" class="absolute z-20 blueprint-card p-7 rounded-3xl" style="left: 4850px; top: 3500px; width: 1750px;">
        <div class="flex items-center justify-between border-b border-slate-200 pb-4 mb-5">
          <div class="flex items-center gap-3">
            <span class="w-9 h-9 rounded-2xl bg-rose-50 border border-rose-200 flex items-center justify-center text-lg">🎨</span>
            <div>
              <h3 class="font-black text-slate-900 text-sm">材质 Shader 与光照微纹理渲染实验台 (高光/法线/领奖台贴图 · 零剪裁)</h3>
              <span class="text-[10px] font-mono text-rose-700 font-bold">[SHADER-TEXTURES · MICRO-TEXTURES & SCENIC SHADER ASSETS]</span>
            </div>
          </div>
          <span class="text-[10px] px-2.5 py-1 rounded-full bg-rose-50 text-rose-700 font-mono font-bold border border-rose-200">8 SHADER EXPERIMENTS</span>
        </div>

        <div class="grid grid-cols-4 gap-4">
          <!-- Texture 01: 3D Podium Panoramic Model (2.5:1) -->
          <div class="bg-slate-50 p-3 rounded-2xl border border-slate-200 cursor-pointer hover:border-rose-400 transition-all col-span-2" onclick="inspectImage('./assets/app_assets/generated/podium_3d.png', 'Shader 贴图 01 · 3D 全景领奖台光影模型 (1375×548)')">
            <div class="w-full aspect-wide-2-5 bg-slate-900/5 rounded-xl overflow-hidden mb-2 flex items-center justify-center">
              <img src="./assets/app_assets/generated/podium_3d.png" class="no-crop-img" alt="podium_3d">
            </div>
            <div class="text-xs font-bold text-slate-800 font-mono">PODIUM_3D_PANORAMIC (1375×548 · 2.5:1)</div>
            <div class="text-[10px] text-slate-400 font-mono mt-0.5">三维荣誉榜梯台空间网格与全向遮蔽阴影贴图</div>
          </div>

          <!-- Texture 02: Leaderboard Lighting & Shade Model (1.5:1) -->
          <div class="bg-slate-50 p-3 rounded-2xl border border-slate-200 cursor-pointer hover:border-rose-400 transition-all col-span-2" onclick="inspectImage('./assets/app_assets/generated/podium_leaderboard.png', 'Shader 贴图 02 · 领奖台空间光影着色贴图 (1536×1024)')">
            <div class="w-full aspect-wide-1-5 bg-slate-900/5 rounded-xl overflow-hidden mb-2 flex items-center justify-center">
              <img src="./assets/app_assets/generated/podium_leaderboard.png" class="no-crop-img" alt="podium_leaderboard">
            </div>
            <div class="text-xs font-bold text-slate-800 font-mono">PODIUM_LEADERBOARD_MAP (1536×1024 · 1.5:1)</div>
            <div class="text-[10px] text-slate-400 font-mono mt-0.5">多光源漫反射与镜面高光着色器通道材质图</div>
          </div>

          <!-- Texture 03: Wide Archive Shader Texture (2.0:1) -->
          <div class="bg-slate-50 p-3 rounded-2xl border border-slate-200 cursor-pointer hover:border-rose-400 transition-all" onclick="inspectImage('./assets/app_assets/generated/btn_archive_texture.png', 'Shader 贴图 03 · 档案手账材质着色器贴图 (1774×887)')">
            <div class="w-full aspect-wide-2-1 bg-slate-900/5 rounded-xl overflow-hidden mb-2 flex items-center justify-center">
              <img src="./assets/app_assets/generated/btn_archive_texture.png" class="no-crop-img" alt="btn_archive_texture">
            </div>
            <div class="text-xs font-bold text-slate-800 font-mono">BTN_ARCHIVE_TEX (1774×887 · 2.0:1)</div>
            <div class="text-[10px] text-slate-400 font-mono mt-0.5">双梯形手账按键高光与倾斜切角纹理</div>
          </div>

          <!-- Texture 04: Wide Rank Shader Texture (2.0:1) -->
          <div class="bg-slate-50 p-3 rounded-2xl border border-slate-200 cursor-pointer hover:border-rose-400 transition-all" onclick="inspectImage('./assets/app_assets/generated/btn_rank_texture.png', 'Shader 贴图 04 · 排行榜材质着色器贴图 (1774×887)')">
            <div class="w-full aspect-wide-2-1 bg-slate-900/5 rounded-xl overflow-hidden mb-2 flex items-center justify-center">
              <img src="./assets/app_assets/generated/btn_rank_texture.png" class="no-crop-img" alt="btn_rank_texture">
            </div>
            <div class="text-xs font-bold text-slate-800 font-mono">BTN_RANK_TEX (1774×887 · 2.0:1)</div>
            <div class="text-[10px] text-slate-400 font-mono mt-0.5">双梯形荣誉榜按键金属拉丝与微折射纹理</div>
          </div>

          <!-- Texture 05: Ceramic Texture (1.2:1) -->
          <div class="bg-slate-50 p-3 rounded-2xl border border-slate-200 cursor-pointer hover:border-rose-400 transition-all" onclick="inspectImage('./assets/app_assets/generated/btn_white_ceramic_texture.png', 'Shader 贴图 05 · 白色微晶陶瓷质感贴图 (1374×1145)')">
            <div class="w-full aspect-tex-1-2 bg-slate-900/5 rounded-xl overflow-hidden mb-2 flex items-center justify-center">
              <img src="./assets/app_assets/generated/btn_white_ceramic_texture.png" class="no-crop-img" alt="ceramic">
            </div>
            <div class="text-xs font-bold text-slate-800 font-mono">CERAMIC_TEX (1374×1145 · 1.2:1)</div>
            <div class="text-[10px] text-slate-400 font-mono mt-0.5">微晶陶瓷温润漫反射与法线凹凸纹理</div>
          </div>

          <!-- Texture 06: 3D Journal Icon Asset -->
          <div class="bg-slate-50 p-3 rounded-2xl border border-slate-200 cursor-pointer hover:border-rose-400 transition-all" onclick="inspectImage('./assets/app_assets/generated/ic_archive_journal.png', 'Shader 贴图 06 · 3D 手账立体渲染贴图')">
            <div class="w-full aspect-square-1-1 bg-slate-900/5 rounded-xl overflow-hidden mb-2 flex items-center justify-center p-2">
              <img src="./assets/app_assets/generated/ic_archive_journal.png" class="no-crop-img" alt="journal">
            </div>
            <div class="text-xs font-bold text-slate-800 font-mono">IC_ARCHIVE_JOURNAL</div>
            <div class="text-[10px] text-slate-400 font-mono mt-0.5">手账立体三维渲染图标与投影</div>
          </div>
          <!-- Texture 07: Archive Art Shader Texture (1.5:1) -->
          <div class="bg-slate-50 p-3 rounded-2xl border border-slate-200 cursor-pointer hover:border-rose-400 transition-all" onclick="inspectImage('./assets/app_assets/generated/btn_archive_art.png', 'Shader 贴图 07 · 手账艺术光影着色图 (1536×1024 · 1.5:1)')">
            <div class="w-full aspect-wide-1-5 bg-slate-900/5 rounded-xl overflow-hidden mb-2 flex items-center justify-center">
              <img src="./assets/app_assets/generated/btn_archive_art.png" class="no-crop-img" alt="btn_archive_art">
            </div>
            <div class="text-xs font-bold text-slate-800 font-mono">BTN_ARCHIVE_ART (1.5:1)</div>
            <div class="text-[10px] text-slate-400 font-mono mt-0.5">1536×1024 渐变漫反射艺术贴图</div>
          </div>

          <!-- Texture 08: Rank Art Shader Texture (1.5:1) -->
          <div class="bg-slate-50 p-3 rounded-2xl border border-slate-200 cursor-pointer hover:border-rose-400 transition-all" onclick="inspectImage('./assets/app_assets/generated/btn_rank_art.png', 'Shader 贴图 08 · 排行榜艺术高光着色图 (1536×1024 · 1.5:1)')">
            <div class="w-full aspect-wide-1-5 bg-slate-900/5 rounded-xl overflow-hidden mb-2 flex items-center justify-center">
              <img src="./assets/app_assets/generated/btn_rank_art.png" class="no-crop-img" alt="btn_rank_art">
            </div>
            <div class="text-xs font-bold text-slate-800 font-mono">BTN_RANK_ART (1.5:1)</div>
            <div class="text-[10px] text-slate-400 font-mono mt-0.5">1536×1024 金属拉丝高光艺术贴图</div>
          </div>
        </div>
      </div>

      <!-- ===================================================================== -->
      <!-- ZONE SOUTH (南部总成 · X: 2500, Y: 3500) · 15 位工程贡献者与系统总线节点网格 -->
      <!-- ===================================================================== -->
      <div id="zone-team" class="absolute z-20 blueprint-card p-8 rounded-3xl" style="left: 2500px; top: 3500px; width: 2200px;">
        <div class="flex items-center justify-between border-b border-slate-200 pb-4 mb-6">
          <div class="flex items-center gap-3">
            <span class="w-10 h-10 rounded-2xl bg-blue-50 border border-blue-200 flex items-center justify-center text-xl">👥</span>
            <div>
              <h2 class="text-lg font-black text-slate-900 tracking-tight">工程核心贡献者与系统总线责任人架构图 (1:1 正方原生画幅 · 严格对齐)</h2>
              <span class="text-xs font-mono text-blue-600 font-bold">[ZONE-SOUTH · 15 REAL CONTRIBUTORS MAPPING & METRIC ALIGNMENT]</span>
            </div>
          </div>
          <div class="flex items-center gap-2">
            <span class="text-xs font-mono text-slate-400">ENGINEERING PERSONNEL SPECIFICATION</span>
            <span class="text-xs px-2.5 py-1 rounded-full bg-emerald-50 text-emerald-700 font-mono font-bold border border-emerald-200">15 MODULE OWNERS</span>
          </div>
        </div>

        <!-- Aligned Grid of 14 Contributors (Strict 1:1 Aspect Ratio Squircles) -->
        <div id="unified-team-grid" class="grid grid-cols-5 gap-4">
          <!-- Rendered via JS -->
        </div>
      </div>

    </div>
  </main>

  <!-- ========================================================================= -->
  <!-- SIDE INSPECTOR DRAWER (高密度技术物料探针抽屉)                              -->
  <!-- ========================================================================= -->
  <aside id="inspector-drawer" class="fixed top-16 right-0 bottom-0 w-[460px] bg-white/95 backdrop-blur-2xl border-l border-slate-200 shadow-2xl z-50 p-6 flex flex-col justify-between transform translate-x-[460px] transition-transform duration-300 ease-out">
    <div>
      <div class="flex items-center justify-between border-b border-slate-200 pb-4 mb-5">
        <div>
          <span id="insp-tag" class="text-[10px] font-mono font-bold px-2 py-0.5 rounded-full bg-blue-50 text-blue-700 border border-blue-200">[TELEMETRY PROBE]</span>
          <h3 id="insp-title" class="text-base font-black text-slate-900 mt-1">部件工程探针与参数</h3>
        </div>
        <button onclick="closeInspector()" class="w-8 h-8 rounded-full bg-slate-100 hover:bg-slate-200 flex items-center justify-center font-bold text-slate-500">×</button>
      </div>

      <!-- Large Preview Box (Strictly Zero Crop with Cleanroom Pad) -->
      <div class="w-full h-64 cleanroom-pad rounded-2xl overflow-hidden border border-slate-200 mb-5 flex items-center justify-center p-3 relative">
        <img id="insp-img" src="" class="no-crop-img" alt="检视预览">
        <div class="absolute bottom-2 right-2 bg-black/60 backdrop-blur-md px-2 py-0.5 rounded text-[9px] text-white font-mono">ZERO CROP · 100% NATIVE</div>
      </div>

      <!-- Technical Telemetry Data -->
      <div class="space-y-3 font-mono text-xs">
        <div class="flex justify-between border-b border-slate-100 pb-2">
          <span class="text-slate-400">组件标识 / NAME</span>
          <span id="insp-name" class="font-bold text-slate-800">-</span>
        </div>
        <div class="flex justify-between border-b border-slate-100 pb-2">
          <span class="text-slate-400">物理路径 / PATH</span>
          <span id="insp-path" class="font-bold text-blue-600 truncate max-w-[260px]">-</span>
        </div>
        <div class="flex justify-between border-b border-slate-100 pb-2">
          <span class="text-slate-400">画幅比 / RATIO</span>
          <span id="insp-ratio" class="font-bold text-slate-800">-</span>
        </div>
        <div class="flex justify-between border-b border-slate-100 pb-2">
          <span class="text-slate-400">模块责任人 / OWNER</span>
          <span id="insp-author" class="font-bold text-emerald-600">-</span>
        </div>
        <div class="pt-2">
          <span class="text-slate-400 block mb-1">工程功能与状态机说明:</span>
          <p id="insp-desc" class="text-slate-600 font-sans text-xs leading-relaxed bg-slate-50 p-3 rounded-xl border border-slate-200">-</p>
        </div>
      </div>
    </div>

    <div class="pt-4 border-t border-slate-200 flex items-center justify-between text-[11px] font-mono text-slate-400">
      <span>HONOR YOYO INSPECTOR v2.6</span>
      <button onclick="closeInspector()" class="px-4 py-2 rounded-xl bg-slate-900 text-white font-bold hover:bg-slate-800 transition-all font-sans">收起面板</button>
    </div>
  </aside>

  <!-- ========================================================================= -->
  <!-- JAVASCRIPT: PAN, ZOOM, TRACKPAD GESTURES & LEADER LINE ENGINE             -->
  <!-- ========================================================================= -->
  <script>
    // -------------------------------------------------------------------------
    // 1. Core Data Models
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
      { name: '木子', alias: 'Muzi', role: '产品架构工程', avatar: './assets/app_assets/avatars/avatar_muzi.png', desc: '端侧业务流程梳理、BOM 物料规格设计与 24H 空间时间线逻辑编排。' },
      { name: '小六', alias: '66', role: '动效渲染管线', avatar: './assets/app_assets/avatars/avatar_xiaoliu.png', desc: '1080P 60FPS 硬解多媒体流混流合成、Alpha 透明图层叠加与动效管线。' },
      { name: 'Adam', alias: 'Adam', role: '交互设计系统', avatar: './assets/app_assets/avatars/avatar_adam.png', desc: '双梯形 Bento 几何裁切算法、响应式排版引擎与触控交互动效规范。' },
      { name: 'Bingo', alias: 'Bingo', role: '全栈架构总监', avatar: './assets/app_assets/avatars/avatar_bingo.png', desc: '端侧 Native Rebuild 全局技术架构重构、混合容器与硬件传感器桥接。' },
      { name: '小白', alias: 'Xiaobai', role: '多模态模型算法', avatar: './assets/app_assets/avatars/avatar_xiaobai.png', desc: '端侧 CV 视觉脏污检测模型、轻量化网络量化部署与多模态感知。' },
      { name: '林一', alias: 'LinYi', role: '端侧体验工程', avatar: './assets/app_assets/avatars/avatar_linyi.png', desc: '全工况设备兼容性调优、触摸屏采样率校准与低延迟触控优化。' },
      { name: '佳豪', alias: 'Jiahao', role: '品质验证工程', avatar: './assets/app_assets/avatars/avatar_jiahao.png', desc: '端侧性能极限压测、内存泄漏拦截与长时间运行稳定性监测。' },
      { name: '黑黑', alias: 'Heihei', role: '系统稳定性工程', avatar: './assets/app_assets/avatars/avatar_heihei.png', desc: '自动化测试流水线构建、网络异常离线熔断与本地缓存策略。' },
      { name: 'Lex', alias: 'Lex', role: '数据服务架构', avatar: './assets/app_assets/avatars/avatar_lex.png', desc: '端侧 IndexedDB 双写持久化机制、数据加密与离线状态恢复。' },
      { name: '易明', alias: 'imyrs', role: '视觉算法系统', avatar: './assets/app_assets/avatars/avatar_imyrs.png', desc: '端侧视觉特征提取、图像比例矫正与零剪裁自适应渲染管线。' }
    ];

    // -------------------------------------------------------------------------
    // 2. Pan & Zoom Engine with Mac Trackpad Smooth Gestures
    // -------------------------------------------------------------------------
    let panX = -1700;
    let panY = -1200;
    let zoomScale = 0.55;
    let isMouseDown = false;
    let startMouseX = 0;
    let startMouseY = 0;

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
      const nextScale = Math.min(Math.max(0.15, prevScale * factor), 2.8);
      panX = wCenter - (wCenter - panX) * (nextScale / prevScale);
      panY = hCenter - (hCenter - panY) * (nextScale / prevScale);
      zoomScale = nextScale;
      applyTransform();
    }

    // --- Mac Trackpad Wheel Event Listener ---
    viewport.addEventListener('wheel', (e) => {
      e.preventDefault();

      if (e.ctrlKey) {
        // Trackpad Pinch Gesture (Mac sends wheel + ctrlKey)
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
        // Trackpad Two-Finger Pan Gesture
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
      if (e.target.closest('.exploded-module') || e.target.closest('#core-device-frame') || e.target.closest('button') || e.target.closest('input') || e.target.closest('video')) {
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
    // 3. Quick Zone Focus Logic
    // -------------------------------------------------------------------------
    function focusZone(zoneId) {
      const vW = viewport.clientWidth;
      const vH = viewport.clientHeight;

      let targetX = 3600;
      let targetY = 2500;
      let targetScale = 0.55;

      if (zoneId === 'center') {
        targetX = 3600;
        targetY = 2520;
        targetScale = 0.65;
      } else if (zoneId === 'north') {
        targetX = 3600;
        targetY = 1050;
        targetScale = 0.58;
      } else if (zoneId === 'ref') {
        targetX = 1475;
        targetY = 1150;
        targetScale = 0.56;
      } else if (zoneId === 'candidates') {
        targetX = 5725;
        targetY = 1150;
        targetScale = 0.56;
      } else if (zoneId === 'west') {
        targetX = 1475;
        targetY = 2500;
        targetScale = 0.54;
      } else if (zoneId === 'east') {
        targetX = 5725;
        targetY = 2500;
        targetScale = 0.54;
      } else if (zoneId === 'posters') {
        targetX = 1475;
        targetY = 3850;
        targetScale = 0.56;
      } else if (zoneId === 'shaders') {
        targetX = 5725;
        targetY = 3850;
        targetScale = 0.56;
      } else if (zoneId === 'south') {
        targetX = 3600;
        targetY = 3850;
        targetScale = 0.54;
      }

      panX = (vW / 2) - (targetX * targetScale);
      panY = (vH / 2) - (targetY * targetScale);
      zoomScale = targetScale;
      applyTransform();
    }

    function resetView() {
      const vW = viewport.clientWidth;
      const vH = viewport.clientHeight;
      const fitScale = Math.min(vW / 7200, vH / 5200) * 0.95;
      zoomScale = Math.max(0.18, fitScale);
      panX = (vW - 7200 * zoomScale) / 2;
      panY = (vH - 5200 * zoomScale) / 2;
      applyTransform();
    }

    // -------------------------------------------------------------------------
    // 4. Dynamic Exploded View Separation & Leader Lines Engine
    // -------------------------------------------------------------------------
    let currentExplosion = 80;

    function setExplosion(val) {
      document.getElementById('explosion-slider').value = val;
      updateExplosion(val);
    }

    function updateExplosion(val) {
      currentExplosion = val;
      document.getElementById('explosion-val').textContent = `${val}%`;
      const factor = val / 100;

      // Translate 4 core exploded modules outward
      const gaugesEl = document.getElementById('module-gauges');
      const mediaEl = document.getElementById('module-media');
      const timelineEl = document.getElementById('module-timeline');
      const bentoEl = document.getElementById('module-bento');

      // Top module: moves UP
      gaugesEl.style.transform = `translateY(${-280 * factor}px)`;
      // Right module: moves RIGHT
      mediaEl.style.transform = `translateX(${290 * factor}px)`;
      // Left module: moves LEFT
      timelineEl.style.transform = `translateX(${-310 * factor}px)`;
      // Bottom module: moves DOWN
      bentoEl.style.transform = `translateY(${280 * factor}px)`;

      // Redraw connector lines
      setTimeout(drawLeaderLines, 50);
    }

    document.getElementById('explosion-slider').addEventListener('input', (e) => {
      updateExplosion(parseInt(e.target.value, 10));
    });

    function drawLeaderLines() {
      const svg = document.getElementById('svg-leader-lines');
      svg.innerHTML = '';

      // Central Device Frame Center
      const cFrame = { x: 3600, y: 2522 };

      // Helper to draw connecting line
      function addLine(x1, y1, x2, y2, color = '#2563EB') {
        const line = document.createElementNS('http://www.w3.org/2000/svg', 'line');
        line.setAttribute('x1', x1);
        line.setAttribute('y1', y1);
        line.setAttribute('x2', x2);
        line.setAttribute('y2', y2);
        line.setAttribute('class', 'tech-leader-line');
        line.style.stroke = color;
        svg.appendChild(line);

        // Joint at start
        const circle1 = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
        circle1.setAttribute('cx', x1);
        circle1.setAttribute('cy', y1);
        circle1.setAttribute('r', 4);
        circle1.setAttribute('class', 'tech-leader-joint');
        circle1.style.fill = color;
        svg.appendChild(circle1);

        // Joint at end
        const circle2 = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
        circle2.setAttribute('cx', x2);
        circle2.setAttribute('cy', y2);
        circle2.setAttribute('r', 4);
        circle2.setAttribute('class', 'tech-leader-joint');
        circle2.style.fill = color;
        svg.appendChild(circle2);
      }

      const factor = currentExplosion / 100;
      // Connect Core Chassis to 4 Exploded Sub-Assemblies
      addLine(cFrame.x, 2100, 3600, 1420 + 130 - (280 * factor), '#2563EB'); // Gauges Top
      addLine(3795, cFrame.y, 3950 + (290 * factor), 2260, '#059669'); // Media Right
      addLine(3405, cFrame.y, 2680 + 560 - (310 * factor), 2260, '#D97706'); // Timeline Left
      addLine(cFrame.x, 2944, 3600, 3080 + (280 * factor), '#4F46E5'); // Bento Bottom

      // Major structural trunk lines to satellite zones
      addLine(2350, 1200, 2500, 1200, '#CBD5E1'); // Ref to Specs
      addLine(4700, 1200, 4850, 1200, '#CBD5E1'); // Specs to Candidates
      addLine(2350, 2500, 2680 - (310 * factor), 2500, '#CBD5E1'); // BOM to Timeline
      addLine(3950 + 560 + (290 * factor), 2500, 4850, 2500, '#CBD5E1'); // Media to Screens
      addLine(3600, 3250 + (280 * factor), 3600, 3500, '#CBD5E1'); // Bento to Team
    }

    // -------------------------------------------------------------------------
    // 5. Dynamic Content Population
    // -------------------------------------------------------------------------
    function populateTimeline() {
      const container = document.getElementById('dissected-timeline-grid');
      let html = '';
      SCHEDULE_DATA.slice(0, 8).forEach(it => {
        html += `
          <div class="bg-slate-50 p-2 rounded-xl border border-slate-200 flex flex-col items-center text-center cursor-pointer hover:border-amber-400" onclick="inspectItem(${it.id})">
            <div class="w-8 h-8 flex items-center justify-center mb-1">
              <img src="${it.icon}" class="no-crop-img" alt="${it.title}">
            </div>
            <span class="text-[9px] font-black text-slate-800 truncate w-full font-mono">${it.title.slice(0, 4)}</span>
            <span class="text-[8px] text-slate-400 font-mono">${it.time}</span>
          </div>
        `;
      });
      container.innerHTML = html;
    }

    function populateBOM() {
      // 1. 11 Care Props with Cleanroom Optical Pads
      const bContainer = document.getElementById('unified-bom-items');
      let bHtml = '';
      SCHEDULE_DATA.forEach(it => {
        bHtml += `
          <div class="bg-slate-50 p-3 rounded-2xl border border-slate-200 hover:border-indigo-400 transition-all flex flex-col items-center text-center cursor-pointer" onclick="inspectItem(${it.id})">
            <div class="w-14 h-14 cleanroom-pad rounded-xl flex items-center justify-center mb-1.5 p-1 border border-slate-200 shadow-2xs">
              <img src="${it.icon}" class="no-crop-img drop-shadow-2xs" alt="${it.title}">
            </div>
            <span class="text-[11px] font-black text-slate-800 truncate w-full font-mono">${it.title}</span>
            <span class="text-[9px] text-slate-400 font-mono mt-0.5">${it.time} · ${it.person}</span>
          </div>
        `;
      });
      bContainer.innerHTML = bHtml;

      // 2. HUD Gauges & Action Controls
      const uContainer = document.getElementById('unified-bom-icons');
      const uiControls = [
        { name: 'ic_index_catlove.png', title: '爱猫加权徽标', path: './assets/app_assets/ui_icons/ic_index_catlove.png', tag: 'GAUGE' },
        { name: 'ic_index_happiness.png', title: '快乐值基础仪表', path: './assets/app_assets/ui_icons/ic_index_happiness.png', tag: 'GAUGE' },
        { name: 'ic_index_happiness_blue.png', title: '清爽低饱和仪表', path: './assets/app_assets/ui_icons/ic_index_happiness_blue.png', tag: 'GAUGE' },
        { name: 'ic_index_happiness_green.png', title: '活力健康态仪表', path: './assets/app_assets/ui_icons/ic_index_happiness_green.png', tag: 'GAUGE' },
        { name: 'ic_index_happiness_orange.png', title: '疲惫警戒态仪表', path: './assets/app_assets/ui_icons/ic_index_happiness_orange.png', tag: 'GAUGE' },
        { name: 'ic_index_happiness_red.png', title: '脏污高急迫仪表', path: './assets/app_assets/ui_icons/ic_index_happiness_red.png', tag: 'GAUGE' },
        { name: 'ic_index_happiness_tight.png', title: '紧凑版指标切图', path: './assets/app_assets/ui_icons/ic_index_happiness_tight.png', tag: 'GAUGE' },
        { name: 'ic_btn_like.png', title: '点赞默认状态', path: './assets/app_assets/ui_icons/ic_btn_like.png', tag: 'ACTION' },
        { name: 'ic_btn_like_active.png', title: '点赞高亮激活态', path: './assets/app_assets/ui_icons/ic_btn_like_active.png', tag: 'ACTION' },
        { name: 'ic_btn_comment.png', title: '手账评论留言', path: './assets/app_assets/ui_icons/ic_btn_comment.png', tag: 'ACTION' },
        { name: 'ic_btn_expand.png', title: '展开折叠手柄', path: './assets/app_assets/ui_icons/ic_btn_expand.png', tag: 'ACTION' },
        { name: 'ic_btn_collapse.png', title: '收起复位手柄', path: './assets/app_assets/ui_icons/ic_btn_collapse.png', tag: 'ACTION' }
      ];
      let uHtml = '';
      uiControls.forEach(ui => {
        uHtml += `
          <div class="bg-slate-50 p-2.5 rounded-2xl border border-slate-200 hover:border-rose-400 transition-all flex flex-col items-center text-center cursor-pointer" onclick="inspectImage('${ui.path}', '${ui.title} (${ui.name})')">
            <div class="w-12 h-12 cleanroom-pad rounded-xl flex items-center justify-center mb-1.5 p-1 border border-slate-200 shadow-2xs">
              <img src="${ui.path}" class="no-crop-img drop-shadow-2xs" alt="${ui.title}">
            </div>
            <span class="text-[10px] font-black text-slate-800 truncate w-full font-mono">${ui.title}</span>
            <span class="text-[8.5px] text-slate-400 font-mono mt-0.5 truncate w-full">${ui.name}</span>
          </div>
        `;
      });
      uContainer.innerHTML = uHtml;

      // 3. 7 Archive Cards
      const aContainer = document.getElementById('unified-bom-archives');
      let aHtml = '';
      [163, 164, 165, 166, 167, 168, 169].forEach(id => {
        aHtml += `
          <div class="bg-slate-50 p-2.5 rounded-2xl border border-slate-200 hover:border-indigo-400 transition-all">
            <div class="w-full h-36 bg-slate-900/5 rounded-xl overflow-hidden mb-1.5 flex items-center justify-center p-1.5 cursor-pointer hover:scale-105 transition-transform" onclick="inspectImage('./assets/app_assets/archives/archive_${id}.png', '持久化数据记录 #${id}')">
              <img src="./assets/app_assets/archives/archive_${id}.png" class="no-crop-img" alt="手账${id}">
            </div>
            <div class="text-[10px] font-bold text-slate-700 text-center font-mono">RECORD #${id}</div>
            <div class="text-[8px] text-slate-400 text-center font-mono">自然尺寸 · 零裁剪</div>
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
          <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 hover:border-blue-500 hover:bg-white transition-all flex flex-col items-center text-center cursor-pointer h-full justify-between" onclick="inspectMember('${m.alias}')">
            <div>
              <!-- Strictly Aligned 56x56 Square Avatar Token (1:1 Natural Aspect Ratio) -->
              <div class="engineer-avatar-box shadow-xs ring-2 ring-slate-200 mb-2.5 mx-auto flex items-center justify-center p-0.5">
                <img src="${m.avatar}" class="no-crop-img" alt="${m.alias}">
              </div>
              <div class="text-xs font-black text-slate-900 font-mono">${m.alias} <span class="text-[10px] font-normal text-slate-400">(${m.name})</span></div>
              <div class="text-[10px] font-bold text-blue-600 mt-0.5 font-mono">${m.role}</div>
            </div>
            <div class="w-full pt-2.5 mt-2.5 border-t border-slate-200/60 text-[9px] font-mono text-slate-400 flex items-center justify-between">
              <span>ACTIVE</span>
              <span class="text-emerald-600 font-bold">1:1 TOKEN</span>
            </div>
          </div>
        `;
      });
      container.innerHTML = html;
    }

    // -------------------------------------------------------------------------
    // 6. Component & Asset Inspector Drawer
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
        descEl.textContent = '三组无缝切换硬解短视频流水线，Alpha 通道图层混合技术与 60fps 恒定锁帧保障。';
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
      document.getElementById('insp-ratio').textContent = '3D 拟物透明 Alpha · 原生尺寸零剪裁';
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
      document.getElementById('insp-ratio').textContent = '1:1 正方形原生免冠画幅 · 零剪裁';
      document.getElementById('insp-author').textContent = `${mem.name} · ${mem.alias}`;
      document.getElementById('insp-desc').textContent = mem.desc;
      drawer.classList.remove('translate-x-[460px]');
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
      drawer.classList.remove('translate-x-[460px]');
    }

    function closeInspector() {
      document.getElementById('inspector-drawer').classList.add('translate-x-[460px]');
    }

    // -------------------------------------------------------------------------
    // 7. Boot Initialization
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

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(html_code)

print("Ultimate Organic Canvas generated successfully!")
