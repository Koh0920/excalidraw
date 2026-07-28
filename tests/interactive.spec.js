import { expect, test } from "@playwright/test";

test("opens the product-flow scene and permits drawing plus undo", async ({
  page,
}) => {
  await page.goto("/");
  await expect(page.locator("body")).toHaveAttribute(
    "data-ato-demo",
    "product-flow",
  );
  await expect(page.locator("canvas")).toBeVisible();

  await page.getByRole("button", { name: /rectangle/i }).click();
  await page.mouse.move(300, 350);
  await page.mouse.down();
  await page.mouse.move(430, 430);
  await page.mouse.up();
  await expect(page.getByRole("button", { name: /undo/i })).toBeEnabled();
  await page.getByRole("button", { name: /undo/i }).click();
});
