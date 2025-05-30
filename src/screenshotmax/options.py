from dataclasses import dataclass, field, asdict
from typing import Optional, List, Dict, Any


@dataclass
class BaseOptions:
  url: Optional[str] = None
  gpu_rendering: Optional[bool] = None
  capture_beyond_viewport: Optional[bool] = None
  viewport_device: Optional[str] = None
  viewport_width: Optional[int] = None
  viewport_height: Optional[int] = None
  viewport_landscape: Optional[bool] = None
  viewport_has_touch: Optional[bool] = None
  viewport_mobile: Optional[bool] = None
  device_scale_factor: Optional[float] = None
  attachment_name: Optional[str] = None
  dark_mode: Optional[bool] = None
  reduced_motion: Optional[bool] = None
  media_type: Optional[str] = None
  vision_deficiency: Optional[str] = None
  clip_x: Optional[int] = None
  clip_y: Optional[int] = None
  clip_width: Optional[int] = None
  clip_height: Optional[int] = None
  block_annoyance: Optional[str] = None
  block_ressources: Optional[List[str]] = field(default_factory=list)
  geolocation_accuracy: Optional[int] = None
  geolocation_latitude: Optional[float] = None
  geolocation_longitude: Optional[float] = None
  timezone: Optional[str] = None
  hide_selectors: Optional[List[str]] = field(default_factory=list)
  click_selector: Optional[str] = None
  authorization: Optional[str] = None
  user_agent: Optional[str] = None
  cookies: Optional[List[str]] = field(default_factory=list)
  headers: Optional[List[str]] = field(default_factory=list)
  bypass_csp: Optional[bool] = None
  ip_location: Optional[str] = None
  proxy: Optional[str] = None
  delay: Optional[int] = None
  timeout: Optional[int] = None
  wait_until: Optional[List[str]] = field(default_factory=list)
  cache: Optional[bool] = None
  cache_ttl: Optional[int] = None
  metadata_icon: Optional[bool] = None
  metadata_fonts: Optional[bool] = None
  metadata_title: Optional[bool] = None
  metadata_hash: Optional[bool] = None
  metadata_status: Optional[bool] = None
  metadata_headers: Optional[bool] = None
  async_: Optional[bool] = None
  webhook_url: Optional[str] = None
  webhook_signed: Optional[bool] = None

  def to_dict(self) -> Dict[str, Any]:
    result = asdict(self)
    # rename async_ to async if present
    if result.get("async_") is not None:
      result["async"] = result.pop("async_")
    else:
      result.pop("async_")
    return {k: v for k, v in result.items() if v is not None}


@dataclass
class ScreenshotOptions(BaseOptions):
  html: Optional[str] = None
  format: Optional[str] = None
  full_page: Optional[bool] = None
  full_page_scroll: Optional[bool] = None
  full_page_scroll_by_amount: Optional[int] = None
  full_page_scroll_by_duration: Optional[int] = None
  image_quality: Optional[int] = None
  image_width: Optional[int] = None
  image_height: Optional[int] = None
  omit_background: Optional[bool] = None
  metadata_image_size: Optional[bool] = None
  signature: Optional[str] = None


@dataclass
class PDFOptions(BaseOptions):
  html: Optional[str] = None
  pdf_paper_format: Optional[str] = None
  pdf_landscape: Optional[bool] = None
  pdf_print_background: Optional[bool] = None
  signature: Optional[str] = None


@dataclass
class ScreencastOptions(BaseOptions):
  format: Optional[str] = None
  duration: Optional[int] = None
  scenario: Optional[str] = None
  scroll_by_amount: Optional[int] = None
  scroll_by_delay: Optional[int] = None
  scroll_by_duration: Optional[int] = None
  scroll_back: Optional[bool] = None
  scroll_back_delay: Optional[int] = None
  scroll_easing: Optional[str] = None
  signature: Optional[str] = None


@dataclass
class ScrapeOptions(BaseOptions):
  format: Optional[str] = None
  js_enabled: Optional[bool] = None
  signature: Optional[str] = None
